from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "6435225"
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "1679112664"))
SUPPORT_GRP = "+cXIPgHSuJnxiNjU1"
UPDATE_CHNL = "ai_image_junction"
OWNER_USERNAME = "OfficialDurgesh"