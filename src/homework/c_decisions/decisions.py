def test_config():
    return True

def get_options_ratio(options, total):
    options = float(options)
    total = float(total)
    ratio = options/total
    # print (ratio)
    return (ratio)

def get_faculty_rating(ratio):
    if 0<=ratio<=0.59:
        rating = ('UNACCEPTABLE')
    elif 0.6 < ratio <0.7:
        rating = ('NEEDS IMPROVEMENT')
    elif 0.7 < ratio < 0.8:
        rating = ('GOOD')
    elif 0.8 < ratio < 0.9:
        rating = ('VERY GOOD')
    elif 0.9 <= ratio < 1:
        rating = ('EXCELLENT')
    else:
        rating =('ERROR')
    # print (rating)
    return rating
