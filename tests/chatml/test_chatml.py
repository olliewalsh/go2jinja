import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="chatml.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_chatml(file: str):
    run_test("chatml", file)
