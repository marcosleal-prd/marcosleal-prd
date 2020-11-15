import os


def getenv_or_raise(env: str) -> str:
    environment = os.getenv(env)
    if environment is None:
        raise EnvironmentError(f'Environment {env} is not defined.')

    return environment
