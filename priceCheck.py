def priceCheck(products, productPrices, productSold, soldPrice):
    if (dataCheck(products, productPrices, productSold, soldPrice) == False):
        return -1
    saleErrors = 0
    avlblProdct = dict(zip(products, productPrices))
    
    for i in range(len(productSold)):
        if avlblProdct.get(productSold[i]) != soldPrice[i]:
            saleErrors += 1

    return saleErrors

def dataCheck(products, productPrices, productSold, soldPrice):
    if (len(products) != len(productPrices)) or (len(productSold) != len(soldPrice)):
        return False

    for product in productSold:
        if product not in products:
            return False

    if (len(products) > 99 or len(products) < 1) or (len(productSold) > 99 or len(productSold) < 1):
        return False

    for price in productPrices:
        if price < 1 or price > 100000:
            return False
          
    for price in soldPrice:
        if price < 1 or price > 100000:
            return False

    return True
        
