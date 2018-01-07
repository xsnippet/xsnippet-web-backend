import aiohttp
import aiohttp.web


async def get_raw_snippet_content(request):
    try:
        _id = int(request.match_info['id'])
    except (IndexError, ValueError):
        raise aiohttp.web.HTTPBadRequest('id must be specified and must be an integer')

    # fetch the snippet from the API
    async with aiohttp.ClientSession() as session:
        url = request.app.conf.API_URL + '/snippets/' + str(_id)
        async with session.get(url) as response:
            if response.status == 404:
                raise aiohttp.web.HTTPNotFound

            snippet = await response.json()

    return aiohttp.web.Response(text=snippet['content'])


def create_app(conf):
    app = aiohttp.web.Application()
    app.conf = conf

    app.router.add_get('/snippets/{id}/raw', get_raw_snippet_content)

    return app
