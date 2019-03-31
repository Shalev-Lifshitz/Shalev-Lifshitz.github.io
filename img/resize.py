import cv2
import matplotlib.pyplot as plt

def resize(img_file, save_name):
    raw = cv2.imread(img_file)
    new = cv2.resize(raw, (int(raw.shape[0]*(900/712)), raw.shape[0]))
    plt.imshow(new)
    cv2.imwrite(save_name, new)
    
resize("sxsw_talk2.png", "sxsw_portfolio.png")