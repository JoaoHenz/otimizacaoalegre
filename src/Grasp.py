import os
import random
import sys
class Grasp:

	def main(alpha, upperbound,capacidade_segundo,segfim,solucao_inicial, clientes):
		must_stop = False
		melhor_solucao = solucao_inicial
		cont=0

		
		while must_stop == False:
			nova_solucao = Grasp.SolucaoRandomicaGulosa(alpha,capacidade_segundo,segfim,clientes)
			print (Grasp.Avalia(nova_solucao,clientes))
			#nova_solucao = Grasp.BuscaLocal(nova_solucao)
			if Grasp.Avalia(nova_solucao,clientes) > Grasp.Avalia(melhor_solucao,clientes):
				melhor_solucao = nova_solucao
				if abs(Grasp.Avalia(melhor_solucao,clientes) - upperbound) < upperbound/10:
					must_stop = True
			cont = cont+1
			if cont >0:
				must_stop = True						

		return melhor_solucao




	def SolucaoRandomicaGulosa(alpha,cap_seg,segfim,clientes): 
		nova_solucao = [0]*len(clientes)
		must_stop = False

		

		while must_stop ==False:
			RCL = Grasp.CalculaRcl(alpha,nova_solucao,cap_seg,segfim,clientes)   #RCL é uma lista de indices dos clientes mais vantajosos
			if (RCL):
				random.shuffle(RCL)
				nova_solucao = Grasp.AtualizaSolucao(RCL[0],nova_solucao)
			else:
				must_stop = True #não havia nenhum cliente possível para ser colocado na solução sem que fossem quebradas restrições
			print(nova_solucao)
			#os.system('cls' if os.name == 'nt' else 'clear')


		
		return nova_solucao




	def CalculaRcl(alpha,solucao,cap_seg,segfim,clientes):
		lista_eficiencia = [[0 for x in range(2)] for y in range(len(solucao))] 
		for i in range(len(solucao)):
			if solucao[i]==0:
				#if Grasp.NaoRespeitaRestricoes(Grasp.AtualizaSolucao(lista_eficiencia[i][1],solucao),cap_seg,segfim,clientes)==False:
				
				lista_eficiencia[i][0] = clientes[i][0]/clientes[i][1]
			lista_eficiencia[i][1]=i


		PrecisaOrganizar = True
		lengthRcl = int((alpha/100)*len(solucao))
		while PrecisaOrganizar == True:
			PrecisaOrganizar = False
			lista_eficiencia.sort(key=lambda x: x[0],reverse= True)
			for i in range(lengthRcl):
				if lista_eficiencia[i][0] > 0:
					if Grasp.NaoRespeitaRestricoes(Grasp.AtualizaSolucao(lista_eficiencia[i][1],solucao),cap_seg,segfim,clientes)==True:
						lista_eficiencia[i][0]=0
						PrecisaOrganizar =True


		if lista_eficiencia[0][0] == 0:
			return None
		j = 0
		
		while lista_eficiencia[j][0] > 0 and j < lengthRcl: #delimita a Rcl para os valores que realmente sao entrantes
			j = j+1
		lengthRcl = j







		RCL = [0]*lengthRcl
		for j in range(lengthRcl):
			RCL[j] = lista_eficiencia[j][1]
		return RCL



	def AtualizaSolucao(entrante,solucao):
		
		uma_solucao = [0]*len(solucao)
		for i in range(len(solucao)):
			uma_solucao[i] = solucao[i]

		uma_solucao[entrante] = 1
		return uma_solucao



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
			if solucao[i] == 1:
				resultado = resultado+clientes[i][0]

		return resultado