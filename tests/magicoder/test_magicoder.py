import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="magicoder.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_magicoder(file: str):
    run_test("magicoder", file)
