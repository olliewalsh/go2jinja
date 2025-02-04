import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE = "zephyr.gotmpl"


@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_zephyr(file: str):
    run_test("zephyr", file)
