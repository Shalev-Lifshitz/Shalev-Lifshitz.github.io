import cv2
import matplotlib.pyplot as plt

def resize_portfolio(img_file, save_name):
    raw = cv2.imread(img_file)
    new = cv2.resize(raw, (int(raw.shape[0]*(900/712)), raw.shape[0]))
    plt.imshow(new)
    cv2.imwrite(save_name, new)
    
def resize_newsetter(img_file, save_name):
    raw = cv2.imread(img_file)
    new = cv2.resize(raw, (int(raw.shape[0]*(1080/720)), raw.shape[0]))
    plt.imshow(new)
    cv2.imwrite(save_name, new)
    
resize_newsetter("sxsw_talk3.png", "sxsw_talk_newsletter.png")