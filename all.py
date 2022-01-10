import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./report_temp -o ./reports --clean')


