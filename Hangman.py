import os



Hman = ['''

 +---+
   	 |
	 |
	 |
	  
	  ''','''

 +---+
 0	 |
 	 |
 	 |

 	  ''','''

 +---+
 0	 |
 |	 |
	 |
      
      ''','''

 +---+
 0	 |
 |	 |
/	 |

 	  ''','''

 +---+
 0	 |
 |	 |
/ \\ |

	  ''','''

 +---+
 0	 |
 |\\ |
/ \\ |

 	  ''','''

 +---+
 0	 |
/|\\ |
/ \\ |

 	  '''
]



myWord = 'griffin'

myWord = list(myWord)
gList = list('_______')

pGuess = input('Guess a Letter')
index = 0
misses = 0

for letter in myWord:
	if letter == pGuess:
		gList[index] = pGuess 
		 
		index += 1
	else:
		misses += 1
		print(misses)
		

print(gList)


