"""
Task 3: Tim Tams

Daniel likes tim tams ... there's a packet of 11, he eats two at a time
until there's only one left.

Please print this out.

Some variable: name, number_of_tim_tams
"""
i = 11  # name it numberOfTimTams
i = len(sorted([i for i in range(1, 11)], reverse=True))

# timTams = 0

# SaifHasWrittenSomeCode
# saifHasWrittenSomeCode
# saif_has_written_some_code

print('Daniel has 11 Tim Tams')
while i > 1:
    print('Tim Tam Counter')
    print(i)
    print('Daniel eats two Tim Tams')
    if i % 2 == 0:  # is it an even number?
        print("Quick check:", i)
        i += 4
    i -= 2
    if i > 200:
        break  # jump out of the loop
print('1 Tim Tam Remains')
print('FINISH IT')
