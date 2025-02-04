import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="llama3-instruct.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_llama3_instruct(file: str):
    run_test("llama3-instruct", file)
