import cv2
import numpy as np
import pandas as pd 
import os
import time

def generate_image_array(path_to_images,sample_frame):
    images = []
    counter = 1
    for image in sample_frame['Image Index']:

        print(counter ,image)
        images.append(image)
        counter += 1

    return np.array([np.array(cv2.resize(cv2.imread(path_to_images+img, cv2.IMREAD_GRAYSCALE),(512,512))) for img in images]) 

def dump_array(array_name, array_contents):
    return np.save(array_name,array_contents)

def process_labels(labels_frame):

    columns_to_drop = ["Follow-up #","Patient ID","Patient Age","Patient Gender","View Position","OriginalImageWidth","OriginalImageHeight",
                     "OriginalImagePixelSpacing_x","OriginalImagePixelSpacing_y"]

    columns = ["Follow-up #","Patient ID","Patient Age","Patient Gender","View Position","OriginalImage[Width,Height]","OriginalImagePixelSpacing[x,y]"]

    #for col in columns:
     #   del labels_frame[col]
    
    labels_frame['Finding Labels'] = labels_frame['Finding Labels'].apply(lambda x: x.split('|')[0])

    return labels_frame


if __name__ == '__main__':
    current_dir = os.getcwd()
    start = time.time()
    path_to_images = current_dir + '\data\images\\'

    image_frame = pd.read_csv(os.getcwd() + "\data\processed_labels.csv")
    #image_frame_1 = pd.read_csv(r'C:\Users\ishan\Study\CS 584\Project\full dataset\Data_Entry_2017.csv')
    image_array = generate_image_array(path_to_images,image_frame)
    dump_array("xray_images",image_array)
    #print("DONE PROCESSING IMAGES.")
    modified_frame = process_labels(image_frame)
    modified_frame.to_csv(current_dir+'\data\processed_labels_full.csv',index = False, header = True)
    finished = time.time()
    print("TIME TAKEN",finished - start)




