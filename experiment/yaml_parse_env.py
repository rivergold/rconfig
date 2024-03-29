import re, os
import yaml


def env_constructor(loader, node):
    def get_env(match):
        env = os.environ.get(match.group()[2:-1])
        if env is None:
            return match.group()
        return env

    value = node.value
    return env_parser.sub(get_env, value)


env_parser = re.compile(r'\$\{([^{^}]+)\}')
yaml.add_implicit_resolver('!env', env_parser)
yaml.add_constructor('!env', env_constructor)

if __name__ == '__main__':
    data = """
    ENV_INFO: ${PATH1}/123
    DATA: 123
    """

    config = yaml.load(data, Loader=yaml.FullLoader)
    print('ok')
    print(config['ENV_INFO'], config['DATA'])
