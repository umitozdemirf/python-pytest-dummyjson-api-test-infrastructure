import os


class BaseConfig:
    env = "dev"

    if os.environ.get('ENV') is not None:
        print('ENV is read from ENV: {}'.format(os.environ.get('ENVS')))
        env = os.environ['ENVS']

    # we can use switch case or string manipulation if we have more than one environment
    if env == 'dev':
        API_URL = "https://dummyjson.com"

