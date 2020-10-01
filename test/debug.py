import sys
sys.path.append('.')
from rconfig import Config
import rconfig
print(rconfig.__path__)

if __name__ == '__main__':
    config = Config.from_file('./data/example.yaml')
    print(config.TEST.DATA)
    print(config.TEST.ENV_PATH)
