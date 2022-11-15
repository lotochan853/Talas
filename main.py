import argparse

# products_detail
products_info = {
    "T-shirt":{"Item price":30.99,"Shipped from":"US","Weight":0.2},
    "Blouse":{"Item price":10.99,"Shipped from":"UK","Weight":0.3},
    "Pants":{"Item price":64.99,"Shipped from":"UK","Weight":0.9},
    "Sweatpants":{"Item price":84.99,"Shipped from":"CN","Weight":1.1},
    "Jacket":{"Item price":199.99,"Shipped from":"US","Weight":2.2},
    "Shoes":{"Item price":79.99,"Shipped from":"CN","Weight":1.3}
}

# shipping_rate_detail
shipping_rates = {
    "US":2,
    "UK":3,
    "CN":2
}

# VAT_detail
vat_rate = 0.14

def calculate_original_total_price(products_purchase:[]):
    # calculate all the product original price,shipping,vat without discount
    Subtotal = 0 # init Subtotal
    Shipping = 0 # init Shipping

    # iter the products_purchase
    for product in products_purchase:
        if products_info.get(product):
            Subtotal += products_info[product]["Item price"]
            Shipping += products_info[product]["Weight"] *10 * shipping_rates[products_info[product]["Shipped from"]]
        else:
            raise ValueError("No Such Product:{}".format(product))
    # calculate the vat
    VAT = Subtotal * 0.14
    return Subtotal,Shipping,VAT



def discount_shoes(products_purchase:[]):
    # check if Shoes in products_purchase
    if "Shoes" in products_purchase:
        if products_info.get("Shoes"):
            discount_price = products_info["Shoes"]["Item price"] * 0.1
            return {"discount_item":"10% off shoes","discount_price":discount_price,"type":0} # type=0 -> discount is product price
        else:
            raise ValueError("No Such Product:{}".format("Shoes"))
    else:
        return {}

def discount_jacket(products_purchase:[]):
    # check if jacket in products_purchase
    if "Jacket" in products_purchase:
        tops_num = 0 # init top_nums
        jacket_num = 0 # init jacket_nums

        # iter products_purchase
        for product in products_purchase:
            if product == "T-shirt" or product == "Blouse":
                tops_num += 1
            if product == "Jacket":
                jacket_num += 1

        # tops_num >= 2 ,can get the discount
        if tops_num >= 2:
            if tops_num // 2 >= jacket_num:
                if products_info.get("Jacket"):
                    discount_price = products_info["Jacket"]["Item price"] * 0.5 * jacket_num
                    return {"discount_item": "50% off jacket", "discount_price": discount_price, "type": 0}# type=0 -> discount is product price
                else:
                    raise ValueError("No Such Product:{}".format("Jacket"))
            else:
                if products_info.get("Jacket"):
                    discount_price = products_info["Jacket"]["Item price"] * 0.5 * tops_num // 2
                    return {"discount_item": "50% off jacket", "discount_price": discount_price, "type": 0}# type=0 -> discount is product price
                else:
                    raise ValueError("No Such Product:{}".format("Jacket"))
        else:
            return {}

    else:
        return {}

def discount_2items(products_purchase:[]):
    # check if purchase more than two products
    if len(products_purchase) >= 2:
        return {"discount_item": "$10 of shipping", "discount_price": 10, "type": 1}# type=0 -> discount is shipping price
    else:
        return {}


def main_calculate(products_purchase:[]):
    # main function to calculate the total price
    if len(products_purchase) == 0:
        raise ValueError("No Product")


    # step 1: calculate the original total price
    Subtotal,Shipping,VAT = calculate_original_total_price(products_purchase)
    Original_Subtotal = Subtotal
    Original_Shipping = Shipping
    Original_VAT = VAT

    # step 2: check the discount
    discount_list = []
    if discount_shoes(products_purchase):
        discount_list.append(discount_shoes(products_purchase))
    if discount_jacket(products_purchase):
        discount_list.append(discount_jacket(products_purchase))
    if discount_2items(products_purchase):
        discount_list.append(discount_2items(products_purchase))
    if len(discount_list) >0:
        for discount_item in discount_list:
            if discount_item["type"] == 0:
                Subtotal -= discount_item["discount_price"]
            elif discount_item["type"] == 1:
                Shipping -= discount_item["discount_price"]
                if Shipping < 0 :
                    Shipping = 0

    # setp 3: calculate total price
    Total = Subtotal + Shipping + VAT

    print(f"Subtotal:${round(Original_Subtotal,4)}")
    print(f"Shipping:${round(Original_Shipping,4)}")
    print(f"VAT:${round(Original_VAT,4)}")
    if discount_list:
        print(f"Discounts:")
        for discount_item in discount_list:
            print(f"\t{discount_item['discount_item']:}-${round(discount_item['discount_price'],4)}")
    print(f"Total:${round(Total,4)}")

    return Subtotal,Shipping,VAT,discount_list,Total

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="createCart")
    parser.add_argument('--product', help="product name",action='append')
    args = parser.parse_args()
    main_calculate(args.product)
