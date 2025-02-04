import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="chatqa.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_chatqa(file: str):
    run_test("chatqa", file)
