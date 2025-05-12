import os
import sys
import tomllib

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer

media_path = None


def handle_error(error):
    print(f"Error occurred: {error}")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnBottomHint | Qt.WindowType.FramelessWindowHint)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        video_widget = QVideoWidget()
        layout.addWidget(video_widget)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setVideoOutput(video_widget)

        self.audio_output.setVolume(50)

        self.player.errorOccurred.connect(handle_error)

    def play_video(self):
        if media_path:
            qurl = QUrl.fromLocalFile(str(media_path))
            print(f"Playing media from {qurl.toString()}")
            self.player.setSource(qurl)
            self.player.play()


def load_config_toml():
    home_dir = os.path.expanduser("~")
    save_file = ".deskpop.toml"
    path = os.path.join(home_dir, save_file)

    if not os.path.exists(path):
        print(f"Config file {save_file} not found in home directory.")
        exit(1)

    with open(path, "rb") as f:
        data = tomllib.load(f)

        if "media_path" in data:
            global media_path
            media_path = str(data["media_path"])
        else:
            print("No 'media_path' found in config file.")
            exit(1)

if __name__ == "__main__":
    if os.name == "posix":
        os.environ["QT_QPA_PLATFORM"] = "xcb"

    load_config_toml()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    QTimer.singleShot(100, window.play_video)

    sys.exit(app.exec())
