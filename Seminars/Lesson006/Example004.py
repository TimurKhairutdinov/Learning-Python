





lst = list(map(int, input("Введите числа через пробел:\n").split()))
def return_unique(lst):
  return [i for i in lst if lst.count(i)==1]
print(f"Список из неповторяющихся элементов: {return_unique(lst)}")
