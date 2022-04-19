import sys
import untils

char = sys.argv[1]
kurs, date_value = untils.currency_rates_adv(char)
print(kurs, date_value)