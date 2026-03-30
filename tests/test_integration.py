from app.calculator import health_check


def test_health_check_contract():
    result = health_check()

    assert result["status"] == "ok"
    assert result["service"] == "calculator"