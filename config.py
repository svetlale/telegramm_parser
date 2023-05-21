from pydantic import BaseSettings
from typing import List, Any


class LoginCfg(BaseSettings):
    api_id: int = 27761512
    api_hash: str = "9f6f92e53b29e1775c81783980584acf"
    phone_number = "79135938668"


class ParserCfg(BaseSettings):
    input_channels: List[str] = []
    valid_channels: List[str] = []
    last_n_messages: int = 5
    num_of_channels: int = 200
    parse_date: Any = None
