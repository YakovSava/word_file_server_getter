import asyncio

from aiohttp.web import Response, run_app, Application, RouteTableDef, Request

routes = RouteTableDef()
app = Application()


@routes.get('/')
async def main_handler(request: Request):
	return Response(body='Server is start!')

@routes.get('/file')
async def file_get_handler(request:Request):
	pass

if __name__ == '__main__':
	run_app(app, host='192.168.100.8', port='80')