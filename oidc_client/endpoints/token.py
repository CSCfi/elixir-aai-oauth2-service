"""Token Endpoint."""

from aiohttp import web

from ..utils.utils import get_from_session
from ..utils.logging import LOG


async def token_request(request):
    """Handle token requests."""
    LOG.debug('Handle token request.')

    response = {'access_token': ''}

    # Read saved access token from user session
    response['access_token'] = await get_from_session(request, 'access_token')

    return web.json_response(response)
