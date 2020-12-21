# python3

import cv2

link = '/home/taimur/Documents/Online Courses/Fourth Brain/Week 8/Coding Assignments/train_temp/separated_pics_green'
select_channel = input('enter channel')
select_channel = int(select_channel)

folder = os.path.join(link, 'diabetic retinopathy')

def img_to_np(img_path):
    im_temp = cv2.imread(img_path, 1)
    return im_temp

for i in os.listdir(folder):
    image_np = img_to_np(os.path.join(folder, i))
