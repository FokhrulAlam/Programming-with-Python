#A company has determined that its annual profit is typically 23 percent of total sales.
#Write a program that asks the user to enter the projected amount of total sales, and then displays the profit that will be made from that amount.
#Hint: Use the value 0.23 to represent 23 percent.

total_sales=float(input("Please enter the total annual sale: "))

profit=total_sales*(23/100)

print("Profit= $"+format(profit,",.2f"))
