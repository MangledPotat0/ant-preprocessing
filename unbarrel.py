import argparse as arg
import numpy as np
import cv2 as cv
import glob
import json
import os
import sys

ap = arg.ArgumentParser()
ap.add_argument('-v', '--video', required = True,
                help = 'Video files')
ap.add_argument('-px', '--pixel', required = True,
                help = 'Pixel resolution')
ap.add_argument('-f', '--framerate', required = True,
                help = 'framerate')
args = vars(ap.parse_args())
filenames = args['video']
filenames = glob.glob(filenames)

with np.load('calibration_parameters_{}px.npz'.format(args['pixel'])) as values:
    for fname in filenames:
        filename = os.path.splitext(fname)[0]
        vidfile = cv.VideoCapture('{}.mp4'.format(filename))
        readable, frame = vidfile.read()
        mtx = values['mtx']
        dist = values['dist']
        newcameramtx = values['newcameramtx']
        roi = values['roi']
        x1, y1, x2, y2 = roi

        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        api = cv.CAP_ANY
        out = cv.VideoWriter(filename = '{}corrected.mp4'.format(filename),
                             apiPreference = api,
                             fourcc = fourcc,
                             fps = int(args['framerate']),
                             frameSize = (x2, y2),
                             isColor = True)
        
        while readable:
            dst = cv.undistort(frame, mtx, dist, None, newcameramtx)
            dst = dst[y1:y1+y2, x1:x1+x2]
            out.write(dst)
            readable, frame = vidfile.read()

    vidfile.release()
    out.release()
    cv.destroyAllWindows()
sys.exit(0)

# EOF
