def get_vat (payment, percent=18):
    try:
        payment = float(payment)
        percent = int(percent)
        vat = payment / 100 * percent
        vat = round(vat, 2)
        return "Sum VAT: {}".format(vat)
    except (TypeError, ValueError):
        return "Try again"
result = get_vat (100, 10)
print(result)