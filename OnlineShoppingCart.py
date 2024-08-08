class ItemToPurchase:
    #attributes
    item_name = ""
    item_price = 0.0
    item_quantity = 0

    def __init__(self):
        self.item_name = "none"
        self.item_price =  0
        self.item_quantity = 0
    
    def print_item_cost(self):
        unformatted_cost = self.item_quantity * self.item_price
        cost = "${:,.2f}".format(unformatted_cost)
        price = "${:,.2f}".format(self.item_price) 
        print(self.item_name + " " + str(self.item_quantity)  + " @ " + price +" = "  +cost)
        return unformatted_cost

if __name__=="__main__":
    item_list = []
    max_items = 2
    for x in range(max_items):
        item = ItemToPurchase()
        item.item_name = input("Please enter a product name: ")
        item.item_price = float(input("Please enter a dollar amount for this product: "))
        item.item_quantity = int(input("Please enter a quatity for this item: "))
        item_list.append(item)

    print("TOTAL COST")
    total = 0.0
    for item in item_list:
        total += item.print_item_cost()

    total = "${:,.2f}".format(total)
    
    print(total)