# AGENDAMENTO MÉDICO

## Breve descrição
Este projeto possui o intuito de simular um sistema agendamento médico para aquele exato dia. Haverá um cliente (aquele que realiza o cadastro dos pacientes) é  responsável por: enviar, remover e atualizar os dados dos pacientes no servidor, e um servidor (aquele que é responsável por armazenar e fazer o tratamento dos dados) é responsável por: receber as exigências do cliente, tratar os dados recebidos, encaminhar os dados do paciente para um Médico.

## Abordagem de cada disciplina

**PIRC:** Estará envolvida na parte de comunicação entre o cliente com o servidor. O Cliente possui diferentes verbos:  ?: Enviar os dados de um paciente, ?: Excluir os dados de um paciente, ?: Atualizar os dados de Um paciente, ?: Pede os dados de um cliente e etc. . O servidor tratará os pedidos dos cliente, paralelamente, podendo retornar algum dado ou não.

**Estrutura de Dados:** Estará presente na parte do gerenciamento das excessões, seja na parte do servidor ou na parte do cliente. utilizaremos POO para gerar os pacientes, médicos e outras coisas. Para estrutura de dados, utilizaremos duas: a Fila Encadeada, linear, cada médico deverá ter a sua própria fila de espera, onde o primeiro paciente a ser cadastrado, deverá ser o primeiro a ser consultado, e a Árvore Binária de Busca, não linear, essa servirá para o cadastramento e a consulta dos pacientes nos quais tiveram suas consultas marcadas.

**Sistemas Operacionais** Será utilizada o sistema de Threads: No servidor, ele utilizará Threads para se comunicar com vários clientes simultâneamente, Os médicos, mos quais poderão consultar os pacientes sem necessitar esperar a realização de um comando. Possuimos diversas variáveis que devem ser protegidas, por isso a  exclusão mútua será crucial: nas comunicações em paralelo entre os clientes com o servidor, a fim de evitar que um cliente altere um paciente que está a ser modificado por um outro; na inserção de um paciente, para evitar que um paciente seja inserido depois que o processo for trocado no processador; quando um médico for consultar um paciente, para que não ocorra de um paciente acaba sendo consultando por mais dois médicos ao mesmo tempo.


## O que já Foi feito

#### Básico
- [x] Estruturar as Ideias
- [ ] Programa Princial

#### PIRC
- [x] Discutir a respeito de quem será o Cliente
- [x] Discutir a respeito de quem será o Servidor
- [ ] Construir A parte do Cliente
- [ ] Construir A parte do Servidor

#### Estrutura de Dados
- [x] Criar o gerenciador de Tratamento de Erros 
- [x] Discutir a respeito de quais Estruturas de Dados utilizar
- [x] Construir a classe Cliente
- [x] Construir a classe Médico
- [ ] Incluir as Estruturas de Dados ao programa

#### Sistemas Operacionais
- [ ] Discutir a respeito das Threads
- [ ] Discutir a respeito da zona crítica
- [ ] Adicionar as Threads
- [ ] Adicionar a Exclussão Mútua
