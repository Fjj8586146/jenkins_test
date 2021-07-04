import pytest

version = 5


class TestLogin:
    @pytest.mark.skipif(version < 7, reason='版本低于7的跳过')
    @pytest.mark.run(order=2)
    def test_01(self):
        print("2")
        assert 1

    @pytest.mark.skipif(version < 7, reason='版本低于7的跳过')
    @pytest.mark.run(order=1)
    def test_02(self):
        print('1')
        assert 1

    @pytest.mark.run(order=0)
    def test_03(self):
        print('顶顶顶')
        assert 0


    def test_04(self):
        print('没写')
        assert 0

    @pytest.mark.run(order=-1)
    def test_05(self):
        print('-1')
        assert 1

    @pytest.mark.run(order=-10)
    def test_06(self):
        print('-10')
        assert 1


    # 预期成功，结果成功
    @pytest.mark.xfail(condition= False, reason='预期失败')
    def test_07(self):
        print('预期成功，结果成功')
        assert 1

    # 预期成功，结果失败
    @pytest.mark.xfail(condition=False, reason='预期失败')
    def test_08(self):
        print('预期成功，结果失败')
        assert 1

    # 预期失败，结果成功
    @pytest.mark.xfail(condition=True, reason='预期失败')
    def test_09(self):
        print('预期失败，结果成功')
        assert 1

    # 预期失败，结果失败
    @pytest.mark.xfail(condition=True, reason='预期失败')
    def test_10(self):
        print('预期失败，结果失败')
        assert 1

    def test_11001100(self):
        print(11001100)
        assert 0
    def test_11001101212121(self):
        print(11001100121212)
        assert 0


