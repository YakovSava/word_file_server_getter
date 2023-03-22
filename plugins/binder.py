import asyncio

from os.path import join
from urllib.parse import unquote
from aiofiles import open as aiopen

class Binder:

	def __init__(self, path:str='files'):
		self._path = path

	async def _get_wordfile(self, filename:str) -> dict:
		try:
			async with aiopen(join(self._path, filename)) as file:
				file_data = await file.read()