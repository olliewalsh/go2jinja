import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="llama2-chat.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_llama2_chat(file: str):
    run_test("llama2-chat", file)
