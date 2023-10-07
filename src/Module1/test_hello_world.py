# pytest to check whther the output is hello world or not

import pytest
from src.Module1.hello_world import hello_world

class TestHelloWorld:
        # Test with two positive integers
        def test_hello_world(self):
            assert hello_world() == "Hello World!"