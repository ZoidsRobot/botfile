# (©)Codexbotz
# Recode by @kang_culiknee


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5720208007:AAEb1tGQDKNjkudASlvBrNjPao4TqQSdoq0")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22703395"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "062fb3fcdec3135a29ba93fadb97ddc0")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001798713033"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5730958503"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "kntl1199")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://awxqnloq:A871j1eJ9OHBUwyb00babO3uw3HWd_Dj@castor.db.elephantsql.com/awxqnloq")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "vvslh_pro")
GROUP = os.environ.get("GROUP", "vvslh_pro")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL","-1001857364012"))

FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001694464041"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5730958503").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(5396158379)
ADMINS.append(1996472517)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
