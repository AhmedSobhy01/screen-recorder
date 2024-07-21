from tkinter import Tk, Button, Label, StringVar


class GUI:
    def __init__(self, on_toggle_record):
        self.on_toggle_record = on_toggle_record
        self.recording_state = False

        self.window = Tk()
        self.window.title("Screen Recorder")
        self.window.geometry("300x200")
        self.window.resizable(False, False)

        self.start_stop_button = Button(
            self.window, text="Start Recording", command=self.toggle_recording
        )
        self.start_stop_button.pack()

        self.state_label = Label(self.window, text="Not Recording")
        self.state_label.pack()

        self.duration_label_var = StringVar()
        self.duration_label_var.set("00:00:00")
        self.duration_label = Label(self.window, textvariable=self.duration_label_var)
        self.duration_label.pack()

    def mainloop(self):
        self.window.mainloop()

    def update_duration(self, duration):
        if duration != self.recording_duration:
            self.duration_label_var.set(duration)

    def start_recording(self):
        self.recording_duration = 0
        self.recording_state = True

        self.start_stop_button.config(text="Stop Recording")
        self.state_label.config(text="Recording")

    def stop_recording(self):
        self.recording_state = False

        self.start_stop_button.config(text="Start Recording")
        self.state_label.config(text="Not Recording")

    def toggle_recording(self):
        if self.recording_state:
            self.stop_recording()
        else:
            self.start_recording()

        self.on_toggle_record()
