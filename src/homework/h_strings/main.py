import strings

on = True
while on:
    print('')
    print('1 - Hamming Distance')
    print('2 - DNA compliment')
    print('3 - Exit')
    print('')
    select = int(input(''))
    if select == 1:
        hammingDistanceMenu = True
        while hammingDistanceMenu == True:
            print('')
            dna1 = input('Enter the first DNA string: ')
            dna2 = input('Enter the second DNA string: ')
            print('')
            hamming = strings.get_hamming_distance(dna1, dna2)
            if hamming == "ERROR":
                print('Error: The DNA strings must be the same length.')
            else:
                print('The hamming distance between those DNA strings is: '+str(hamming))
                hammingDistanceMenu = False
    elif select == 2:
        dnaComplimentMenu = True
        while dnaComplimentMenu ==True:
            print('')
            dna = input('Enter a DNA string: ')
            print('')
            print('The compliment to that DNA string is: '+str(strings.get_dna_compliment(dna)))
            dnaComplimentMenu = False
    elif select == 3:
        exitMenu = True
        while exitMenu == True:
            print('')
            confirmation = (input('Are you sure you would like to quit? y/n: ').upper())
            if confirmation == 'Y' or confirmation == 'YES':
                on = False
                exitMenu = False
            elif confirmation == 'N' or confirmation =='NO':
                exitMenu = False