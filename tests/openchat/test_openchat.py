import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE = "openchat.gotmpl"


@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_openchat(file: str):
    run_test("openchat", file)
