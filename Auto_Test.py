#write pytest for main.py

Path: test_main.py
"""This is the test file for the weather app"""

import pytest
from main import read_vault
from main import weather

def test_read_vault():
    assert read_vault() == {"error": "File not found"}

def test_weather():
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}
    assert weather("US", "New York") == {"city": "New York", "forecast": "Rain and a thunderstorm from this afternoon to late tonight"}

if __name__ == "__main__":
    pytest.main()
