my_set = set()
groceries = ['chicken', 'chicken', 'chicken']
print(groceries[1])
'''
What is a set in comparison to a list? 
- A set is unordered
- A set is also mutable
    .add() .remove()
- The values in a set all have to be unique
- No indexing. 
'''

# list vs set
# arr = [{'blueberries', 'pineapple'}]
# print(arr)
# test_set = {{'blueberries', 'pineapple'}, 'strawberries'}
# print(test_set)

# for g in groceries: 
#     print(g)

groceries_week_1 = {'chicken', 'eggs', 'bbq sauce', 'spinach', 'beef'}
groceries_week_2 = {'chicken', 'eggs', 'bbq sauce', 'spinach', 'Ice cream'}
groceries_week_3 = {'chicken', 'eggs', 'bbq sauce', 'spinach'}
# groceries.add('Ice Cream')
# groceries.remove('spinach')
# issubset()
# issuperset()
# print(groceries_week_1.issuperset(groceries_week_3))
print(groceries_week_3.issubset(groceries_week_1))
#     <set running method>.<method>(<What we're checking against>)


'''
union()
    - Combines two sets together
intersection()
    - It combines the values in sets that are the same
difference()
    - It shows the different values between set 1 in comparison to set 2
    - set1.difference(set2)
symmetric_difference()
    - It shows the different values from both sets no matter the order.
'''

groceries_week_1 = {'chicken', 'eggs', 'bbq sauce', 'spinach', 'beef'}
groceries_week_2 = {'chicken', 'eggs', 'bbq sauce', 'spinach', 'Ice cream'}
groceries_week_3 = {'chicken', 'eggs', 'bbq sauce', 'spinach', 'Broccoli'}

my_union = groceries_week_2.union(groceries_week_3)
# print(groceries_week_1.difference(groceries_week_2.union(groceries_week_3)))
# print(groceries_week_1.intersection(groceries_week_2))
# print(groceries_week_1.symmetric_difference(groceries_week_2))


arr = ['chicken', 'pork', 'cereal', 'candle', 'candle', 'candle']
my_set = set(arr)
print(arr)
print(my_set)
