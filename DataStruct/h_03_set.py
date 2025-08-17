# Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
# Months={"Jan","Feb","Mar"}
# Dates={21,22,17}
# print(type(Days))
# print(Days)
# print(type(Months))
# print(Months)
# print(type(Dates))
# print(Dates)
#
# Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
#
# Days.add("Sun")
# print(Days)


# Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
#
# Days.discard("Sun")
# print(Days)

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA&DaysB
print(AllDays)