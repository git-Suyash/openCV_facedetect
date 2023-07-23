import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def start_detection():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Error", "Camera not accessible.")
        return

    # Create a function to update the video stream in the Tkinter label.
    def update_frame():
        ret, frame = cap.read()

        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            img_tk = ImageTk.PhotoImage(image=img)
            label.img_tk = img_tk
            label.config(image=img_tk)

        # Schedule the next update after 10 milliseconds.
        label.after(10, update_frame)

    # Start the update_frame loop.
    update_frame()

    # Release the VideoCapture and close the window when 'q' is pressed or the window is closed.
    def close_window():
        cap.release()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", close_window)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Face Detection")

    label = tk.Label(root)
    label.pack()

    button = tk.Button(root, text="Start Detect", command=start_detection)
    button.pack()

    root.mainloop()
