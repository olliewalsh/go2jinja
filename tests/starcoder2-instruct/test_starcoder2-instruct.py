import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE = "starcoder2-instruct.gotmpl"


@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_starcoder_instruct(file: str):
    run_test("starcoder2-instruct", file)
