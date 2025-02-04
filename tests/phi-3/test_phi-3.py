import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="phi-3.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_phi_3(file: str):
    run_test("phi-3", file)
