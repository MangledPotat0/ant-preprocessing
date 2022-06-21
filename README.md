# Documentation

## Calibration parameter generation

The bulk of this code is taken directly from OpenCV's usage example.

1. Using the 1cm x 1cm chessboard grid, take a sample shot and count how many pixels are in each square to obtain the image resolution in px/mm.
2. Make a new sample clip of the chessboard moving around. Try to cover as much of the FoV as possible for best result.
3. Run `calibrate.py` with the chessboard height and width (flags `-h` and `-w`) and the input video file name (flag `-v`). Example:

``` python calibrate.py -h 7 -w 7 -v debarrel.mp4 ```

Note that the height and width is determined by the number of INTERSECTION POINTS along each axis and not by number of squares.

5. Run `python calibrate.py` to generate calibration parameter file.

## Barrel distortion correction

The bulk of this code is taken directly from OpenCV's usage example. Simple run:

```python unbarrel.py -f 10 -px 10 -v samplevid.mp4```

The argument flags are

`-f`  : fps \
`-px` : image resolution in px/mm \
`-v`  : video file name

for example the above line will launch the script using 'calibration_parameters_10px.npz' and sets the output video at 10 frames per second. The -v flag can also take more than one video file. For this the filenames can be entered with spaces in between, or using wildcard to pattern match a bulk of files (e.g. -v \*.mp4 will run the unbarrel procedure on every .mp4 in the directory).

## Cropping

`cropper.py` is just there to trim the clips with a graphic update to keep track of how things look. The GUI usage was copied from pyimagesearch's tutorial for a similar work. 
1. Run the code with flags `-v` for video filename (without the extension) and `-f` for framerate.
2. Once started it opens the first frame of the video on a separate window (i.e. this code cannot be used on a headless setup).
3. Press any key with the image view on top.
4. Now the terminal should prompt you to enter left crop value. Enter any number as desired, and the change should be reflected immediately on the image window.
5. switch over to the image window and press any key to proceed. Repeat until desired crop is achieved.
6. Enter 0 as crop value when you are satisfied with the side you are working with. The order of crop is left-right-top-bottom.
7. After all four sides are completed, the script will sift through the whole video, crop and save to a new video file.
