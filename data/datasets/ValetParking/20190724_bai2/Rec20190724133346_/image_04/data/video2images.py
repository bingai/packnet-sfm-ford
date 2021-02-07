# change the video into images in the format of 0000000000, 0000000001, 0000012345

import cv2
import os

# os.remove(images) for images in os.listdir('./') if images.endswith('.png')
# image_path = './'
image_path = os.path.abspath("./")
image_lists = [ f for f in os.listdir(image_path) if f.endswith(".png") ]
for image in image_lists:
    os.remove(os.path.join(image_path, image))

sample_rate = 200
# Opens the Video file
videofile = './ValetParking_RearCamera.avi'
cap = cv2.VideoCapture(videofile)
i=0
counter = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i % sample_rate == 0:
        # cv2.imwrite('./ValetParking_Images/{0:04}'+str(i)+'.png',frame)
        # cv2.imwrite('./'+'{0:010}'.format(counter)+'.png',frame)
        cv2.imwrite('{0:010}'.format(counter)+'.png', frame)

        counter += 1

    i+=1
    # print('image {0:04}'.format(i))

cap.release()
cv2.destroyAllWindows()