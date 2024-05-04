from aiohttp import web
from pydantic import ValidationError

from app.handlers import stuff as stuff_handlers
from app.dto import stuff as stuff_dto

routes = web.RouteTableDef()


@routes.get(path='/healthcheck')
async def healthcheck(request):
	return web.Response()


@routes.post(path='/hash')
async def hash(request):
	try:
		data = await request.json()
		validated_data = stuff_dto.HashIn(**data)
		result = await stuff_handlers.hash(input_string=validated_data.string)
		return web.json_response(
			status=200,
			data=stuff_dto.HashOut(hash_string=result).model_dump()
		)

	except ValidationError as e:
		return web.json_response({'validation_errors': str(e)}, status=400)
