import sys

days = int(sys.argv[1])
miles = int(sys.argv[2])
receipts = float(sys.argv[3])

MAX_DAYS = 14
MAX_MILEAGE = 1000
MAX_RECEIPTS = 2500

days_capped = min(days, MAX_DAYS)
miles_capped = min(miles, MAX_MILEAGE)
receipts_capped = min(receipts, MAX_RECEIPTS)

if days_capped <= 7:
    per_diem_total = 105 * days_capped
else:
    per_diem_total = 105 * 7 + 75 * (days_capped - 7)

MILEAGE_RATE = 0.42
mileage_total = MILEAGE_RATE * miles_capped if miles_capped > 50 else 0

if receipts_capped <= 500:
    receipts_total = 0.75 * receipts_capped
else:
    receipts_total = 0.75 * 500 + 0.12 * (receipts_capped - 500)

reimbursement = per_diem_total + mileage_total + receipts_total

MAX_TOTAL = 4000
reimbursement = min(reimbursement, MAX_TOTAL)

print(f"{reimbursement:.2f}")