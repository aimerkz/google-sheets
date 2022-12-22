import sched
import time
from app.data_logs import reading_logs, creating_logs


s = sched.scheduler(time.time, time.sleep)

commands = {
    'read': reading_logs,
    'load': creating_logs
}


def main():
    command = input('Введите команду ')
    if command == 'read':
        commands[command]()
    elif command == 'load':
        s.enter(3, 1, main)
        commands[command]()
        print('OK')
    else:
        print('Введите либо read, либо load')


if __name__ == '__main__':
    main()
    s.run()
