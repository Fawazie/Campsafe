import numpy as np
import cv2
import imutils
import datetime

# Load the Haar cascade classifier for detecting guns
gun_cascade = cv2.CascadeClassifier("cascadee.xml")

# Open the video file for capturing frames
camera = cv2.VideoCapture(0)

# Initialize a variable to track whether a gun is detected
gun_exist = False

# Loop through the video frames
while True:
    # Read the next frame from the video
    ret, frame = camera.read()

    # If there are no more frames, break out of the loop
    if frame is None:
        break

    # Resize the frame to a smaller width to speed up processing
    frame = imutils.resize(frame, width=600)

    # Convert the frame to grayscale for Haar cascade detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the grayscale frame using the Haar cascade classifier
    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    # Loop through each detected gun
    for x, y, w, h in guns:
        # Draw a rectangle around the detected gun
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract the region of interest (ROI) for the gun
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]

        # Set the flag to True if a gun is detected
        gun_exist = True

    # Add a timestamp to the frame
    cv2.putText(
        frame,
        datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
        (10, frame.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.35,
        (0, 0, 255),
        1,
    )

    # Display the frame with detected guns
    cv2.imshow("Security Feed", frame)

    # Wait for a key press; if 'q' is pressed, break out of the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Print the final value of gun_exist (True if a gun was detected, False otherwise)
print(gun_exist)

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
