# ant-preprocessing
Running calibrate.py on a calibration footage (of a chessboard pattern) will generate a .npz file containing the appropriate barrel distortion correction parameter. Run unbarrel.py with this config file and the target data file as argument following appropriate flags and it will perform the correction and spit out a new file named (FILENAME)corrected.mp4. \

Example: \
python unbarrel.py -f 10 -px 10 -v samplevid.mp4

launches the script using 'calibration_parameters_10px.npz' and sets the output video at 10 frames per second.
