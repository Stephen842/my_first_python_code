def leap(year):
     if year % 4 != 0:
          return False
     elif year % 100 != 0:
          return True
     elif year % 400 != 0:
          return False
     else:
          return True

yr_data = [2000, 2005, 2006, 2010, 1900, 2020, 2022, 2024]
yr_result = [False, True, True, False, False, True, True, False]

for i in range(len(yr_data)):
     yr = yr_data[i]
     print(yr, "-> ", end="")
     result = leap(yr)
     if result == yr_result[i]:
          print("ok")
     else:
          print("failed")
