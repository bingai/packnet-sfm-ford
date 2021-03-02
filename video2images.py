# change the video into images in the format of 0000000000, 0000000001, 0000012345

import cv2
import os
import time

# os.remove(images) for images in os.listdir('./') if images.endswith('.png')
# image_path = './'
image_path = os.path.abspath("./")
image_lists = [ f for f in os.listdir(image_path) if f.endswith(".png") ]
for image in image_lists:
    os.remove(os.path.join(image_path, image))

sample_rate = 20
# Opens the Video file
videofile = './ValetParking_RearCamera.avi'
cap = cv2.VideoCapture(videofile)

counter = 0

frame_rate = 30
prev = 0

while(cap.isOpened()):
    time_elapsed = time.time() - prev
    ret, frame = cap.read()
    if ret == False:
        break
    # if i % sample_rate == 0:
    #     # cv2.imwrite('./ValetParking_Images/{0:04}'+str(i)+'.png',frame)
    #     # cv2.imwrite('./'+'{0:010}'.format(counter)+'.png',frame)
    #     cv2.imwrite('{0:010}'.format(counter)+'.png', frame)
    if time_elapsed > 1./frame_rate:
        prev = time.time()
        cv2.imwrite('{0:010}'.format(counter)+'.png', frame)
        counter += 1

    # i+=1
    # print('image {0:04}'.format(i))

cap.release()
cv2.destroyAllWindows()