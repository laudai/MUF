#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "laudai"
__version__ = "0.1.0"

import speech_recognition as sr
from muf import getTime

# initialize the Recognizer as r
r = sr.Recognizer()


def use_mic():
    """
    return SpeechRecognition Microphone instances
    """
    print("All Microphone in this device:\n{}\n".format(
        sr.Microphone.list_microphone_names()))
    print("Initialize the microphone\n")
    mic = sr.Microphone()
    return mic


def getMicrophoneAudio(Microphone):
    try:
        print("Watting get microphone voice to Speech_Recognition AudioData\n")
        with Microphone as source:
            # 會抓音檔的前0.5秒做音訊的校正
            r.adjust_for_ambient_noise(source, duration=0.5)
            AudioData = r.listen(source)
    except(OSError, IOError, WindowsError) as Enverr:
        print("Something is wrrong , will retry again , Ctrl + C to interrupt\n")
        print("="*50)
        print("Maybe OSError , IOError , WindowsError\nError message is :\n")
        print(Enverr)
    except Exception as e:
        print(e.message, e.args)
    return AudioData


def recognize_speech(audio, language="zh-TW"):
    """language can use like :
    English (US) 	en
    Dutch 	nl
    French 	fr
    Japanese 	ja
    Korean 	ko
    """
    try:
        print("Now get the audio voice to google speech recognition\n")
        # timestamp + the recongited speech
        text = "{} {}\n".format(getTime.getNTP_Server_Time(
        ), r.recognize_google(audio, language=language))
        print(text)
    except sr.RequestError:
        print("{}\n\t無法與伺服器連線，將確認連線，並將重新抓音檔\n{}\n".format("="*50, "="*50))
    except sr.UnknownValueError:
        # speech was unintelligible
        # raise sr.UnknownValueError
        print("{}\n\t無法辨識，將重新抓音檔\n{}\n".format("="*50, "="*50))


def main():
    message1 = "Use Ctrl + C twice to terminate the MUF!!"
    message2 = "Your UTC TimeZone is {}".format(getTime.getUTC_Timezone())
    message3 = "Start at : {}".format(getTime.getNTP_Server_Time())
    message4 = "Default recognition language is 'zh-TW'"
    print("{}\n\t{}\n\t{}\n\t{}\n\t{}\n{}".format(
        "="*50, message1, message2, message3, message4, "="*50))
    mic = use_mic()
    while True:
        try:
            AudioData = getMicrophoneAudio(mic)
            recognize_speech(AudioData)
        except (EOFError, KeyboardInterrupt):
            message1 = "User shutdown the MUF !!"
            message2 = "End at : {}".format(getTime.getNTP_Server_Time())
            print("{}\n\t{}\n\t{}\n{}\n".format(
                "="*50, message1, message2, "="*50))
            break
