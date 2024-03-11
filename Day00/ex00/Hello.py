ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
# your code here

# list
ft_list[1] = 'World'

# tuple
tmp_list = list(ft_tuple)
tmp_list[1] = 'Morroco'
ft_tuple = tuple(tmp_list)

# set
ft_set.remove('tutu!')
ft_set.update({'Khouribga'})
# ft_set.add({'Khouribga'})

# dict
ft_dict['Hello'] = '1337'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
