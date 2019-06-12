s=input()
x=['a','A','i','I','o','O','e','E','u','U']
y=['b','B','c','C','d','D','F','f','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','w','W','x','X','y','Y','z','Z']
if s in x:
  print('Vowel')
elif s in y:
  print('Consonant')
else:
  print('invalid')
