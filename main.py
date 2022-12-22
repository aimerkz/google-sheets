from app.data_logs import reading_logs, creating_logs


if __name__ == '__main__':
    command = input('Введите команду ')
    commands = {
        'read': reading_logs,
        'load': creating_logs
    }
    commands[command]()
