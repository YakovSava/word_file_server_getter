from os import listdir
from aiohttp.web import Response, run_app, Application, RouteTableDef, Request
from plugins.binder import Binder

routes = RouteTableDef()
app = Application()
binder = Binder()


@routes.get('/')
async def main_handler(request: Request):
    data = await binder.get_html('main.html')
    data['body'] = (data['body']
                    .replace('(No files)',
                             ''.join(
                                 f'<a href="/word?{filename}">{filename}</a><br>\n'
                                 for filename in (listdir('files'))
                             )
                             )
                    )
    return Response(
        body=data['body'],
        content_type=data['content_type'],
        status=data['status']
    )


@routes.get('/styles')
async def css_handler(request: Request):
    data = await binder.get_css(str(request.url).split('?')[1])
    return Response(
        body=data['body'],
        content_type=data['content_type'],
        status=data['status']
    )


@routes.get('/word')
async def file_get_handler(request: Request):
    data = await binder.get_wordfile(str(request.url).split('?')[1])
    return Response(
        body=data['body'],
        content_type=data['content_type'],
        status=data['status']
    )

if __name__ == '__main__':
    run_app(app, host='localhost', port='80')
