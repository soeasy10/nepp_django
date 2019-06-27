# face-recognition-opencv/recognize_faces_image.py

# USAGE
# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png 

# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# load the known faces and embeddings
# print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

# load the input image and convert it from BGR to RGB
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# detect the (x, y)-coordinates of the bounding boxes corresponding
# to each face in the input image, then compute the facial embeddings
# for each face
# print("[INFO] recognizing faces...")
boxes = face_recognition.face_locations(rgb,
	model=args["detection_method"])
encodings = face_recognition.face_encodings(rgb, boxes)

# initialize the list of names for each face detected
names = []

# loop over the facial embeddings
for encoding in encodings:
	# attempt to match each face in the input image to our known
	# encodings
	matches = face_recognition.compare_faces(data["encodings"],
		encoding)
	name = "Unknown"

	# check to see if we have found a match
	if True in matches:
		# find the indexes of all matched faces then initialize a
		# dictionary to count the total number of times each face
		# was matched
		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		counts = {}

		# loop over the matched indexes and maintain a count for
		# each recognized face face
		for i in matchedIdxs:
			name = data["names"][i]
			counts[name] = counts.get(name, 0) + 1

		# determine the recognized face with the largest number of
		# votes (note: in the event of an unlikely tie Python will
		# select first entry in the dictionary)
		name = max(counts, key=counts.get)
	
	# update the list of names
	names.append(name)

# loop over the recognized faces
for ((top, right, bottom, left), name) in zip(boxes, names):

	if name == 'Unknown' :
		# 가우시안블러
		sub_face1 = image[top:bottom, left:right] #가우시안블러 얼굴범위지정
		sub_face1 = cv2.GaussianBlur(sub_face1,(23, 23), 30) #가우시안 블러 처리
		image_gaussian = image #원본파일복사
		image_gaussian[top:top+sub_face1.shape[0], left:left+sub_face1.shape[1]] = sub_face1 #가우시안블러처리부분 합치기
		
cv2.imwrite('/Users/bakseo3060/Desktop/nepp_git/input/Autoblur_gaussian.jpeg', image_gaussian)


for ((top, right, bottom, left), name) in zip(boxes, names):

	if name == 'Unknown' :
		# 모자이크
		sub_face2 = image[top:bottom, left:right] #모자이크블러 얼굴범위 지정
		sub_face2 = cv2.resize(sub_face2, None, fx=0.09, fy=0.09,  interpolation=cv2.INTER_AREA) # 얼굴범위 축소
		sub_face2 = cv2.resize(sub_face2, dsize=(bottom-top, right-left), interpolation=cv2.INTER_AREA) # 다시 확대
		image_mosaic = image #원본파일복사
		image_mosaic[top:bottom, left:right] = sub_face2 # 모자이크블러처리부분 합치기

cv2.imwrite('/Users/bakseo3060/Desktop/nepp_git/input/Autoblur_mosaic.jpeg', image_mosaic)
print("FINISH")
cv2.waitKey(0)