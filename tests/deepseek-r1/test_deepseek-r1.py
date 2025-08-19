import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE = "deepseek-r1.gotmpl"


@pytest.mark.parametrize("file", ["empty.json", "simple.json", "thinking.json"])
def test_deepseek_r1(file: str):
    run_test("deepseek-r1", file)
