def LinearSearchProduct(productList,targetproduct):
  indices=[]
  for index,Product in enumerate(productList):         
   if Product==targetproduct:
      indices.append(index)
  return indices


Products=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
target2='apple'
result=LinearSearchProduct(Products,target)
print(result)