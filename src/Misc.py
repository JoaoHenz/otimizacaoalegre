import random


class Misc:

	def GeraSolucaoInicial(seed,seginicio,segfim,capacidade_segundo,clientes):
		random.seed(seed)
		solucao_inicial = [0]*len(clientes)
		for i in range(len(clientes)):
			solucao_inicial[i] = random.randint(0,1)
		cont=0
		'''
		print("Solução inicial gerada pela seed, sem qualquer tratamento:")
		print(solucao_inicial)'''
		
		while Misc.NaoRespeitaRestricoes(solucao_inicial,capacidade_segundo,segfim,clientes) and cont<len(solucao_inicial):
			solucao_inicial = Misc.ArrumaSolucao(solucao_inicial,cont)
			cont = cont+1

		'''
		print("Solução inicial depois de ser tratada para obedecer as restrições do Temporal Knapsack:")
		print(solucao_inicial)'''

		return solucao_inicial



	def BuscaInicio(clientes):
		
		lista_aux = [0] *len(clientes)

		for i in range(len(clientes)):
			lista_aux[i] = clientes[i][2]

		return min(lista_aux)

	def BuscaFim(clientes):
		lista_aux = [0] *len(clientes)

		for i in range(len(clientes)):
			lista_aux[i] = clientes[i][3]

		return max(lista_aux)


	def NaoRespeitaRestricoes(solucao,capacidade_segundo,segfim,clientes):
		lista_aux = [0] *segfim
		for i in range(len(solucao)): #coloca num array o quanto cada segundo está preenchido
			if solucao[i]==1:
				for j in range(clientes[i][2],clientes[i][3]):
					
					
					lista_aux[j] = lista_aux[j] + clientes[i][1]

		for i in range(len(lista_aux)): # se algum estiver preenchido mais do que o limite, a solução é inválida
			if lista_aux[i] > capacidade_segundo:
				return True

		return False

	def ArrumaSolucao(solucao, iterador):
		i=0
		while iterador+10*i < len(solucao):
			solucao[iterador+10*i] = 0
			i = i+1


		return solucao

	def TrataPorcento(alpha):
		if alpha < 1 or alpha > 100:
			return 10
		else:
			return alpha


	def AbreArquivo(archivename):
		info = []*3

		file = open(archivename,'r')
		content = file.read()
		file.close()
		content = content.split('\n')
		quantidade_itens = int(content[0])
		capacidade_segundo = int(content[1])
		clientes = content[2:quantidade_itens+2]
		for i in range(len(clientes)):
			clientes[i] = clientes[i].split()
		for i in range(len(clientes)):
			for j in range(4):
				clientes[i][j]=int(clientes[i][j]) 

		info = (clientes, quantidade_itens, capacidade_segundo)

		return info