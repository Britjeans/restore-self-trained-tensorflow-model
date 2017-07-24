import cv2
import numpy as np
scale_size=[227,227]

def readimg(path):
    img1_x = cv2.imread(path + '/x/1_x.jpg', 0)
    img1_x = cv2.resize(img1_x, (scale_size[0], scale_size[0]))
    img1_x = img1_x.astype(np.float32)
    img2_x = cv2.imread(path + '/x/2_x.jpg', 0)
    img2_x = cv2.resize(img2_x, (scale_size[0], scale_size[0]))
    img2_x = img2_x.astype(np.float32)
    img3_x = cv2.imread(path + '/x/3_x.jpg', 0)
    img3_x = cv2.resize(img3_x, (scale_size[0], scale_size[0]))
    img3_x = img3_x.astype(np.float32)
    img4_x = cv2.imread(path + '/x/4_x.jpg', 0)
    img4_x = cv2.resize(img4_x, (scale_size[0], scale_size[0]))
    img4_x = img4_x.astype(np.float32)
    img5_x = cv2.imread(path + '/x/5_x.jpg', 0)
    img5_x = cv2.resize(img5_x, (scale_size[0], scale_size[0]))
    img5_x = img5_x.astype(np.float32)
    img6_x = cv2.imread(path + '/x/6_x.jpg', 0)
    img6_x = cv2.resize(img6_x, (scale_size[0], scale_size[0]))
    img6_x = img6_x.astype(np.float32)
    img7_x = cv2.imread(path + '/x/7_x.jpg', 0)
    img7_x = cv2.resize(img7_x, (scale_size[0], scale_size[0]))
    img7_x = img7_x.astype(np.float32)
    img8_x = cv2.imread(path + '/x/8_x.jpg', 0)
    img8_x = cv2.resize(img8_x, (scale_size[0], scale_size[0]))
    img8_x = img8_x.astype(np.float32)
    img9_x = cv2.imread(path + '/x/9_x.jpg', 0)
    img9_x = cv2.resize(img9_x, (scale_size[0], scale_size[0]))
    img9_x = img9_x.astype(np.float32)
    img10_x = cv2.imread(path + '/x/10_x.jpg', 0)
    img10_x = cv2.resize(img10_x, (scale_size[0], scale_size[0]))
    img10_x = img10_x.astype(np.float32)
    img1_y = cv2.imread(path + '/y/1_y.jpg', 0)
    img1_y = cv2.resize(img1_y, (scale_size[0], scale_size[0]))
    img1_y = img1_y.astype(np.float32)
    img2_y = cv2.imread(path + '/y/2_y.jpg', 0)
    img2_y = cv2.resize(img2_y, (scale_size[0], scale_size[0]))
    img2_y = img2_y.astype(np.float32)
    img3_y = cv2.imread(path + '/y/3_y.jpg', 0)
    img3_y = cv2.resize(img3_y, (scale_size[0], scale_size[0]))
    img3_y = img3_y.astype(np.float32)
    img4_y = cv2.imread(path + '/y/4_y.jpg', 0)
    img4_y = cv2.resize(img4_y, (scale_size[0], scale_size[0]))
    img4_y = img4_y.astype(np.float32)
    img5_y = cv2.imread(path + '/y/5_y.jpg', 0)
    img5_y = cv2.resize(img5_y, (scale_size[0], scale_size[0]))
    img5_y = img5_y.astype(np.float32)
    img6_y = cv2.imread(path + '/y/6_y.jpg', 0)
    img6_y = cv2.resize(img6_y, (scale_size[0], scale_size[0]))
    img6_y = img6_y.astype(np.float32)
    img7_y = cv2.imread(path + '/y/7_y.jpg', 0)
    img7_y = cv2.resize(img7_y, (scale_size[0], scale_size[0]))
    img7_y = img7_y.astype(np.float32)
    img8_y = cv2.imread(path + '/y/8_y.jpg', 0)
    img8_y = cv2.resize(img8_y, (scale_size[0], scale_size[0]))
    img8_y = img8_y.astype(np.float32)
    img9_y = cv2.imread(path + '/y/9_y.jpg', 0)
    img9_y = cv2.resize(img9_y, (scale_size[0], scale_size[0]))
    img9_y = img9_y.astype(np.float32)
    img10_y = cv2.imread(path + '/y/10_y.jpg', 0)
    img10_y = cv2.resize(img10_y, (scale_size[0], scale_size[0]))
    img10_y = img10_y.astype(np.float32)
    r = scale_size[0]
    c = scale_size[0]
    img = np.zeros((r, c, 20))

    for i in range(r):

        for j in range(c):
            img[i][j] = [img1_x[i][j]] + [img2_x[i][j]] + [img3_x[i][j]] + [img4_x[i][j]] + [img5_x[i][j]] + [
                img6_x[i][j]] + [img7_x[i][j]] + [img8_x[i][j]] + \
                        [img9_x[i][j]] + [img10_x[i][j]] + [img1_y[i][j]] + [img2_y[i][j]] + [img3_y[i][j]] + [
                            img4_y[i][j]] + [img5_y[i][j]] + [img6_y[i][j]] + \
                        [img7_y[i][j]] + [img8_y[i][j]] + [img9_y[i][j]] + [img10_y[i][j]]
    return img

