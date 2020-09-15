def translator(num):
    persian_numbers = '۱۲۳۴۵۶۷۸۹۰'
    english_numbers = '1234567890'
    arabic_numbers = '١٢٣٤٥٦٧٨٩٠'
    for c in num:
        if c in persian_numbers:
            num = num.replace(c, english_numbers[persian_numbers.index(c)])
        if c in arabic_numbers:
            num = num.replace(c, english_numbers[arabic_numbers.index(c)])
    return num


print(translator("١٢٣٤٥٦٧٨٩٠"))
print(translator('۱۲۳۴۵۶۷۸۹۰'))
