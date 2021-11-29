import cv2
import numpy as np

# Function to generate color histogram
def color_hist(img, nbins) :
    Hist = []
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H = cv2.calcHist([img_hsv], [0], None, [nbins[0]], [0, 360])
    S = cv2.calcHist([img_hsv], [1], None, [nbins[1]], [0, 1])
    V = cv2.calcHist([img_hsv], [2], None, [nbins[2]], [0, 1])
    hist_temp = np.concatenate((H, S, V), axis = 0)
    for i in  hist_temp.tolist() :
        Hist.append(i[0])
    return Hist

# Global Color Histogram
def GCH (image1, image2, nbins):
    #image1_path ==> path for image1
    img1 = cv2.imread(image1, 1)
    hist_1 = color_hist(img1, nbins)
    #image2_path ==> path for image2
    img2 = cv2.imread(image2, 1)
    hist_2 = color_hist(img2, nbins)
    dist = 0
    for i in range(len(hist_1)):
        dist += abs((hist_1[i]**2)-(hist_2[i]**2))**(0.5)
    print(image1, image2, " : ", dist)

# Local Color Histogram
def LCH(image1, image2, nbins, ndiv) :
    #image1_path : Path of first image for comparison
    img1 = cv2.imread(image1, 1)
    #image2_path : Path of second image for comparison
    img2 = cv2.imread(image2, 1)
    (w1, h1, _)=img1.shape
    (w2, h2, _)=img1.shape
    m1, n1 = math.floor(w1/ndiv), math.floor(h1/ndiv)
    m2, n2 = math.floor(w2/ndiv), math.floor(h2/ndiv)
    m1_rest, n1_rest = w1 % ndiv, h1 % ndiv
    m2_rest, n2_rest = w2 % ndiv, h2 % ndiv
    img1_new = img1[:(w1 - m1_rest), :(h1 - n1_rest)]
    img2_new = img2[:(w2 - m2_rest), :(h2 - n2_rest)]
    img1_temp = np.split(img1_new, ndiv, 0)
    img2_temp = np.split(img2_new, ndiv, 0)
    img1_segs = []
    for i in img1_temp :
        img1_segs += np.split(i, ndiv, 1)
    img1_segs = np.array(img1_segs)
    img2_segs = []
    for i in img2_temp :
        img2_segs += np.split(i, ndiv, 1)
    img2_segs = np.array(img2_segs)
    dist_local = 0
    for i in xrange(len(img1_segs)) :
        hist1 = color_hist(img1_segs[i], nbins)
        hist2 = color_hist(img2_segs[i], nbins)
        dist = 0
        for j in xrange(len(hist1)):
            dist += abs((hist1[j]**2)-(hist2[j]**2))**(0.5)
        dist_local += dist
    print dist_local
"""
GCH('../images/apple1.jpg', '../images/apple2.jpg', [32, 32, 32])
GCH('../images/apple2.jpg', '../images/apple2.jpg', [32, 32, 32])
GCH('../images/apple3.jpg', '../images/apple2.jpg', [32, 32, 32])
GCH('../images/apple4.jpg', '../images/apple2.jpg', [32, 32, 32])
"""
