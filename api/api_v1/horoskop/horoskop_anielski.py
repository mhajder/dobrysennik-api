from fastapi import APIRouter, Response

from api.api_v1.deps import *

router = APIRouter()


@router.get(
    "/{zodiac_sign}",
    response_model=HoroskopAnielski,
    summary="Returns daily, angelic horoscopes",
    description="Endpoint returning daily, angelic horoscopes of a given zodiac sign.",
)
async def get_horoscope(zodiac_sign: ZodiacSigns, response: Response):
    response.headers["Expires"] = await cache_header()
    return await horoskop_anielski_scrape(zodiac_sign.name)
