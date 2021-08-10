class month_results:
	def __init__(self, month):
		 self.month = month
	
	base = {
	'Приход опоры': [0,'pos'],
	'Затраты опоры': [0,'neg'],
	'Затраты транспорт': [0,'neg'],
	'Курьер':[0,'neg'],
	'Офис':[0,'neg'],
	'Л/Б': [0,'pos']
	}

	def month_update(self):
		month_total = 0
		positions = self.base.keys()
		for position in positions:
			print('Ввод суммы для {}'.format(position))
			num = int(input())
			self.base[position][0] = num
			if self.base[position][1] == 'pos':
				month_total += num
			else:
				month_total -= num
		return month_total, self.base.items()

	def file_creator(self,to_write_data,to_write_total):
		with open("{}.txt".format(self.month),"a+") as  my_file:
			for line in to_write_data:
				my_file.write(str(line) + '\n')
			my_file.write(to_write_total)
		my_file.close()

if __name__ == '__main__':
    print('Выбор действия ')
    print('1 - Внести отчет за месяц')
    choice = int(input())
    if choice == 1:
    	print('Введите название месяца на английском')
    	mon = input()
    	this_mon = month_results(mon)
    	itog, month_base = this_mon.month_update()
    	output_txt = 'Итог по месяцу {} составил {}'.format(mon, itog)
    	print(output_txt)
    	this_mon.file_creator(month_base,output_txt)



