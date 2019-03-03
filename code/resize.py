import cv2
import numpy
import matplotlib.pyplot as plt

def resize_portfolio(filename, new_filename):
    image = cv2.imread(filename)
    image_portfolio = cv2.resize(image, (image.shape[1], int(image.shape[1]*(720/909))))
    cv2.imwrite(new_filename, image_portfolio)
    return image_portfolio
    