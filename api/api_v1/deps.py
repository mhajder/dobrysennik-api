import re
from datetime import date, datetime, timedelta

import aiohttp
import pytz
from bs4 import BeautifulSoup

from core.config import settings
from schemas.horoskop import *

pl_timezone = pytz.timezone("Europe/Warsaw")
gmt_timezone = pytz.timezone("GMT")


async def cache_header():
    today = datetime.now(pl_timezone).date()
    expiry_time_pl = (datetime.combine(today, datetime.min.time())
                      + timedelta(days=1, minutes=5)).astimezone(pl_timezone)
    expiry_time_gmt = gmt_timezone.normalize(expiry_time_pl)
    expiry_time = expiry_time_gmt.strftime("%a, %d %b %Y %H:%M:%S GMT")
    # header = {"Expires": expiry_time}
    return expiry_time


async def horoskop_anielski_scrape(zodiac_sign):
    url = f"http://www.dobrysennik.pl/horoskop/horoskop-anielski/{ZodiacSigns[zodiac_sign].value}"
    response_data = {
        "date": str(datetime.now(pl_timezone).date()),
        "zodiac_sign": ZodiacSignsPL[zodiac_sign].value,
        "horoscopes": [],
    }

    timeout = aiohttp.ClientTimeout(total=10, connect=2)
    async with aiohttp.ClientSession(headers={"Connection": "keep-alive", "User-Agent": settings.AIOHTTP_HEADERS},
                                     timeout=timeout) as session:
        async with session.get(url) as r:
            if r.status == 200:
                html = await r.read()

                page = BeautifulSoup(html.decode("utf-8"), "html.parser")
                elements = BeautifulSoup(str(page.find_all(class_="okresowy")), "html.parser")
                horoscopes = elements.findAll("p")

                for idx, horoscope in enumerate(horoscopes):
                    angel_id = re.search(r"^(https?://)?(www\.)?(dobrysennik\.pl/img/anioly/)?(\d+)?(\.jpg)",
                                         horoscope.img["src"])[4]
                    response_data["horoscopes"].append({
                        "id": idx + 1,
                        "title": HoroskopAnielskiTypes[f"id_{idx + 1}"].value,
                        "message": horoscope.br.next.strip(" "),
                        "angel": {
                            "id": angel_id,
                            "name": Angels[f"id_{angel_id}"].value,
                            "image": horoscope.img["src"]
                        }
                    })

                return response_data
