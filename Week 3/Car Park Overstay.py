def is_overstayed(minutes, is_permit_holder):
    if minutes > 30:
        overstay_fee = round(minutes / 10)
        overstay_fee = overstay_fee * 1.5
        if is_permit_holder:
            overstay_fee = 0
        print("Overstay Fee: £", overstay_fee)
        return True
    else:
        return False

def ticket_book()