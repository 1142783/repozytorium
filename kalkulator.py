def dodawanie(a,b):
	wynik = a + b
	return wynik
def get_info():
	print('To jest prosty kalkulator')
	
get_info()
print('Wprowadz pierwszą liczbę')
z1 = int(input())	
print('Wprowadz druga liczbę')
z2 = int(input())	
print(dodawanie(z1, z2))