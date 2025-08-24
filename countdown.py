import time
import sys
from tqdm import tqdm
import os
import msvcrt
import pygame

class CountdownTimer:
    def __init__(self, minutes):
        self.seconds = int(minutes * 60)
        self.paused = False
        self.stopped = False
        self.pbar = None

    def pause(self):
        if not self.paused:
            self.paused = True
            self.pbar.write("Paused. Press 'c' to continue.")

    def continue_timer(self):
        if self.paused:
            self.paused = False
            self.pbar.write("Continuing...")

    def stop(self):
        self.stopped = True
        self.pbar.write("Stopping...")
        pygame.mixer.music.stop()
        sys.exit(0)

    def run(self):
        with tqdm(total=self.seconds, initial=self.seconds) as self.pbar:
            self.pbar.set_description("Countdown")
            while self.pbar.n > 0 and not self.stopped:
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'p':
                        self.pause()
                    elif key == 'c':
                        self.continue_timer()
                    elif key == 'x':
                        self.stop()

                if not self.paused:
                    self.pbar.update(-1)
                    time.sleep(1)
                else:
                    time.sleep(0.1)

        if not self.stopped:
            pygame.mixer.music.load('xylophone.mp3')
            pygame.mixer.music.play(loops=-1)
            self.pbar.write("Countdown finished. Press 'x' to stop the sound and exit.")
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'x':
                        self.stop()
                time.sleep(0.1)


def countdown(minutes):
    """
    Starts a countdown timer for the specified number of minutes.

    Args:
        minutes: The number of minutes to count down from.
    """
    timer = CountdownTimer(minutes)
    timer.run()

if __name__ == "__main__":
    pygame.init()
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(sys.argv) != 2:
        print("Usage: python countdown.py <minutes>")
        sys.exit(1)

    try:
        minutes = float(sys.argv[1])
        if minutes <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive number of minutes.")
        sys.exit(1)

    print("Press 'p' to pause, 'c' to continue, and 'x' to stop.")
    countdown(minutes)