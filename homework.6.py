my_dict = {
    'Mike': 1986, 'Uma': 2015
}
print(my_dict)
print(my_dict.get('Mike'))
print(my_dict.get('mike'))
my_dict.update({
    'Alice': 2001,
    'Bob': 20012
})
print(my_dict)
a = my_dict.pop('Alice')
print('Deleted value: ',a)
print(my_dict)
my_set = {1,1,1,1,1,2,3,3,4,5,56,76,78,8,90,'Hello', True, 12}
print(my_set)
my_set.add('cherry')
my_set.add(22)
my_set.discard('Hello')
print(my_set)