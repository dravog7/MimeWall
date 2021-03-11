import pyautogui
from queue import Queue,Full
import threading

class Mouse(threading.Thread):
    width: int
    height: int
    landmarks: Queue

    def __init__(self):
        super().__init__()
        self.width,self.height = pyautogui.size()
        self.landmarks = Queue(maxsize=1)
    
    def convert(self, landmark):
        return self.width * getattr(landmark,"x",0) , self.height * getattr(landmark,"y",0)

    def _moveTo(self, landmark, time=0.0):
        x,y = self.convert(landmark)
        pyautogui.moveTo(x,y,time)

    def moveTo(self, landmark):
        try:
            self.landmarks.put_nowait(landmark)
        except Full:
            pass

    def run(self):
        while True:
            landmark = self.landmarks.get()
            self._moveTo(landmark)