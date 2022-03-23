from environs import Env

env = Env()
env.read_env()

MANAGER_TELEGRAM_ID = env.str("MANAGER_TELEGRAM_ID")
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")



