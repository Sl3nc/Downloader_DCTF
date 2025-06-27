from win32api import GetSystemMetrics, EnumDisplaySettings, ChangeDisplaySettings
from pygetwindow import getWindowsWithTitle
from time import sleep

class Screen:
    width = 1366
    height = 768
    deft = 32
    was_changed = False

    def __init__(self):
        self.x =  GetSystemMetrics(0)
        self.y = GetSystemMetrics(1)
        pass

    def reposite(self, title: str):
        browser = getWindowsWithTitle(title)[0]
        window_x = browser.left + 8

        if self.x <= window_x : 
            browser.moveTo(-8, -8)
            sleep(1)

        if self.x != self.width : 
            mode = EnumDisplaySettings()
            mode.PelsWidth = self.width
            mode.PelsHeight = self.height
            mode.BitsPerPel = self.deft
            self.was_changed = True

            ChangeDisplaySettings(mode, 0)
            sleep(3)

        if browser.isMaximized == False: browser.maximize()

    def reset(self):
        if self.was_changed:
            mode = EnumDisplaySettings()
            mode.PelsWidth = self.x
            mode.PelsHeight = self.y
            mode.BitsPerPel = self.deft
            ChangeDisplaySettings(mode, 0)
