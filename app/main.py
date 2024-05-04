import click
from aiohttp import web

from app.routes import stuff as stuff_routes


def create_app():
    app = web.Application()
    app.add_routes(stuff_routes.routes)

    return app


@click.command()
@click.option("--port", default=9000, help="port for run app")
def main(port):
    app = create_app()
    print('app created')
    web.run_app(app, host='0.0.0.0', port=port)
    print('app started')


if __name__ == "__main__":
    main()
