import threading
import cv2

from recognize_faces_image import get_id

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Users/bakseo3060/Desktop/nepp-serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nepp-577ae.firebaseio.com/'
})
time = 0
#시간x학번 별 인식 데이터 매트릭스
time_id_matrix = {}

def set_interval(func, sec):
    global time
    def func_wrapper():
        global time
        time+=1
        set_interval(func, sec) 
        func()
    
    t = threading.Timer(sec, func_wrapper)
    t.start()
    if(time>5):
        t.cancel()
    return t

CAM_ID = 0

def capture(camid=CAM_ID):
    global time
    global t
    cam = cv2.VideoCapture(camid)
    if cam.isOpened() == False:
        print('cant open the cam (%d)' % camid)
        return None
    ret, frame = cam.read()
    if frame is None:
        print('frame is not exist')
        return None

    # png로 압축 없이 영상 저장
    cv2.imwrite('/Users/bakseo3060/Desktop/nepp_git/face-recognition-opencv/examples/Capture.png', frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
    cam.release()
    print(get_id()) #검출된 학생 학번 출력.
    id_list = get_id()
    for id_val in id_list:    
        if id_val != "Unknown":
            if id_val not in time_id_matrix.keys():
                time_id_matrix[id_val] = []
                for i in range(100):
                    time_id_matrix[id_val].append(0)
            time_id_matrix[id_val][time] = 1 #있으면 1 로 바꿔줌
def analystic():
    #

    ref = db.reference('students')

    student_list = []
    studentIds = list(ref.get().keys())

    for i in range(len(studentIds)-2):
        student_list.append(studentIds[i])

    studtent_absent_list = {}
    #
    print(student_list)
    id_list_from_db = student_list
    for id_val in id_list_from_db:
        if id_val not in studtent_absent_list.keys():
            studtent_absent_list[id_val] = 0

        for time_val in range(0,98):
            flag = time_id_matrix[id_val][time_val] + time_id_matrix[id_val][time_val+1] + time_val[id_val][time_val+2]
            if time_val != 0 and flag == 0:    # 조퇴 표시
                studtent_absent_list[id_val] = 4
            elif time_val == 0 and flag == 0:
                studtent_absent_list[id_val] = 2
            elif time_val == 0 and flag <= 2:
                studtent_absent_list[id_val] = 3
            elif time_val != 0  and flag <= 2:
                studtent_absent_list[id_val] = 1
            

    print(studtent_absent_list)        
            
"""0 미출결
1 출석
2 결석
3 지각
4 조퇴"""
if __name__ == '__main__':
    timer=set_interval(capture,30)
    analystic
    #timer.cancle()