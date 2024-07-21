from ScreenCapturer import ScreenCapturer
from VideoWriter import VideoWriter
from time import time
from GUI import GUI


class App:
    def __init__(self, fps=30):
        self.fps = fps

        self.is_recording = False

        self.recording_duration = 0
        self.latest_duration_update = 0
        self.recording_timer = None

        self.sc = ScreenCapturer(fps)
        self.vw = VideoWriter(self.fps, self.sc.get_resolution())

        self.gui = GUI(self.toggle_recording)
        self.gui.mainloop()

    def record(self):
        while self.is_recording:
            frame = self.sc.capture_frame()
            self.vw.write(frame)

            self.update_duration()
            self.gui.window.update_idletasks()
            self.gui.window.update()

    def start_recording(self):
        self.is_recording = True
        self.latest_frame_at = time()

        self.update_duration(0)
        self.record()

    def stop_recording(self):
        self.is_recording = False
        self.latest_frame_at = 0
        self.vw.release()

    def toggle_recording(self):
        if self.is_recording:
            self.stop_recording()
        else:
            self.start_recording()

    def get_current_duration(self):
        hours = self.recording_duration // 3600
        minutes = (self.recording_duration % 3600) // 60
        seconds = self.recording_duration % 60

        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def update_duration(self, duration=None):
        if duration is not None:
            self.recording_duration = duration
            self.latest_duration_update = time()

            self.gui.update_duration(self.get_current_duration())
        elif time() - self.latest_duration_update >= 1:
            self.recording_duration = self.recording_duration + 1
            self.latest_duration_update = time()

            self.gui.update_duration(self.get_current_duration())

    def __del__(self):
        self.stop_recording()


if __name__ == "__main__":
    app = App()
