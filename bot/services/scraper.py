import aiohttp
from bs4 import BeautifulSoup

from utils.logger import logger

async def scrape_channels(keyword: str) -> list[dict]:
    url = f"https://tgstat.com/search?query={keyword.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as response:
                if response.status != 200:
                    logger.warning(f"Scrape failed: status {response.status}")
                    return []
                html = await response.text()

        soup = BeautifulSoup(html, "html.parser")
        results = []

        for item in soup.find_all("div", class_="search-result-item"):
            try:
                title_elem = item.find("h5", class_="channel-title")
                name = title_elem.text.strip() if title_elem else None

                link_elem = item.find("a", class_="channel-link")
                username = link_elem["href"].split("/")[-1].lstrip("@") if link_elem else None

                subs_elem = item.find("small", class_="text-muted")
                subs_text = subs_elem.text.strip().split()[0] if subs_elem else "0"

                multiplier = 1
                if "K" in subs_text.upper():
                    multiplier = 1000
                    subs_text = subs_text.rstrip("Kk")
                elif "M" in subs_text.upper():
                    multiplier = 1000000
                    subs_text = subs_text.rstrip("Mm")

                subscriber_count = int(float(subs_text) * multiplier)

                if name and username:
                    results.append({
                        "name": name,
                        "username": username,
                        "subscriber_count": subscriber_count
                    })
            except Exception as e:
                logger.debug(f"Parse error in item: {e}")
                continue

        logger.info(f"Scraped {len(results)} channels for '{keyword}'")
        return results
    except Exception as e:
        logger.error(f"Scraper error: {e}")
        return []
