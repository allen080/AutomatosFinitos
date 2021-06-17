from collections import OrderedDict

class AFD: # Estrutura básica para um AFD
	def __init__(self,alfabeto):
		if len(alfabeto)>0:
			self.alfabetoSetado = True
		else:
			self.alfabetoSetado = False

		self.estados = OrderedDict()
		self.alfabeto = set(alfabeto)
		self.estadoInicial = None
		self.estadoFinal = None
		self.estadoAtual = None

	def getEstados(self):
		return list(self.estados.keys())

	def getEstadoAtual(self):
		return self.estadoAtual

	def getEstadoInicial(self):
		return self.estadoInicial

	def getEstadoFinal(self):
		return self.estadoFinal

	def createEstado(self,nomeEstado,final=False,inicial=False):
		assert type(nomeEstado)==str

		if len(self.estados)==0:
			self.estadoInicial = nomeEstado
			self.estadoFinal = nomeEstado
			self.estadoAtual = nomeEstado

		self.estados[nomeEstado] = {}

		if inicial:
			self.estadoInicial = nomeEstado
		if final:
			self.estadoFinal = nomeEstado

	def createEstados(self,*estados):
		for e in estados:
			self.createEstado(e)

	def createTransicao(self,estadoOrigem,estadoDest,transicao):
		
		assert estadoOrigem in self.getEstados()
		assert estadoDest in self.getEstados()

		if self.alfabetoSetado:
			if not transicao in self.alfabeto:
				raise ValueError("[!] Valor da transicao nao contido no alfabeto")

		#if estadoDest in self.estados[estadoOrigem].values():
		#	raise ValueError("[!] estado de %s pra %s ja esta setado"%(estadoOrigem,estadoDest))
		if transicao in self.estados[estadoOrigem]:
			raise ValueError("[!] valor de transicao nao pode ser repetido em um AFD")

		self.estados[estadoOrigem][transicao] = estadoDest

	def mudaEstado(self,transicao):
		if transicao not in self.estados[self.getEstadoAtual()]:
			raise ValueError("[!] estado %s nao possui um estado de transicao para o valor %s"%(self.getEstadoAtual(),str(transicao)))

		self.estadoAtual = self.estados[self.getEstadoAtual()][transicao];
		return True

	def isFinal(self): # verifica se esta no ultimo estado
		return self.estadoAtual == list(self.estados.values())[-1]

	def aceitaPalavra(self,palavra):
		assert type(palavra)==str or type(palavra)==list or type(palavra)==tuple  

		if type(palavra)==str and ',' in palavra:
			palavra = palavra.split(',')

		for estado in palavra:
			if estado not in self.alfabeto:
				raise ValueError("[!] \"%s\" nao eh um simbolo valido do alfabeto %s"%(estado,self.alfabeto))
			self.mudaEstado(estado)

		if self.getEstadoAtual()!=self.getEstadoFinal():
			return False

		return True

# *************************** AFD Lógico ***************************

class Q: # conjunto de estados de um automato
	def __init__(self,*estados):
		if len(estados)==1:
			self.estados = estados[0]
		else:
			self.estados = list(estados)
	def __call__(self):
		return self.estados

class Delta: # funcoes de transicao
	def __init__(self,*funcoesTransicao):
		self.funcoesTransicao = list(funcoesTransicao)
	def __call__(self):
		return self.funcoesTransicao

class Sigma: # alfabeto
	def __init__(self,*alfabeto):
		self.alfabeto = list(alfabeto)
	def __call__(self):
		return self.alfabeto

class F: # conjunto de estados finais
	def __init__(self,*estadosFinais):
		if len(estadosFinais)==1:
			self.estadosFinais = estadosFinais[0]
		else:
			self.estadosFinais = list(estadosFinais)
	def __call__(self):
		return self.estadosFinais

class Logical_AFD(AFD): # implementa o AFD da classe AFD(), porem com a logica estrutural matemática de um autômato finito deterministico
	def __init__(self,sigma,q,delta,q0,f):
		super().__init__(list(sigma()))

		assert q0() in q() and f() in q()

		self.createEstado(q0(),inicial=True)
		self.createEstado(f(),final=True)
		q().remove(q0())
		q().remove(f())
		self.createEstados(*q())

		for transicao in delta():
			self.createTransicao(*list(transicao))