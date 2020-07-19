#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = laudai
"""
from gtts import gTTS
import os
import sys

# 透過參數，寫入要說的中文字
theword = sys.argv[1]
filetype = ".mp3"
# 將檔名透過參數寫入
fileprefix = sys.argv[2]
filename = fileprefix + filetype

tts = gTTS(text=theword, lang="zh-TW")
tts.save(filename)

# convert mp3 to wav
# force override output event file is exist
os.system("ffmpeg -i {} -y {}.wav".format(filename, fileprefix))
