import time

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_size_seconds: float):
        """
        Initializes the rate limiter.
        
        :param max_requests: The maximum number of requests allowed within the window.
        :param window_size_seconds: The length of the sliding window in seconds.
        """
        self.max_requests = max_requests
        self.window_size_seconds = window_size_seconds
        
        # This dictionary will store the history of request timestamps for each user.
        # Key: user_id (string), Value: list of timestamps [float, float, ...]
        self.user_requests = {}

    def is_allowed(self, user_id: str) -> bool:
        """
        Checks if a user is allowed to make a request based on the sliding window.
        
        :param user_id: A unique identifier for the user (e.g., IP address or username).
        :return: True if allowed, False if throttled.
        """
        current_time = time.time()  # Get the exact current time in seconds
        
        # If this is a brand new user, give them an empty history list
        if user_id not in self.user_requests:
            self.user_requests[user_id] = []
            
        # Get the timestamp history for this specific user
        request_history = self.user_requests[user_id]
        
        # --- THE SLIDING WINDOW MAGIC ---
        # Define the boundary of our current window (e.g., current time minus 10 seconds)
        window_start_time = current_time - self.window_size_seconds
        
        # Remove any timestamps that are older than our window start time
        # We use a while loop to keep removing the oldest items from the front of the list
        while request_history and request_history[0] <= window_start_time:
            request_history.pop(0)
            
        # Check if the user has room left in their current window
        if len(request_history) < self.max_requests:
            # They have room! Record the current request's timestamp
            request_history.append(current_time)
            return True
        else:
            # They have sent too many requests. Block them!
            return False

# --- SIMULATION AND TESTING CODE ---
# This part runs automatically to show you how it works in real-time.
if __name__ == "__main__":
    print("--- Starting Rate Limiter Simulation ---")
    print("Setting Limit: Maximum 3 requests allowed every 5 seconds.\n")
    
    # Create an instance of our rate limiter (3 requests per 5 seconds)
    limiter = SlidingWindowRateLimiter(max_requests=3, window_size_seconds=5.0)
    
    user = "user_123"
    
    # Let's simulate sending 5 rapid requests
    for i in range(1, 6):
        allowed = limiter.is_allowed(user)
        status = "ALLOWED" if allowed else "BLOCKED (Throttled)"
        print(f"Request {i} at second {i*0.2:.1f}: {status}")
        time.sleep(0.2) # Wait a tiny fraction of a second before the next request
        
    print("\n...Waiting for 5 seconds to let the window slide and reset...")
    time.sleep(5)
    
    # Try again after waiting
    allowed = limiter.is_allowed(user)
    status = "ALLOWED" if allowed else "BLOCKED (Throttled)"
    print(f"Request 6 after waiting: {status}")