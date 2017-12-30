import os

DEBUG = True


def truthy(val):
    strval = str(val)
    return strval.lower() == 'true'


class ConfigError(Exception):
    pass


def env(name, default=None):
    from_env = os.environ.get(name)
    if from_env is not None:
        return from_env

    if DEBUG and (default is not None):
        print("{} not found in environment, using default.".format(name))
        return default
    else:
        raise ConfigError("{} not found in environment".format(name))


USE_FIREFOX = truthy(env('USE_FIREFOX'))
