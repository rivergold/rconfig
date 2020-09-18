import re, os
import yaml


def env_constructor(loader, node):
    value = node.value
    res = env_matcher.findall(value)
    env_name = res[0]
    return os.environ.get(env_name)


def get_env(match):
    return os.environ.get(match.group()[2:-1])


if __name__ == '__main__':
    env_matcher = re.compile(r'\$\{([^{^}]+)\}')

    text = '${PATH}/123/${LD_LIBRARY_PATH}'

    res = env_matcher.sub(get_env, text)
    print(res)
    # yaml.add_implicit_resolver('!env', env_matcher)
    # yaml.add_constructor('!env')
