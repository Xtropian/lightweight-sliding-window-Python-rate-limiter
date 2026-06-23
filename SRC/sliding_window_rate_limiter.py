import time

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_size_seconds: float):
        """
        Initializes the rate limiter.
        
        :param max_requests: Maximum requests allowed within the sliding window.
        :param window_size_seconds: The duration of the window in seconds.
        """
        self.max_requests = max_requests
        self.window_size_seconds = window_size_seconds
        self.user_requests = {}

    def is_allowed(self, user_id: str) -> bool:
        """
        Checks if a user request is allowed or throttled.
        """
        current_time = time.time()
        
        if user_id not in self.user_requests:
            self.user_requests[user_id] = []
            
        request_history = self.user_requests[user_id]
        window_start_time = current_time - self.window_size_seconds
        
        # Clean up expired timestamps from the past
        while request_history and request_history[0] <= window_start_time:
            request_history.pop(0)
            
        # Check limit
        if len(request_history) < self.max_requests:
            request_history.append(current_time)
            return True
        return False