def calculate_client_commission(discount: bool) -> float:
    """ Calculate the commission for a client.

    Parameters:
    - isClient (bool): Indicates whether the customer is a client or not.

    Returns:
    - float: The commission amount.
    """
    commission_rates = {
        True: 5,
        False: 7
    }
    return commission_rates[discount]