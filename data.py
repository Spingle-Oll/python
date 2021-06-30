import datetime
my_datetime = datetime.datetime.now()
F = my_datetime.strftime("%d %b")

print(F)

my_datetime = datetime.datetime.now()
F = my_datetime.strftime("%H:%M")
print(F)