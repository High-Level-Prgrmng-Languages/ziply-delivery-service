

def validate_name(*names):
    """
    checks if first is valid, if not coalesces to the next
    returns valid string or null if not valid
    """
    for name in names:
        if isinstance(name, str) and name.strip:
            return name.strip()
    return None


def validate_status(*status):
    for status in status:
        if status:
            return status
    return None


def validate_address(*addresss):
    for address in addresss:
        if address:
            return address
    return None


def validate_date(*dates):
    for date in dates:
        if date:
            return date
    return None
