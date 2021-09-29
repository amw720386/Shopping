Solution For: 

Project description:
Write a Python program to process the shopping list. You need to buy these items from the cheapest store.

Input:
input_data.txt (use input_data.txt in repository)
shopping.txt
  Old shopping.txt:
    3 items on my shopping list:
    3 Butter
    4 Orange
    5 Eggs

Output:
Order details:
3 Butter @ 1.99		$ 5.97
4 Orange @ 4.00		$16.00
5 Eggs   @ 1.00		$ 5.00
Total				$26.97

In this example 
	Butter should be purchased from Values Mart. Because it is $1.99. In other stores, its expensive
	Orange should be purchased from Canadian Tires. Because it is $4.00. In other stores, its expensive
	Egg should be purchased from Canadian Tires. Because it is $1.00. In other stores, its expensive

Hint:
Save the input_data.txt file in the folder where your .py file is.
Save the shopping.txt file in the folder where your .py file is.

From your python program, read this file and store it in a list/dictionary etc..
create a store_dictionary  
create a city_dictionary
Try to store your data like below

store_dictionary = {'Walmart':'Brampton':[[Orange,5,$4.80],[Bread,10,$2.99],[Butter,20,$3.99],[Milk,20,$2.25],[Eggs,100,$1.50]],.... }
	
Once you create the store dictionary, read shopping.txt
loop through the shopping. check each item in the shopping list in the store_dictionary to find the cheapest. 

Project improvement 1: Buying from multiple stores

Change your program to handle the below situation.
No changes to input file.
Shopping file changed. Use attached shopping.txt now

Check your shopping cart now. 
You are buying 8 Butter now. Butter is cheap at Values Mart, but you don't have 8 Butter. So what will you do?
In this situation, you will need to by 5 from Values Mart and another 3 from different store(with next cheapest price. In this example, it is Canadian Tires)

Same with Orange. Now you have to by 22. 5 from Canadian Tires, 15 from Values Mart and 2 from Walmart.

(Use shopping.txt in repository)
  
Project Improvement 2:
Reduce the quantities from the stores when purchasing.

So, you need to print all stores and there products. Quantity in the stores is reduced now.
