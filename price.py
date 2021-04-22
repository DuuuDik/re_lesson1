def discounted(price, discount, max_discount = 50):
    if isinstance(price, (int, float)) != True or isinstance(discount, (int, float)) != True or isinstance(max_discount, (int,float)) != True:
        print(f'Значение цены или скидки приведено в неправильном формате!')
    else:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Максимальная скидка не может быть больше 99%')
        if discount >= max_discount:
            price_with_discount = price
        else:
            price_with_discount = price*(1-discount/100)
        return price_with_discount

product = {
    'name': 'Samsung Galaxy S10',
    'stock': 8, 
    'price': 50000.0,
    'discount': 80
}

print(discounted(100, 50, 40))
print(discounted(100,60))
print(discounted(100, 100, 100))

'''
p=discounted(200, 50)

print(p)
discounted(300,-20)
discounted(-100, 20)
discounted('hello', 20)
'''
