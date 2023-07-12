from pydantic import BaseModel


class FastAPISettings(BaseModel):
    title: str = 'Georgian Spell Checker'
    version: str = '0.1.0'
    description: str = 'Georgian Spell Checker API'