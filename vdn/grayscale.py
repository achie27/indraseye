import numpy as np
import cv2
import os, sys

def gray(file, file1):
	cap = cv2.VideoCapture(file)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter(file1,fourcc, 20.0, (256,144))
	while(True):
		ret, frame = cap.read()
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		out.write(grey)
	out.release()
	cap.release()

if(__name__=="__main__"):
	while(len(sys.argv)):
		gray(sys.argv[0],sys.argv[0])
		sys.argv = sys.argv[1:]

