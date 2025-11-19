from dotenv import load_dotenv
import os

load_dotenv()

print("KEY:", os.getenv("APCA_API_KEY_ID"))
print("SECRET:", os.getenv("APCA_API_SECRET_KEY"))
print("BASE URL:", os.getenv("APCA_API_BASE_URL"))
