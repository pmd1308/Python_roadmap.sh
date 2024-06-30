import httpx
import asyncio
from config import RETRY_LIMIT

async def send_request(client, endpoint, report):
    attempt = 0
    while attempt < RETRY_LIMIT:
        try:
            response = await client.get(endpoint)
            response_time = response.elapsed.toatal_seconds()
            report.log(endpoint, response.status_code, response_time)
            return
        except httpx.RequestError as e:
            attempt += 1
            print(f"Attempt {attempt} - Request to {endpoint} failed: {e}")
            if attempt == RETRY_LIMIT:
                report.log(endpoint, 500, 0)
                return
async def run_requests(endpoint, num_requests, report):
    async with httpx.AsyncClient() as client:
        tasks = [send_request(client, endpoint, report) for _ in range(num_requests)]
        await asyncio.gather(*tasks)