#!/bin/bash
trip_duration_days=$1
miles_traveled=$2
total_receipts_amount=$3

result=$(python3 reimburse.py "$trip_duration_days" "$miles_traveled" "$total_receipts_amount")
echo "$result"
