LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934


def convert_to_litres_per_100_km(mpg):
    x = (mpg * KMS_PER_MILE)**(-1)
    return x * LITRES_PER_GALLON * 100


print(convert_to_litres_per_100_km(32))
print(convert_to_litres_per_100_km(0))
