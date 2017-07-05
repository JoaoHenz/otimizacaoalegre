
import random
class Grasp:

	def main(alpha, upperbound,capacidade_segundo,segfim,solucao_inicial, clientes):
		must_stop = False
		melhor_solucao = solucao_inicial
		
		while must_stop == False:
			nova_solucao = Grasp.SolucaoRandomicaGulosa(alpha,capacidade_segundo,segfim,clientes)
			#nova_solucao = Grasp.BuscaLocal(nova_solucao)
			print(nova_solucao)
			if Grasp.Avalia(nova_solucao,clientes) > Grasp.Avalia(melhor_solucao,clientes):
				melhor_solucao = nova_solucao
				if abs(Grasp.Avalia(melhor_solucao,clientes) - upperbound) < upperbound/10:
					must_stop = True
															

		return melhor_solucao


	def SolucaoRandomicaGulosa(alpha,cap_seg,segfim,clientes): 
		nova_solucao = [0]*len(clientes)
		must_stop = False

		while must_stop ==False:
			RCL = Grasp.CalculaRcl(alpha,nova_solucao,clientes)   #RCL é uma lista de indices dos clientes mais vantajosos
			random.shuffle(RCL)
			i=0
			while i<len(RCL) and Grasp.NaoRespeitaRestricoes(Grasp.AtualizaSolucao(RCL[i],nova_solucao),cap_seg,segfim,clientes)==True:
				i = i+1
			if i == len(RCL): #percorreu toda a RCL e nenhum valor pode ser encaixado
				must_stop = True
			else: 
				nova_solucao = Grasp.AtualizaSolucao(RCL[i],nova_solucao)

		return nova_solucao

	def CalculaRcl(alpha,solucao,clientes):
		lista_eficiencia = [[0 for x in range(2)] for y in range(len(solucao))] 

		for i in range(len(solucao)):
			if solucao[i]==0:
				lista_eficiencia[i][0] = clientes[i][0]/clientes[i][1]
			lista_eficiencia[i][1]=i



		lista_eficiencia.sort(key=lambda x: x[0],reverse= True)
		lengthRcl = int((alpha/100)*len(solucao))
		

		RCL = [0]*lengthRcl

		for j in range(lengthRcl):
			RCL[j] = lista_eficiencia[j][1]

		return RCL



	def AtualizaSolucao(entrante,solucao):

		nova_solucao = solucao
		nova_solucao[entrante] = 1
		return nova_solucao



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



	def BuscaLocal(solucao,cap_seg,segfim,clientes):
		
		for i in range(len(solucao)):
			i=1
		return 5


	def Avalia(solucao,clientes):
		resultado=0
		for i in range(len(solucao)):
			resultado = resultado + solucao[i]*clientes[i][0]

		return resultado