"""product={"SAMSUNG","REDMI","VIVO","VIVO"}
print(type(product))
product_2={"XIOMI","OPPO","SAMSUNG","LG"}
print(product)
print(product_2)
print(product.intersection(product_2))
print(product.union(product_2))
print(product.difference(product_2 ))
product.add("ONEPLUS")
print(product)
product.remove("ONEPLUS")
print(product)"""

"""product={"SAMSUNG","REDMI","VIVO","VIVO"}
product_2={"XIOMI","OPPO","SAMSUNG","LG"}
product_3={"SAMSUNG"}
product.intersection_update(product_2,product_3)
print(product)
print(product.difference_update(product_2))
print(product)"""

s={10,20,30,40}
s.add(100)
print(s)
s=frozenset(s)"""stagnent"""
s.add(15)

