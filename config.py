from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

    @staticmethod
    def from_env(env: Env):
        token = env.str('BOT_TOKEN')
        admin_ids = env.int('ADMIN_IDS')

        return TgBot(token=token, admin_ids=admin_ids)


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:

    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot.from_env(env))