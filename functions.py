from time import time as unixtime


def log(e: str):
    with open('log.txt', 'a') as file:
        file.write(f'\n{unixtime()} - {e}\n')
