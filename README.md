# Python Rate Limiter
# ⚡ Lightweight Sliding Window Rate Limiter

An ultra-lightweight, zero-dependency Python implementation of the **Sliding Window Log** algorithm for API throttling and traffic control. Perfect for microservices, testing, and small-scale applications.

## ✨ Features
- **Sliding Window Accuracy:** Eliminates request bursts at window boundaries (unlike Fixed Window algorithms).
- **Zero Dependencies:** Built entirely using Python's standard libraries (`time`).
- **Memory Efficient:** Dynamically cleans up expired timestamps on every request check.
- **Developer Friendly:** Clean, fully commented, and easy to read.
