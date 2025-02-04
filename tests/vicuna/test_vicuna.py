import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="vicuna.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_vicuna(file: str):
    run_test("vicuna", file)
