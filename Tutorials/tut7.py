import cv2 as cv
import numpy as np

img = cv.resize(cv.imread('soccer_practice.jpg',0), (0,0), fx=0.6, fy=0.6)
template=cv.resize(cv.imread('shoe.png',0),(0,0), fx=0.6,fy=0.6)


h,w=template.shape #this is tuple

methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

#trying all 6
for method in methods:
    img2=img.copy()

    result=cv.matchTemplate(img2, template, method) #this output array tells how close template is to which region
    min_val, max_val, min_loc, max_loc=cv.minMaxLoc(result)
    print(min_loc, max_loc)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right=(location[0] + w, location[1] + h) #logical
    cv.rectangle(img2, location, bottom_right, 255, 5)
    cv.imshow('Match', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()