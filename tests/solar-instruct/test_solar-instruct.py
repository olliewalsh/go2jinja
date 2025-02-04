import pytest

from tests.helper import run_test

GO_TEMPLATE_FILE="solar-instruct.gotmpl"

@pytest.mark.parametrize("file", ["empty.json", "simple.json"])
def test_solar_instruct(file: str):
    run_test("solar-instruct", file)
