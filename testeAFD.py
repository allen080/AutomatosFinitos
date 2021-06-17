from afd import AFD
from afd import *

automato = AFD(alfabeto=[0.5,1])

automato.createEstado("Q1") # 0.0
automato.createEstado("Q2") # 0.50
automato.createEstado("Q3") # 1.00
automato.createEstado("Q4",final=True) # 1.50

automato.createTransicao("Q1","Q2",0.50)
automato.createTransicao("Q1","Q3",1.00)

automato.createTransicao("Q2","Q3",0.50)
automato.createTransicao("Q2","Q4",1.00)

automato.createTransicao("Q3","Q4",0.50)
automato.createTransicao("Q3","Q4",1.00)

automato.createTransicao("Q4","Q4",0.50)
automato.createTransicao("Q4","Q4",1.00)

print(automato.aceitaPalavra([1.0,1.0]))

# ******************************* Teste 2 ******************************

automato = AFD(['a','b'])
automato.createEstados('q0','q1','q3')
automato.createEstado('q2',final=True)

automato.createTransicao('q0','q1','a')
automato.createTransicao('q0','q3','b')

automato.createTransicao('q1','q2','b')
automato.createTransicao('q1','q3','a')

automato.createTransicao('q2','q2','a')
automato.createTransicao('q2','q2','b')

automato.createTransicao('q3','q3','a')
automato.createTransicao('q3','q3','b')

print(automato.aceitaPalavra('ababbbab'))

# ******************************* Teste 3 **************************88

afd = Logical_AFD(
	Sigma('a','b'),
	Q('q0','q1','q2','q3'),
	Delta(
		('q0','q1','a'),('q0','q3','b'),('q1','q2','b'),
		('q1','q3','a'),('q2','q2','a'),('q2','q2','b'),
		('q3','q3','a'),('q3','q3','b')
	),
	Q('q0'),
	F('q3')
)

print(afd.aceitaPalavra('abb'))
