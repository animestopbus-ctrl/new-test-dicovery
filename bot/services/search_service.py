from datetime import datetime, timedelta

from models.channel_model import Channel
from database import get_collection
from services.scraper import scrape_channels
from utils.logger import logger

async def search_channels(keyword: str) -> list[Channel]:
    try:
        collection = await get_collection("search_cache")
        cache = await collection.find_one({"keyword": keyword.lower()})

        if cache and datetime.utcnow() - cache["scraped_at"] < timedelta(hours=24):
            return [Channel(**ch) for ch in cache["channels"]]

        raw_channels = await scrape_channels(keyword)
        channels = []
        for ch in raw_channels:
            channels.append(Channel(
                name=ch["name"],
                username=ch["username"],
                subscriber_count=ch["subscriber_count"],
                source="tgstat",
                keyword=keyword,
                scraped_at=datetime.utcnow()
            ))

        if channels:
            await collection.replace_one(
                {"keyword": keyword.lower()},
                {
                    "keyword": keyword.lower(),
                    "channels": [ch.model_dump() for ch in channels],
                    "scraped_at": datetime.utcnow()
                },
                upsert=True
            )
            logger.info(f"Cached {len(channels)} results for '{keyword}'")

        return channels
    except Exception as e:
        logger.error(f"Search service error: {e}")
        return []