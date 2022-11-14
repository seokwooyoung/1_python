fruits = {'apple', 'banana', 'orange'}
fruits
#>> {'apple', 'banana', 'orange'}

fruits.add('mango')
fruits
#>> {'apple', 'banana', 'orange', 'mango'}

companies = set()
companies = {'apple', 'micro', 'google'}

type(fruits)
#>> <class 'set'>

type(companies)
#>> <class 'set'>

fruits & companies
#>> {'apple'}

fruits | companies
#>> {'apple', 'mango', 'google', 'micro', 'banana', 'orange'}

############################################
list_of_set =[fruits, companies]

# 교집합
set.intersection(*list_of_set)
#>> {'apple'}

# 합집합
set.union(*list_of_set)
#>> {'apple', 'mango', 'google', 'micro', 'banana', 'orange'}

#############################################

alphabet = list('google')
alphabet
#>> ['g', 'o', 'o', 'g', 'l', 'e']

# 원소의 순서 유지, 중복 없음
set(alphabet)
#>> {'l', 'e', 'g', 'o'}

# 집합끼리의 뺄셈
s1 = {1,2,3,4,5}
s2 = {1,3}
s1 - s2
#>> {2, 4, 5}
