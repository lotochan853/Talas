#How to use？  

##1.Custom the data.  

User can load their data of product from any data source and transform the data into the dict,eg:  

'''python
products_info = {"Product_1":{"Item price":xxx,"Shipped from":“xx”,"Weight":xx}...} # must be use the products_info  
'''  

User can load data of shipping from any data source and transform the data into the dict,eg:  

'''python
shipping_rates = {"Country":xxx,...} # must be use the shipping_rates  
'''  
 
##2.Custom the discount method  

User can custom the discount method,eg:  

'''python
def custom_method(products_purchase:[]):
    discount_detail...  
    if get the discount:  
        return {"discount_item":xxx,"discount_price":xxx,"type":x} type-> 0:discount is product price;1:discount is shipping price  
    else:  
        return {}  
'''  

Add the method to the function:main_calculate step 2:  
'''python
def main_calculate():  
    #setp 1:  
    ...  
    #setp 2:  
    if custom_method(products_purchase):  
        discount_list.append(custom_method(products_purchase))  
    ...  
'''
  
##3.Run the programmer  
Use the terminal and input the command: python createCart.py --product "Shoes" --product "T-shirt" ...  
