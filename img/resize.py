import cv2
import matplotlib.pyplot as plt


def resize_portfolio(img_file, save_name):
    raw = cv2.imread(img_file)
    new = cv2.resize(raw, (int(raw.shape[0] * (900 / 712)), raw.shape[0]))
    plt.imshow(new)
    cv2.imwrite(save_name, new)


def resize_newsetter(img_file, save_name):
    raw = cv2.imread(img_file)
    new = cv2.resize(raw, (int(raw.shape[0] * (1080 / 720)), raw.shape[0]))
    plt.imshow(new)
    cv2.imwrite(save_name, new)


def png_to_jpg(img_file):
    raw = cv2.imread(img_file)
    cv2.imwrite(img_file[:-3] + 'jpg', raw)


# resize_newsetter("summer_newsletter.jpg", "summer_newsletter_resized.jpg")
resize_portfolio("gramBarcodes.JPG", "gramBarcodes_portfolio.jpg")
# png_to_jpg("ARD.png")
