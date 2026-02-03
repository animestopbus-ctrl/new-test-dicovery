import motor.motor_asyncio

from config import MONGO_URI, DB_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

async def get_collection(name: str):
    return db[name]
