import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="mistral-instruct.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_mistral_instruct(file: str):
    run_test("mistral-instruct", file)
