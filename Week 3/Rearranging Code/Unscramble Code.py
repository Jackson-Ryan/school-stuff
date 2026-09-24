def is_eligible(reserved, renewals, limit):
    return not reserved and renewals < limit

reserved = False
limit = 3
renewals = 2

if is_eligible(reserved, renewals, limit):
    print("Renewal Allowed")