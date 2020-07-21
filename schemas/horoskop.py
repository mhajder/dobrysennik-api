from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, HttpUrl


class ZodiacSigns(str, Enum):
    aries = "baran"
    taurus = "byk"
    gemini = "bliznieta"
    cancer = "rak"
    leo = "lew"
    virgo = "panna"
    libra = "waga"
    scorpio = "skorpion"
    sagittarius = "strzelec"
    capricorn = "koziorozec"
    aquarius = "wodnik"
    pisces = "ryby"


class ZodiacSignsPL(str, Enum):
    aries = "Baran"
    taurus = "Byk"
    gemini = "Bliźnięta"
    cancer = "Rak"
    leo = "Lew"
    virgo = "Panna"
    libra = "Waga"
    scorpio = "Skorpion"
    sagittarius = "Strzelec"
    capricorn = "Koziorożec"
    aquarius = "Wodnik"
    pisces = "Ryby"


class Angels(str, Enum):
    id_1 = "Archanioł Rafał"
    id_2 = "Archanioł Michał"
    id_3 = "Archanioł Uriel"
    id_4 = "Archanioł Gabriel"
    id_5 = "Archanioł Metatron"
    id_6 = "Anioły białego płomienia"
    id_7 = "Anioły fioletowego płomienia"
    id_8 = "Anioły złotego płomienia"
    id_9 = "Anioły błękitnego płomienia"
    id_10 = "Anioł światła"
    id_11 = "Anioły wśród ludzi"
    id_12 = "Anioł nawrócenia"
    id_13 = "Anioł strachu"
    id_14 = "Anioł uzdrowienia"
    id_15 = "Anioł piękna"
    id_16 = "Anioł wsparcia"
    id_17 = "Anioł stróż"
    id_18 = "Anioł siły"
    id_19 = "Anioł rozwoju duchowego"
    id_20 = "Anioł szczęścia"
    id_21 = "Anioł przemijania"
    id_22 = "Anioł miłości"
    id_23 = "Anioł pocieszenia"
    id_24 = "Archanioł Chamuel"
    id_25 = "Anielski przewodnik"
    id_26 = "Tajemnicza siła anielska"
    id_27 = "Anioł walki"
    id_28 = "Anioł przemiany"
    id_29 = "Anioł czasu"
    id_30 = "Anioł odwagi"
    id_31 = "Anioł wybaczenia"
    id_32 = "Anioł zrozumienia"


class HoroskopAnielskiTypes(str, Enum):
    id_1 = "Przesłanie ogólne"
    id_2 = "Rodzina, miłość i znajomi"
    id_3 = "Finanse i praca"
    id_4 = "Zdrowie i kondycja"


class Angel(BaseModel):
    id: int
    name: str
    image: HttpUrl


class Horoscope(BaseModel):
    id: int
    title: str
    message: str
    angel: Optional[Angel]


class HoroskopAnielski(BaseModel):
    date: str
    zodiac_sign: str
    horoscopes: List[Horoscope]
