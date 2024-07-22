<h1 align="center">🎥 Screen Recorder</h1>

![screenshot](https://github.com/user-attachments/assets/f0cf6798-844a-417a-ace6-f5a7821a0d84)

A simple screen recording tool built with Python and OpenCV (`cv2`). This recorder captures screenshots at a specified frame rate, includes a duration counter, and saves the output as an AVI file in a designated recording folder. The application features a graphical user interface (GUI) built with Tkinter.

## ✨ Features

-   📹 Records screen at a configurable frame rate
-   ⏲️ Duration counter
-   🎞️ Saves recordings in AVI format
-   📂 Outputs videos to a `recordings` folder in the current working directory

## 🔧 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AhmedSobhy01/screen-recorder.git

    cd screen-recorder
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

1. Run the screen recorder script:
   `python main.py`

2. Adjust the frame rate by modifying the constructor parameters in the `main.py` file.

3. The output video will be saved in the `recordings` folder within the current working directory, with a timestamped filename.

## ⚙️ Configuration

-   **Frame Rate:** Configure the number of screenshots per second by adjusting the parameter in the `main.py` constructor.

## 📜 Requirements

-   Python 3.x
-   OpenCV (`cv2`)
-   `dxcam` (version 0.0.5)

Ensure you have the required packages listed in `requirements.txt`.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
