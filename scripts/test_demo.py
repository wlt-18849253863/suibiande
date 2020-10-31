import pytest


class TestDemo:

    @pytest.mark.run(order=1)
    def test_1(self):
        print("1")

    @pytest.mark.run(order=2)
    def test_2(self):
        print("2")

    @pytest.mark.run(order=1.5)
    def test_3(self):
        print("1.5")

    @pytest.mark.run(order=-1)
    def test_4(self):
        print("-1")

    @pytest.mark.run(order=-2)
    def test_5(self):
        print("-2")

    @pytest.mark.run(order=-1.5)
    def test_6(self):
        print("-1.5")

    @pytest.mark.run(order=0)
    def test_7(self):
        print("0")

    def test_8(self):
        print("什么都不写")