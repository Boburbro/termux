# str1
# Bobur bro
import time 
print('=======v1.0=========')
print('Agar buni iahlatishni bilmasangiz Bhelp buyrug\'ini bering')
import time 
Bhelp = input()
if Bhelp == 'Bhelp':
	print('Bu Bobur bro str1 v1.0 \nNima qila oladi? \nBu python orqali ishlaydi va Matini bilan ishlaydi ')
print('=======v1.0=========')
gap = input('Gap yozing\n')
print('1.Matindagi belgilarni sanash\n2.Matindagi gaplarni sanash\n3.Matini teskari yozish\n4.Gapdagi hamma hariflarni kattada qilish\n5.Gapdagi hamma hariflarni kichkina qilish\n6.Barchasi')
main = input('Tanlang: ')
bir = len(gap)
words = gap.split(' ')
p = gap[::-1]
if main == '1':
	print('Bu gapda' , bir, 'ta belgi bor')
elif main == '2':
	print('Bu gapda', len(words) , 'ta so\'z bor')
elif main == '3':
	print('-->', p)
elif main == '4':
	print('-->', gap.upper())
elif main == '5':
	print('-->', gap.lower())
	
	
elif main == '6':
		print('Bu gapda' , bir, 'ta belgi bor')
		print('Bu gapda', len(words) , 'ta so\'z bor')
		print('-->', p)
		print('-->', gap.upper())
		print('-->', gap.lower())
else :
		print('Xato buyruq')
		
print('=======v1.0=========')

time.sleep(10000)
		
