from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import urls
import subprocess

def recognition(request):
    call = subprocess.Popen('source /Users/bakseo3060/Desktop/nepp_git/test/bin/activate' ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #downloadImg = subprocess.Popen('python /Users/bakseo3060/Desktop/nepp_git/exportgc.py', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output = subprocess.Popen('python /Users/bakseo3060/Desktop/nepp_git/face-recognition-opencv/camera.py --encodings /Users/bakseo3060/Desktop/nepp_git/face-recognition-opencv/encodings.pickle \
	--image /Users/bakseo3060/Desktop/nepp_git/face-recognition-opencv/examples/Capture.png',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = output.communicate()
    #txt로 바꿔서 올려여한다
    saveImg = subprocess.Popen('python /Users/bakseo3060/Desktop/nepp_git/importgc.py', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return HttpResponse(stdoutdata)