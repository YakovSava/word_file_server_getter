from os.path import join
from urllib.parse import unquote
from aiofiles import open as aiopen


class Binder:

    def __init__(self, path: str='files', html_path: str='html'):
        self._path = path
        self._html = html_path

    async def get_wordfile(self, filename: str) -> dict:
        try:
            async with aiopen(join(self._path, unquote(filename)), 'rb') as file:
                data = {
                    'content_type': 'application/msword',
                    'body': await file.read(),
                    'status': 200
                }
        except:
            data = {
                'content_type': 'text/plain',
                'body': '',
                'status': 404
            }
        return data

    async def get_css(self, style_name: str) -> dict:
        try:
            async with aiopen(join(self._html, unquote(filename)), 'r', encoding='utf-8') as file:
                data = {
                    'content_type': 'text/css',
                    'body': await file.read(),
                    'status': 200
                }
        except:
            data = {
                'content_type': 'text/plain',
                'body': '',
                'status': 404
            }
        return data

    async def get_html(self, html_name: str) -> dict:
        try:
            async with aiopen(join(self._html, unquote(filename)), 'r', encoding='utf-8') as file:
                data = {
                    'content_type': 'text/html',
                    'body': await file.read(),
                    'status': 200
                }
        except:
            data = {
                'content_type': 'text/plain',
                'body': '',
                'status': 404
            }
        return data
