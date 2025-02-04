import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE = "codellama-70b-instruct.gotmpl"


@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_codellama_70b_instruct(file: str):
    run_test("codellama-70b-instruct", file)
