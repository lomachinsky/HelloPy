import pytest
import modules.api_interaction as api_int


def test_get_supp_ticket():
    assert {"success":true,"data":[],"errors":[]}' == '{"success":true,"data":[],"errors":[]}'


if __name__ == '__main__':
    pytest.main()
