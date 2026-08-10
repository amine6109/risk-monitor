def calculate_pnl(current_price, initial_price, quantity):
    return (current_price - initial_price) * quantity


def calculate_exposure(price, quantity):
    return abs(price * quantity)


def calculate_var(exposure, volatility, confidence_factor=2.33):
    return exposure * volatility * confidence_factor