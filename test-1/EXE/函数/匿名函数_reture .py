# 可写函数说明
def new_sum( arg1, arg2 ):
   # 返回2个参数相加."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total

# 调用sum函数
total = new_sum( 10, 20 )
print ("函数外 : ", total)
print(sum([1,2],3))