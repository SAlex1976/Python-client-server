# Task 5
import subprocess
import chardet


def ping_func(urls):
    cmds = ['ping', urls]
    ping = subprocess.Popen(cmds, stdout=subprocess.PIPE)

    for i, line in enumerate(ping.stdout):
        coding = chardet.detect(line)
        line = line.decode(coding['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
        if i == 4:
            ping.kill()


ping_func('yandex.ru')
ping_func('youtube.com')
