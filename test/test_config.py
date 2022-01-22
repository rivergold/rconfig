from rconfig import Config

if __name__ == '__main__':
    # YAML
    config = Config.from_file('./data/example.yaml')
    print(config.TEST.DATA)
    print(config.TEST.ENV_PATH)
    # Json
    config = Config.from_file('./data/example.json')
    print(config.test.data)
    print(config.test.env_path)