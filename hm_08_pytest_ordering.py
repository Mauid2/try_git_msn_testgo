import pytest


class TestDemo:
    # 语法:@pytest.mark.run(order=序号)
    # 注意:run(order=序号)没有代码提示，
    # 需要手写!
    # @pytest.mark.run(order=2)
    # 新版本如下：
    @pytest.mark.order(1)
    def test_one(self):
        print("Test one")

    @pytest.mark.order(3)
    def test_two(self):
        print("Test two")

    @pytest.mark.order(2)
    def test_three(self):
        print("Test three")

if __name__ == '__main__':
    pytest.main(['-s'],"hm_08_pytest_ordering.py")