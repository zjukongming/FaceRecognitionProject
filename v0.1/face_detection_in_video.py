#coding=utf-8

import cv2
import face_recognition
from PIL import Image


# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

FaceDir = "./FaceImg/"


# Open the input movie file
input_movie = cv2.VideoCapture("./TestVideoes/jzss.mp4")#打开
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))#获取该视频的帧数，强制转换为整数，舍弃小数部分
fps = input_movie.get(cv2.CAP_PROP_FPS)
size = (int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH)),   
        int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print size

print(length)
# Create an output movie file (make sure resolution/frame rate matches input video!)
fourcc = cv2.VideoWriter_fourcc(*'XVID')#需要确保自己的播放器有MPEG-4解码器，否则输出视频无法播放，个人感觉应该没有'*',但是face_recognition的github上有
output_movie = cv2.VideoWriter('one_output.avi', fourcc, fps, (size[0], size[1]))#四个参数分别为 输出视频名称 4位cc码 fps 尺寸px

# Load some sample pictures and learn how to recognize them.
#faces = face_recognition.load_image_file("./TestVideoes/two_faces.png")#face_recognition函数，加载用于识别的人脸图片
#lmm_face_encoding = face_recognition.face_encodings(lmm_image)[0]
#！获得该图片中的人脸的编码，人脸有多张，故应返回一个列表
#faces_encodings[:] = face_recognition.face_encodings(faces)#将encodings值拷贝到新数组
img_path_seq    = 1
img_path_tail_1 = ".jpeg"
img_path_tail_2 = ".png" 
img_number      = 2;


#for i in range(1,img_number):
#    img_path    = "%d%s"%(image_seq,image_path_tail_1)
#    img         = Image.open(image_path)  
    

#al_image = face_recognition.load_image_file("alex-lacamoire.png")
#al_face_encoding = face_recognition.face_encodings(al_image)[0]

'''
known_faces = [
    lmm_face_encoding,
    al_face_encoding
]
'''
# Loading Face Images

print("Loading face Images...")
known_faces = []
name_file = open("face_lib.txt","r")
for line in name_file.readlines():
    i = 0
    face_img_file = FaceDir+line
    face_img_file=face_img_file.replace('\n','')
    print(face_img_file)
    face = face_recognition.load_image_file(face_img_file)
    face_encode = face_recognition.face_encodings(face)[0]
    known_faces.append(face_encode)
    i+=1

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
print("Done.")


while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1
    
    #if frame_number%50!=0: continue
    #if frame_number>1000: break
    # Quit when the input video file ends
    if not ret:
        break

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(frame)

    # Label the results
    for (top, right, bottom, left) in face_locations:
        print("Got somebody...")
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

# All done!
input_movie.release()
cv2.destroyAllWindows()

