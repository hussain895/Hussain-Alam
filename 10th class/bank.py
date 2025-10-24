# Banking System - Account Number Information

# Example account number
account_number = "NYC1045689"

# Extract parts using indexing (subscript operator)
region_code = account_number[0:3]     # First 3 characters
branch_code = account_number[3:5]     # Next 2 characters
customer_number = account_number[5:]  # Remaining characters

# Display extracted details
print("Account Number:", account_number)
print("Region Code:", region_code)
print("Branch Code:", branch_code)
print("Customer Number:", customer_number)

# Example: Organizing multiple accounts
accounts = ["NYC1045689", "NYC1099988", "LAX2054321", "DAL3098765"]

# Sort and categorize by region and branch
region = input("\nEnter region code to filter (e.g., NYC): ").upper()
branch = input("Enter branch code to filter (e.g., 10): ")

print(f"\nAccounts in region '{region}' and branch '{branch}':")
for acc in accounts:
    if acc[0:3] == region and acc[3:5] == branch:
        print("-", acc)
