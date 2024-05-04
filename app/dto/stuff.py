from pydantic import BaseModel


class HashIn(BaseModel):
	string: str


class HashOut(BaseModel):
	hash_string: str
