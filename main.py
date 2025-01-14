import config
import stt
import tts
import  script 
from fuzzywuzzy import fuzz
import datetime
from script import *
#програма сделана Mask_0F_Darkness ❤️

print(f"{config.NOVA_NAME} (v{config.NOVA_VER}) начал свою работу ...")
#script.play('run')
def va_respond(voice: str):
    voice_print = voice.replace('ного','нова')
    print(voice_print)
    if voice.startswith(config.NOVA_ALIAS):
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



# начать прослушивание команд
stt.va_listen(va_respond)
