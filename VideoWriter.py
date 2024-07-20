from cv2 import VideoWriter as VW, VideoWriter_fourcc
from os import mkdir, getcwd
from os.path import join
from time import time


class VideoWriter:
    def __init__(self, fps, frameSize):
        self.fps = fps
        self.frameSize = frameSize

        self.recording_path = join(getcwd(), "recordings")
        self.create_recording_directory()

        self.video = None

    def create_recording_directory(self):
        try:
            mkdir(self.recording_path)
        except FileExistsError:
            pass

    def write(self, frame):
        if self.video is None:
            self.video = VW(
                join(self.recording_path, f"recording-{int(time())}.avi"),
                VideoWriter_fourcc(*"XVID"),
                self.fps,
                self.frameSize,
            )

        self.video.write(frame)

    def release(self):
        if self.video is not None:
            self.video.release()

        self.video = None
