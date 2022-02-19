import http.client

class CircuitBreaker:
    def __init__(self, http.Client, error_threshold, time_window):
        self.client = http.Client
        self.error_threshold = error_threshold
        self.time_window = time_window


    def do_request(self, url):
        try:
            response = self.client.get(url)
            self.error_count = 0
            return response
        except Exception as e:
            self.error_count += 1
            self.last_error_time = time.time()
            raise e

if __name__ == '__main__':
        client = http.Client()
    stub_client = StubClient()
    breaker = CircuitBreaker(stub_client, x, y)
    for n in range(10):
        try:
            response = breaker.do_request('https://www.cnn.com')
            print(response.status_code)
            sleep(1)
        except Exception as e:
            print(e)
