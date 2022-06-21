import argparse
import numpy as np
import cv2 as cv
import glob
import json

ap = argparse.ArgumentParser()
ap.add_argument('-h', '--height', dtype=int,
                help='Height of chessboard')
ap.add_argument('-w', '--width', dtype=int,
                help='Width of chessboard')
ap.add_argument('-v', '--video', dtype=str,
                help='Chessboard video file')

args = vars(ap.parse_args())
h = args['height']
w = args['width']
vfile = args['video']

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((h*w,3), np.float32)
objp[:,:2] = np.mgrid[0:w,0:h].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

vid = cv.VideoCapture(vfile)
run, img = vid.read()
newimg = img
loops = 0
ct = 0

while run:
    loops += 1
    img = newimg
    ct = 0
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite('gray.png', gray)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (w,h), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (3,3), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        #cv.drawChessboardCorners(img, (w,h), corners2, ret)
        #cv.imwrite('img.png', img)
    while ct < 30:
        ct += 1
        run, newimg = vid.read()

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints,
                                            gray.shape[::-1], None, None)
cv.destroyAllWindows()

ymax, xmax = img.shape[:2]
print('xmax: ',xmax)
print('ymax: ',ymax)
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (xmax,ymax), 1,
                                                 (xmax,ymax))

npzfile = np.savez('calibration_parameters.npz',
                   mtx = mtx, dist = dist,
                   newcameramtx = newcameramtx, roi = roi)

dst = cv.undistort(img, mtx, dist, None, newcameramtx)
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('calibresult.png',dst)

# EOF
