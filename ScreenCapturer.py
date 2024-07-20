import dxcam


class ScreenCapturer:
    def __init__(self, fps):
        self.camera = dxcam.create(output_color="BGR")
        self.camera.start(target_fps=fps, video_mode=True)

        self.resolution = tuple(
            [
                int(i)
                for i in dxcam.output_info().split("(")[-1].split(")")[0].split(", ")
            ]
        )

    def capture_frame(self):
        return self.camera.get_latest_frame()

    def get_resolution(self):
        return self.resolution
