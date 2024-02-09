import decisions
    
options = input ('Enter Options: ')
total = input ('Enter Total: ')
result = decisions.get_options_ratio(float(options),float(total))
rating = decisions.get_faculty_rating(result)
print(rating)