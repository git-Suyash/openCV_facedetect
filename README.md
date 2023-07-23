# Face Detection Project Documentation

## Overview

The Face Detection project is a Python application that utilizes OpenCV and Tkinter to access the camera in a device, detect faces in real-time video streams, and display the video with rectangles drawn around the detected faces. The project uses a pre-trained Haar Cascade classifier for face detection.

## Requirements

- Python 3.x
- OpenCV (opencv-python)
- Tkinter
- Pillow (PIL)

Install the required libraries using the following command:

```bash
pip install opencv-python tkinter pillow
```

## How to Use

1. Clone the repository or download the `face_detection.py` file.

2. Run the `face_detection.py` script using the following command:

```bash
python face_detection.py
```

3. A Tkinter window will open with a "Start Detect" button.

4. Click the "Start Detect" button to begin the face detection process.

5. The camera will access the default camera in your device and display the live video stream.

6. Detected faces will be highlighted with rectangles drawn around them.

7. Press 'q' or close the Tkinter window to stop the face detection process and exit the program.

## Implementation Details

### Libraries Used

- `cv2`: OpenCV library for computer vision tasks.
- `tkinter`: Tkinter library for creating the GUI.
- `PIL.ImageTk`: Module from the Pillow library for image conversion between OpenCV and Tkinter.

### Functions

#### `start_detection()`

This function is called when the "Start Detect" button is clicked. It performs the following steps:

1. Loads the pre-trained Haar Cascade classifier for face detection using `cv2.CascadeClassifier`.
2. Accesses the default camera using `cv2.VideoCapture`.
3. Creates a nested function `update_frame()` to continuously capture frames, detect faces, and update the video stream displayed in the Tkinter label.
4. Converts the frame to grayscale for face detection using `cv2.cvtColor`.
5. Detects faces in the grayscale frame using `face_cascade.detectMultiScale`.
6. Draws rectangles around the detected faces using `cv2.rectangle`.
7. Converts the frame to RGB format for displaying in Tkinter using `PIL.Image.fromarray` and `PIL.ImageTk.PhotoImage`.
8. Schedules the next update after 10 milliseconds using `label.after(10, update_frame)`.
9. Releases the VideoCapture and closes the Tkinter window when 'q' is pressed or the window is closed.

### GUI Elements

- Tkinter window: The main window for the application.
- Label: Displays the live video stream with detected faces.
- Start Detect Button: Triggers the face detection process when clicked.

## Acknowledgments

- The face detection functionality is implemented using a pre-trained Haar Cascade classifier provided by OpenCV.

## Troubleshooting

- If the camera is not accessible, ensure that your device has a working camera and check camera permissions.

- If you encounter any errors or have issues with the application, feel free to contact the project maintainer.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or questions regarding the project, you can reach out to:

- Project Maintainer: SUYASH
- Email: svtsuyash@gmail.com

---
