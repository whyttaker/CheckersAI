import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor
from random import random

trials = 0
wins = 0

def run():
    global trials
    global wins

    if random() < 0.5:
        command = 'python3 AI_Runner.py 8 8 3 l Sample_AIs/Random_AI/main.py ../src/checkers-cpp/main'
        result = subprocess.run(command.split(' '), stdout=subprocess.PIPE)
        lines = result.stdout.decode('utf-8').splitlines()
        #for line in lines:
            # print(line)
        if '1' in lines[-1]:
            print('lost', end=' ')
            wins += 0
        elif '2' in lines[-1]:
            print('win', end=' ')
            wins += 1
        else:
            print('tie', end=' ')
            wins += 1
    else:
        command = 'python3 AI_Runner.py 8 8 3 l ../src/checkers-cpp/main Sample_AIs/Random_AI/main.py'
        result = subprocess.run(command.split(' '), stdout=subprocess.PIPE)
        lines = result.stdout.decode('utf-8').splitlines()
        #for line in lines:
            # print(line)
        if '2' in lines[-1]:
            print('lost', end=' ')
            wins += 0
        elif '1' in lines[-1]:
            print('win', end=' ')
            wins += 1
        else:
            print('tie', end=' ')
            wins += 1

    trials += 1

    print(wins, "/", trials, ": ", wins/trials)

def main():
    executor = ThreadPoolExecutor(22)
    for i in range(100):
        future = executor.submit(run)

if __name__ == "__main__":
    main()
