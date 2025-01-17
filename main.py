import config
import stt
import tts
import  script 
from fuzzywuzzy import fuzz
import datetime
from script import *
import subprocess
import time
#програма сделана Mask_0F_Darkness ❤️

subprocess.Popen("python telegramm_bot.py") 
time.sleep(8)
print(f"{config.NOVA_NAME} (v{config.NOVA_VER}) начал свою работу ...")


def va_respond(voice: str):
    voice_print = voice.replace('ного','нова')
    print(voice_print)
    if voice.startswith(config.NOVA_ALIAS) and config.NOVA_HELPER==1:
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in script.NOVA_CMD_LIST.keys():
            NOVA_AI(voices)
        else:
            script.execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.NOVA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in script.NOVA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


stt.va_listen(va_respond)
