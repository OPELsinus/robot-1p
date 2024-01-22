import datetime

# today = datetime.date.today()
#
# quarters = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#
# month = today.month
# day = today.day
# year = today.year
#
# range_to_load = []
#
# for ind, quarter in enumerate(quarters):
#     if month in quarter and month == quarters[ind][0]:
#
#         if month == 1:
#             range_to_load.append(datetime.date(year - 1, quarters[ind - 1][0], 1).strftime('%Y-%m-%d'))
#             range_to_load.append((datetime.date(year, 1, 1) - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
#         else:
#             range_to_load.append(datetime.date(year, quarters[ind - 1][0], 1).strftime('%Y-%m-%d'))
#             range_to_load.append((datetime.date(year, quarters[ind - 1][-1] + 1, 1) - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
# print(range_to_load)

