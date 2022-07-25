import os
import cv2


def get_path_file(id,images_path = "data/images"):
    return os.path.join(images_path, id+".jpg")


def clean_categ(categ_tree):
    categ_tree = categ_tree.replace('["','')
    categ_tree = categ_tree.replace('"]','')
    return categ_tree


def get_subcateg(categ_tree, deepness = None):
    if deepness is None:
        subcateg = categ_tree.split(' >> ')
    else : 
        try:
            subcateg = categ_tree.split(' >> ')[deepness]
        except(IndexError):
            print('lala')
            subcateg = None
    return subcateg


def get_img_list(list_path, new_shape=(224,224)):
    my_image_list = [cv2.imread(path) for path in list_path]
    my_image_list = [cv2.resize(image, new_shape, interpolation = cv2.INTER_AREA) for image in my_image_list]
    return my_image_list



import re
import unicodedata
def preprocess_text(sentence):
    sentence = unicodedata.normalize("NFKD",sentence)
    # # Remove punctuations and numbers
    # sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)
    # # sentence.encode('latin-1')
    return sentence