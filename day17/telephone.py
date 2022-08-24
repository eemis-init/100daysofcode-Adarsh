import sys

for line in sys.stdin:
    raw_phone_number = line.strip()
    country_code=line[:3]
    first_three=line[3:6]
    remaining=line[6:]
    print(f'({country_code}) {first_three}-{remaining}')