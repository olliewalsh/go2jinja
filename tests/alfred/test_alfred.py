import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="alfred.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_alfred(file: str):
    run_test("alfred", file)
