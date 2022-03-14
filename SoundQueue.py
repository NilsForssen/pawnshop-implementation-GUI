import playsound
from threading import Thread


class SoundQueue(Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.fileList = []

    def addSound(self, mp3path):
        self.fileList.append(mp3path)
        if not self.is_alive():
            self.start()

    def run(self):
        for file in self.fileList:
            try:
                playsound.playsound(file, True)
            except playsound.PlaysoundException:
                print("Cannot play sound right now!")


if __name__ == "__main__":
    first = SoundQueue()

    for i in range(10):
        first.addSound("sound/pawn.mp3")
    first.join()
