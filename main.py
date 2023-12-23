import sys
print("Welcome to the tip calculator!")

bill = input("Enter the total amount of the bill: ")

changetype_bill =float(bill)

tip = input("Enter the tip percentage: ")

changetype_tip = float(tip)

print(f"Your bill is {changetype_bill} and your tip is {changetype_tip}")

proceed = input("Do you want to proceed? Y or N: ")

if proceed.lower() == "y":
  tip_amount = changetype_bill * (changetype_tip/100)
  total_bill_withtip = changetype_bill + tip_amount
  share = input("How many people are splitting the bill? ")
  share_bill = round((total_bill_withtip/int(share)),2)
  print(f"Bill per person is {share_bill}")
      

else:
  print("proceed from start")
  sys.exit()