def calculate_commission(isClient: bool) -> float:
    """ Calculate the commission for a client.

    Parameters:
    - isClient (bool): Indicates whether the customer is a client or not.

    Returns:
    - float: The commission amount.
    """
    if isClient:
        return 2.5
    else:
        return 5