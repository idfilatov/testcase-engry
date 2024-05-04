import pytest

from app.main import create_app


@pytest.fixture
def test_client(event_loop, aiohttp_client):
    app = create_app()
    return aiohttp_client(app)


@pytest.mark.asyncio
async def test_healthcheck(test_client):
    client = await test_client
    resp = await client.get("/healthcheck")
    assert resp.status == 200


@pytest.mark.asyncio
async def test_hash_with_wrong_body(test_client):
    client = await test_client
    resp = await client.post("/hash", json={'field': 'value'})
    assert resp.status == 400


@pytest.mark.asyncio
async def test_hash_with_right_body(test_client):
    client = await test_client
    resp = await client.post("/hash", json={'string': 'value'})
    assert await resp.json() == {'hash_string': 'cd42404d52ad55ccfa9aca4adc828aa5800ad9d385a0671fbcbf724118320619'}
