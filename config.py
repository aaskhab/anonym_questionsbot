from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot


env: Env = Env()
env.read_env()

config = Config(
    tg_bot=TgBot(
        token=env('BOT_TOKEN'),
        admin_ids=env.int(('ADMIN_IDS'))
    )
)

def load_config(path: str | None = None) -> Config:

    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=env.int('ADMIN_IDS')
        )
    )