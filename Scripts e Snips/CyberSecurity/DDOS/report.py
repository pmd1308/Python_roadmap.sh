import pandas as pd
import time

class Report:
    def __init__(self):
        self.data = []

    def log(self, endpoint, status_code, response_time):
        self.data.append({
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'endpoint': endpoint,
            'http_status_code': status_code,
            'http_response_time': response_time
        })
        

    def print_summary(self, filename='report.csv'):
        df = pd.DataFrame(self.data)
        total_requests = len(df)
        failed_requests = df[df['status_code'] != 200].shape[0]
        avarage_response_time = df['response_time'].mean() if total_requests > 0 else 0

        print(f"Total Requests: {total_requests}")
        print(f"Failed Requests: {failed_requests}")
        print(f"Average Response Time: {average_response_time:.2f} seconds")

        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)