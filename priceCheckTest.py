from priceCheck import *

print("test 1: all products sold incorrect")
result = priceCheck(products=['rice', 'sugar', 'wheat', 'cheese'],
                    productPrices=[16.89, 56.92, 20.89, 345.99],
                    productSold=['rice', 'cheese'],
                    soldPrice=[18.99, 400.89])

if result == 2:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")

print("test 2: some products sold incorrect")
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [2.89, 3.29, 5.79],
                    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
                    soldPrice = [2.89, 2.99, 5.97, 3.29])

if result == 2:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")

print("test 3: all prices correct")
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [2.89, 3.29, 5.79],
                    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
                    soldPrice = [2.89, 2.89, 5.79, 3.29])

if result == 0:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")

print("test 4: incorrect data, non existant product")    
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [2.89, 3.29, 5.79],
                    productSold = ['eggs', 'eygs', 'cheese', 'milk'],
                    soldPrice = [2.89, 2.99, 5.97, 3.29])

if result == -1:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")

print("test 5: incorrect data, missing sale price")
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [2.89, 3.29, 5.79],
                    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
                    soldPrice = [2.89, 2.99, 5.97])

if result == -1:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")

print("test 6: incorrect data, missing product price")
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [2.89, 3.29],
                    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
                    soldPrice = [2.89, 2.99, 5.97, 3.29])

if result == -1:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")

print("test 7: incorrect data, illegal sale price")
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [2.89, 3.29, 5.79],
                    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
                    soldPrice = [0.89, 2.99, 5.97, 3.29])

if result == -1:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")
    
print("test 8: incorrect data, illegal product price")
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [0.89, 3.29, 5.79],
                    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
                    soldPrice = [2.89, 2.99, 5.97, 3.29])

if result == -1:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")

print("test 9: incorrect data, illegal product price")
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [100001, 3.29, 5.79],
                    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
                    soldPrice = [2.89, 2.99, 5.97, 3.29])

if result == -1:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")

print("test 10: incorrect data, illegal sale price")
result = priceCheck(products = ['eggs', 'milk', 'cheese'],
                    productPrices = [2.89, 3.29, 5.79],
                    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
                    soldPrice = [100001, 2.99, 5.97, 3.29])

if result == -1:
    print("result " + str(result) + " pass")
else:
    print("result " + str(result) + " fail")    
