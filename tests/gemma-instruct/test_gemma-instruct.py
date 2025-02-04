import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="gemma-instruct.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_gemma_instruct(file: str):
    run_test("gemma-instruct", file)
