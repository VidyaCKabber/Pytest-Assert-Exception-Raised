import re
import pytest
import sys


def check_email_format(email):
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return "ok"
    else:
        raise Exception("Invalid email format")


def check_number(num):
    if num != 19:
        raise Exception("Number is not equal to 19")
    return num


def check_divisible_by_zero(num1, num2):
    return num1 / num2


class TestCases:

    @pytest.mark.tryfirst
    @pytest.mark.parametrize(
        ("a", "b"), [(1, 2), (19, 0), (0, 5), (34, 3)]
    )
    def test_ZeroDivisionError(self, a, b):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                check_divisible_by_zero(a, b)
        else:
            assert check_divisible_by_zero(a, b) >= 0.0

    @pytest.mark.skipif('re' not in sys.modules, reason="requires the re library")
    @pytest.mark.email
    def test_email_exception(self):
        with pytest.raises(Exception) as e:
            assert check_email_format("vidya.merahkeegmail.com") == "Invalid email format"

    @pytest.mark.xfail(raises=IndexError)
    def test_IndexError(self):
        a = [1, 2, 3]
        # with pytest.raises(IndexError):
        #     print(a[3])
        assert a[3] == 4

    @pytest.mark.numbers
    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_number(self):
        with pytest.raises(Exception) as e:
            assert check_number(9) == 9

    @pytest.mark.xfail(run=False)
    def test_calling_undefined_fun(self):
        with pytest.raises(NameError):
            osmPytest()
        assert osmPytest() == 'Awesome framework'

    @pytest.mark.numbers
    @pytest.mark.parametrize(
        ("value", "num"), [(12.0, 11111111111111111111111111111111111111111111111)]
    )
    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_UnboundLocalError(self, value, num):
        res = value * num
        with pytest.raises(UnboundLocalError):
            for i in range(100):
                f = f ** 2

    @pytest.mark.trylast
    def test_RuntimeError(self):
        with pytest.raises(NameError):
            print(greeting)

    @pytest.mark.skip
    def test_nonExitedElement(self):
        with pytest.raises(ValueError):
            name = "Vidya"
            print(int(name))

    @pytest.mark.keyerror
    def test_KeyError(self):
        disc = {'name': 'Kruti', 'place': 'Hubli'}
        with pytest.raises(KeyError):
            assert disc['age'] == 18

    @pytest.mark.sysError
    def test_OSError(self):
        with pytest.raises(OSError):
            print('Press Return or Ctrl-C:', ignored=input())

    @pytest.mark.overflow
    def test_OverflowError(self):
        res = 2.0 * 9876543212345678912345678987654321
        with pytest.raises(OverflowError):
            for i in range(100):
                res = res ** 2
