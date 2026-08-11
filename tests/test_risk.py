import pytest


from app.risk import calculate_pnl, calculate_exposure, calculate_var


def test_calculate_pnl():
    result = calculate_pnl(1.10, 1.08, 1_000_000)

    assert result == pytest.approx(20_000)


def test_calculate_exposure():
    result = calculate_exposure(1.10, 1_000_000)

    assert result == pytest.approx(1_100_000)


def test_calculate_var():
    result = calculate_var(1_100_000, 0.02)

    assert result == pytest.approx(51_260)
