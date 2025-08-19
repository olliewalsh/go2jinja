import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE = "command-r.gotmpl"


@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_command_r(file: str):
    run_test("command-r", file)
