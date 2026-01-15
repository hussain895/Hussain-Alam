account_number = "NYC1045689"

region_code = account_number[0:3]
branch_code = account_number[3:5]
customer_number = account_number[5:]

print("Account Number : " , account_number)
print("Region Code  : " , region_code)
print("Branch Code : " , branch_code)
print("Customer Number : " , customer_number)
print()


accounts = [
    "NYC1045689",
    "NYC2041234",
    "LAX1049876",
    "NYC1056789"
]

print("Accounts in NYC Region")
for acc in accounts:
    if acc[0:3] == "NYC":
        print(acc)
print()

print("Accounts in Branch 10 ")
for acc in accounts:
    if acc[3:5] == "10":
        print(acc)