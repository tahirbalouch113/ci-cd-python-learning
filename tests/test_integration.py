import pytest
from app.calculator import health_check


@pytest.mark.integration
def test_health_check_contract():
    result = health_check()

    assert result["status"] == "ok"
    assert result["service"] == "calculator"