# Add Products Details 
class Product :
	def __init__(self,name, category, price,stock) :
		self.name = name
		self.category = category 
		self.price = price
		self.stock = stock
		

# Added Product Info				
	def product_info(self) :
		print (f"Name : {self.name}")
		print (f"Category : {self.category}")
		print (f"Price : {self.price}")
		print (f"Total Stock : {self.stock}")
		

# Edit/Update ! Stocks				
	def update_stock(self,qty) :
		if self.stock + qty < 0 :
			return False
		self.stock += qty
		return True
		

# Add Discount Or Deal	
	def discount(self, percentage) :
		discount_amount = self.price * (percentage / 100)
		self.price -= discount_amount
		
		
		
# Store Management Area		
class Store :
	def __init__(self) :
		self.products = []
		
# Like Store employee/Helper	
	def store_helper(self,name) :
		for product in self.products :
			if product.name == name :
				return product 
		return None
		
		
# Add Products 
	def add_products(self, product) :
		self.products.append(product)
		print (f"✅ Product '{product.name}' Added")
		
		
# Remove Products		
	def remove_products(self,name) :
		product = self.store_helper(name) 
		if product :
			self.products.remove(product)
			print (f"✅ Product {name} Successfully Deleted")
		else :
			print (f"product {name} Not Found")
			
			
# Search Products			
	def search_products(self,name) :
		product = self.store_helper(name) 
		if product :
			print ("Product Found")
			product.product_info()
		else :
			print (f"❌ Product {name} Not Found")
			
			
# seen All Products 			
	def show_products(self) :
		if not self.products :
			print ("Not Any Product Yet")
			return 
			
		for i, product in enumerate (self.products,start = 1) :
			print (f"{i} : Name :  {product.name}")
			print (f"Category  {product.category}")
			print (f"Price  : {product.price}")
			

# Store Data Save To Text File		
	def save_file(self) :
		with open("store_data.txt","w") as f :
			for product in self.products :
				line = f"{product.name},{product.category},{product.price},{product.stock}\n"
				f.write(line)
				
	
# Load Store Data Text File	
	def load_file(self) :
		try :
			with open("store_data.txt","r") as f :
				for line in f :
					name, category, price, stock = line.strip().split(",")
					product = Product(name, category, float(price),int(stock))
					self.products.append(product)
		except FileNotFoundError :
			pass
			
				
		
# Program Brain 🧠		
def main() :
	store = Store()
	store.load_file()
	while True :
		print ("- - - - - - Mini Store System - - - - - -")
		print ("1 Add Products")
		print ("2 Remove Products")
		print ("3 Search Products")
		print ("4 Show All Products")
		print ("5 Update Stock")
		print ("6 Apply Discount")
		print ("0 Exit..")
		choice = input("Enter Choice ")
		
		
# Add Products Input		
		if choice == "1" :
			name = input("Enter Product Name : ")
			category = input("Enter Product Category : ")
			
			try :
				price = int(input("Enter Product Price : "))
				stock = int(input("Enter Product Stock : "))
				product = Product(name, category,price,stock)
				store.add_products(product)
			except ValueError :
				print ("Make Sure Price & Stock Digits")
		
		
# Remove Products By Name		
		elif choice == "2" :
			name = input("Enter Product Name : ")
			store.remove_products(name)
			
		
# Search Products By Name		
		elif choice == "3" :
			name = input("Enter Destinated Product Name : ")
			store.search_products(name)
			
		
# Show All Products	
		elif choice == "4" :
			store.show_products()
			
			
# Stock Update 			
		elif choice == "5" :
			name = input("Enter Product NameYou Want Update Stock : ")
			try :
				qty = int(input("Enter Quantity "))
				product = store.store_helper(name)
				if product :
					found = product.update_stock(qty)
					if found :
						print (f"✅ Stock Update for {name}")
					else :
						print (f"❌ Nor Enough Stock : 0 Stock Not Allowed")
				else :
					print (f"❌ Product Not Found")
			except ValueError :
				print ("❌ Qty Must Be A digits")
				
				
# Applying Discounts				
		elif choice == "6" :
			name = input("Enter Product Name You Want A Discount : ")
			try :
				percentage = float(input("Enter Discount Percentage : "))
				product = store.store_helper(name) 
				if product :
					product.discount(percentage)
					print (f"✅ Discount Applied {name}")
				else :
					print ("❌ Product Not Found ")
			except ValueError :
				print ("❌ Discount Must Be A Number")
				
				
				
		elif choice == "0" :
				store.save_file()
				print ("Program Exited")
													
		
if __name__ == "__main__" :
		main()		
		
	
			