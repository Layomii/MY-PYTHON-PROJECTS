import bitly_api

BITLY_ACCESS_TOKEN = "ACCESS_TOKEN"

b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

response = b.shorten('https://www.topuniversities.com/university-rankings/university-subject-rankings/2019/law-legal-studies')
print(response)