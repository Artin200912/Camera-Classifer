import cv2 as cv

# Define a class named Camera to encapsulate the functionality related to a camera
class Camera:

    # The constructor method initializes the camera object
    def __init__(self):
        # Attempt to open the default camera (camera index 0)
        self.camera = cv.VideoCapture(0)
        # Check if the camera was successfully opened
        if not self.camera.isOpened():
            # If not, raise an error indicating that the camera could not be opened
            raise ValueError("Unable to open camera!")

        # Retrieve and store the width and height of the camera's frames
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    # The destructor method is called when the object is about to be destroyed
    def __del__(self):
        # Check if the camera is still open
        if self.camera.isOpened():
            # If so, release the camera to free up resources
            self.camera.release()

    # Method to get a single frame from the camera
    def get_frame(self):
        # Check if the camera is open
        if self.camera.isOpened():
            # Attempt to read a frame from the camera
            ret, frame = self.camera.read()

            # Check if the frame was successfully read
            if ret:
                # If so, convert the frame from BGR to RGB color space and return it
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                # If not, return the failure status and None for the frame
                return (ret, None)
        else:
            # If the camera is not open, return None
            return None