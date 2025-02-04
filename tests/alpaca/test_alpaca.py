import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="alpaca.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_alpaca(file: str):
    run_test("alpaca", file)
