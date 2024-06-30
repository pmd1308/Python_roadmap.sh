import asyncio
import time
from config import *
from report import Report
from utils import run_requests

def main():
    threads = []
    report = Report()
    start_time = time.time()

    for endpoint ENDPOINTS:
        num_requests_per_thread = NUM_REQUESTS // (NUM_THREADS * len(ENDPOINTS))
        for _ in range(NUM_THREADS):
            thread = asyncio.Thread(target=run_requests, args=(endpoint, num_requests_per_thread, report))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Test completed in {end_time - start_time} seconds")
    
    report.print_summary()
    report.generate_csv()

if __name__ == "__main__":
    main()