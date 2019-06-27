# encode/views.py

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import urls
import subprocess
import time

def encode(request):
    call = subprocess.Popen('source /Users/bakseo3060/Desktop/nepp/nepp_django/test/bin/activate' ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    downloadImg = subprocess.Popen('python /Users/bakseo3060/Desktop/nepp/nepp_django/encodegc.py', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    time.sleep(20)
    output = subprocess.Popen('python /Users/bakseo3060/Desktop/nepp/nepp_django/face-recognition-opencv/encode_faces.py --dataset /Users/bakseo3060/Desktop/nepp/nepp_django/face-recognition-opencv/dataset --encodings /Users/bakseo3060/Desktop/nepp/nepp_django/face-recognition-opencv/encodings.pickle' ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = output.communicate()
    return HttpResponse(stdoutdata)