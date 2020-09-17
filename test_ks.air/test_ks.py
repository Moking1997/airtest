# -*- encoding=utf8 -*-
__author__ = "to"

from airtest.core.api import *

# auto_setup(__file__)
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
from airtest.cli.parser import cli_setup
from airtest.core.android.adb import *
from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class startAutoClick:
    def __init__(self):
        print("自动化操作开始...")
        self._main()
    # 点赞

    def _main(self):
        keyevent("HOME")
        stop_app("com.smile.gifmaker")
        start_app("com.smile.gifmaker")
        sleep(6.0)
        while(poco(name="com.smile.gifmaker:id/editor").exists() == False):
            poco(name="com.smile.gifmaker:id/right_btn").click()
        poco(name="com.smile.gifmaker:id/editor").set_text('风景')
        poco(name="com.smile.gifmaker:id/right_tv").click()
        poco(name="android.view.View")[2].click()
        clickUserPage = 0
        while(clickUserPage < 4):
            # self.clickUsers()
            poco.swipe([0.5, 0.92], [0.5, 0.2], duration=(1))
            clickUserPage += 1

    # 点击用户头像
    def clickUsers(self):
        items = poco(name="com.smile.gifmaker:id/avatar")
        for item in items:
            x, y = item.get_position()
            if y > 0.2 and y < 0.9:
                item.click()
                self.startVideo()
                keyevent("BACK")
    # 点击作品
    def clickVideos(self):
        items = poco(name="com.smile.gifmaker:id/player_cover")
        for item in items:
            x, y = item.get_position()
            if y > 0.2 and y < 0.9:
                item.click()
                self.startLink()
                keyevent("BACK")

    def startVideo(self):
        isHaveMoreVideo = False
        while(isHaveMoreVideo == False):
            poco.swipe([0.5, 0.9], [0.5, 0.2], duration=(1))
            self.clickVideos()
            isHaveMoreVideo = poco(text="没有更多作品了").exists()
    # 开始点赞
    def clickLinks(self):
        items = poco(name="com.smile.gifmaker:id/like_button")
        for item in items:
            x, y = item.get_position()
            if y > 0.3 and y < 0.9:
                item.click()

    def startLink(self):
        isHaveMoreComment = False
        while(isHaveMoreComment == False):
            poco.swipe([0.5, 0.8], [0.5, 0.2], duration=(1))
            self.clickLinks()
            isHaveMoreComment = poco(text="没有更多评论").exists()
photo = startAutoClick()
log("Test OK")

sleep(2)
stop_app(name="com.smile.gifmaker:id/avatar")
# script content

