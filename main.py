# A furniture renting store has asked you to create a program that calculates the rental costs. The store rents several types of furniture.
# Furniture is rented monthly.
# 1. A minimum fee (usually higher than monthly cost) is charged for the first month.
# 2. After the first month, the store charges a monthly rental fee.
# 3. There is a maximum charge for any given year.
# 4. The program takes furniture selection and number of months as input. It
# calculates and prints the charge.
# 5. Input validation: the program validates the input for furniture selection (1-5) and
# numbers of months (greater than 0).


print("Please select from the following menu:\n1. Sofa,\n2. Loveseat,"
		"\n3. 4 Post Bed,\n4. Dresser,\n5. Kitchen Table")

while True:
	try:
		selection = int(input("\nEnter furniture selection: "))
		if selection >= 1 and selection <= 5:
			break
		else:
			print("\nPlease, select a number between 1 and 5! Try again...")
	except:
		print("\nInvalid number! Try again...")

# print(f"You have selected: {selection}")

while True:
	try:
		months_rented = int(input("\nEnter months rented: "))
		if months_rented > 0:
			break
		else:
			print("\nEnter a number greater than 0! Try again...")
	except:
		print("\nInvalid number! Try again...")

# print(f"You have entered: {months_rented}")



# helper function to calculate the total cost
def total_calc(months, base_charge, monthly, yearly_max):

	total_charge = base_charge
	
	if months <= 12:
		total_charge += months * monthly
		if total_charge > yearly_max:
			return yearly_max
		else:
			return total_charge
	else:
		# cost over the first year
		total_charge += 11 * monthly
		# if that cost exceed the max, it is set to max
		if total_charge > yearly_max:
			total_charge = yearly_max
		# let's get the cost of the months not representing the whole year
		left_over_year = (months)%12
		left_charge = left_over_year * monthly
		if left_charge > yearly_max:
			total_charge += yearly_max
		else:
			total_charge += left_charge
		# now let's get the costs in each year
		number_of_years_except_first = (months - 12)//12
		yearly_costs = 12 * monthly
		# check if the yearly costs exceed the max
		if yearly_costs > yearly_max:
			total_charge += yearly_max * number_of_years_except_first
		else:
			total_charge += yearly_costs * number_of_years_except_first

		return total_charge


# now let's check the selection
total_charge = 0
if selection == 1:
	total_charge = total_calc(months_rented,60, 45, 450)
elif selection == 2:
	total_charge = total_calc(months_rented, 45, 30, 280)
elif selection == 3:
	total_charge = total_calc(months_rented, 55, 38, 350)
elif selection == 4:
	total_charge = total_calc(months_rented, 28, 25, 200)
else:
	total_charge = total_calc(months_rented, 35, 20, 220)

print(f"\nAmount due ($): {total_charge}")


