import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="granite-instruct.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_granite_instruct(file: str):
    run_test("granite-instruct", file)
