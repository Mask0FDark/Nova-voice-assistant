import config
import stt
import tts
import datetime
from num2words import num2words
import webbrowser
import random
from playsound import playsound
import pyowm 
#програма сделана Mask_0F_Darkness ❤️

def execute_cmd(cmd: str):
    if cmd == 'help':
        NOVA_help()
    elif cmd == 'time':
        NOVA_time()
    elif cmd == 'hi':
        NOVA_hi()
    elif cmd == 'youtube':
        NOVA_youtube()
    elif cmd == 'funk':
        NOVA_youtube_funk()             

'''
elif cmd == '':
    NOVA_()

    "":('','','','','',)

def NOVA_():
    webbrowser.open('')
'''

NOVA_CMD_LIST = {
    "help": ('список команд', 'команды', 'что ты умеешь', 'твои навыки', 'навыки'),
    "time": ('время', 'текущее время', 'сейчас времени', 'который час'),
    "hi":('привет','добрый день','здравствуй','преветствую'),

#далее для ссылки в ютубе
    "youtube":('ютуб','включи ютуб','открой ютуб'),
    "funk":('музыка','включи музыку','мызыка для кс 2')
}

def NOVA_help():
    # help
    text = "Я умею: ..."
    text += "произносить время ..."
    text += "и всё что вы добавите в меня"
    tts.va_speak(text)
    pass

def NOVA_time():
    now = datetime.datetime.now()
    text = "Сейч+ас " + num2words((now.hour), lang='ru') + " " + num2words(now.minute, lang='ru')
    tts.va_speak(text)

def NOVA_hi():
    play('hi')

#youtube script

def NOVA_youtube():
    webbrowser.open('https://www.youtube.com')
    play('ok')
def NOVA_youtube_funk():
    play('ok')
    webbrowser.open('https://www.youtube.com/watch?v=HcZw4UTfgmk')





def play(phrase, wait_done=True):
    filename = "sound/"

    if phrase == "greet":  # for py 3.8
        filename += f"greet{random.choice([1, 2])}.wav"
    elif phrase == "ok":
        filename += f"ok{random.choice([1, 2])}.wav"
    elif phrase == "hi":
        filename += f"hi{random.choice([1, 2])}.wav"
    elif phrase == "not_found":
        filename += "not_found.wav"
    elif phrase == "thanks":
        filename += "thanks.wav"
    elif phrase == "run":
        filename += "run.wav"
    elif phrase == "stupid":
        filename += "stupid.wav"
    elif phrase == "ready":
        filename += "ready.wav"
    elif phrase == "off":
        filename += "off.wav"

    filename = filename.replace(' wait', "")
    playsound(filename)


