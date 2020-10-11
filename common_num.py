def common_elements(l1, l2):
    common = []
    for i in l1:
          if i in l2:
              common.append(i)
    return common

print(common_elements([1, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))   
