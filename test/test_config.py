from rconfig import Config

if __name__ == '__main__':
    config = Config.from_file('./data/example.yaml')
    print(config.TEST.DATA)
