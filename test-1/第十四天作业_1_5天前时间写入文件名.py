import datetime
five_days_before = datetime.datetime.now() - datetime.timedelta(days=5)
format_five_days_before = five_days_before.strftime("%Y-%m-%d %H:%M:%S")
str_five_days_before = str(format_five_days_before)
file_name = 'save_fivedaysago_time ' + str_five_days_before + '.txt'
file = open(file_name,'w')
file.write(str_five_days_before)
file.close()

# if __name__ == '__main__':
#     print(file_name)
#     print(file)
#     pass



