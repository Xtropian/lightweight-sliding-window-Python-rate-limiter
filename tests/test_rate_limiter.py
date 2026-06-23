import os
import sys
import unittest

# 1. Dynamically find the absolute path to your project root
TARGET_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(TARGET_DIR, "src")

# 2. Tell Python to look directly inside both folders
if TARGET_DIR not in sys.path:
    sys.path.insert(0, TARGET_DIR)
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# 3. Print a helpful message to Slim Shady's Terminal so we can see what's happening
print("\n--- 🛠️ PYTHON PATH DEBUGGER 🛠️ ---")
print(f"Looking for 'src' folder inside: {TARGET_DIR}")
print(f"Does 'src' folder exist there? {os.path.exists(SRC_DIR)}")
print("---------------------------------\n")

# 4. Now try importing (supporting both import styles just in case!)
try:
    from src.sliding_window_rate_limiter import SlidingWindowRateLimiter
except ModuleNotFoundError:
    from sliding_window_rate_limiter import SlidingWindowRateLimiter


class TestSlidingWindowRateLimiter(unittest.TestCase):
    
    def test_allow_requests_within_limit(self):
        limiter = SlidingWindowRateLimiter(max_requests=2, window_size_seconds=1.0)
        user = "test_user"
        self.assertTrue(limiter.is_allowed(user))
        self.assertTrue(limiter.is_allowed(user))

    def test_block_requests_over_limit(self):
        limiter = SlidingWindowRateLimiter(max_requests=2, window_size_seconds=1.0)
        user = "test_user"
        limiter.is_allowed(user)
        limiter.is_allowed(user)
        self.assertFalse(limiter.is_allowed(user))

if __name__ == '__main__':
    unittest.main()