import random
count = 0
start = 1
end = 100
start = int(start)
end = int(end)
r = random.randint(start, end)
while True:
	number = input('请猜数字：')
	count += 1
	number = int(number)
	if r == number:
		print('恭喜您猜中了！')
		print('你第', count, '次猜中！')
		break
	elif number < r:
		print('第', count, '次，您猜的数字比正确答案小')
	elif number > r:
		print('第', count, '次，您猜的数字比正确答案大')
	else:
		print('您只能输入数哦！')
	