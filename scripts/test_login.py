import random

import pytest


class TestLogin:
    @pytest.mark.run(order=1)
    def test_login1(self):
        print("login1")
        if random.randint(1, 5) == 1:
            assert True
        else:
            assert False


    @pytest.mark.run(order=4)
    def test_login3(self):
        print("login3")

    @pytest.mark.run(order=2)
    def test_login2(self):
        print("login2")

