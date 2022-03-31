import phonenumbers
from numTest import number

from phonenumbers import geocoder

ch_num = phonenumbers.parse(number,"CH") # C - > country , H -> History
print("Country : ")
print(geocoder.description_for_number(ch_num,'en'))

from phonenumbers import carrier
service_num = phonenumbers.parse(number,'RO')
print("SIM name :")
print(carrier.name_for_number(service_num,'en'))
