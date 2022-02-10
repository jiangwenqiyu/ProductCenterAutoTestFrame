import pytest


def test_01():
    with pytest.raises(AssertionError) as e:
        assert 1==1
        print(123123123123)

    print(456456456456)




if __name__ == '__main__':
    pytest.main()










