# config.py

NUM_REQUESTS = 1000  # Total number of requests to be sent
NUM_CONCURRENT_REQUESTS = 10  # Number of concurrent requests
ENDPOINTS = [
    "http://localhost:8080/users",
    "http://localhost:8080/accounts",
    "http://localhost:8080/cards"
]  # List of API endpoints to be tested
RETRY_LIMIT = 3  # Number of retries for failed requests
