# AGENDAMENTO MÉDICO

## DESCRIÇÃO
Esta aplicação busca simular um consultório médico, onde um paciente relata qual a especialidade desejada e então é guiado para dentro do consultório. Ao entrar, ele é atendido por um médico especializado. Os clientes serão as salas de recepção do consultório, eles serão os responsáveis por cadastrar, remover e atualizar os pacientes que vão entrar ou já estão no consultório. 
O consultório será o servidor. Nele há diferentes especialidades médicas, estas servirão para armazenar e separar os pacientes, a partir de qual os médicos consultarão qual o paciente a ser atendido.


## ABORDAGENS

<ol> 
    <li> <b>PIRC:</b> Estará envolvida na parte de comunicação entre o cliente com o servidor. O Cliente possui diferentes verbos:  ?: Enviar os dados de um paciente, ?: Excluir os dados de um paciente, ?: Atualizar os dados de Um paciente, ?: Pede os dados de um cliente e etc. _No Momemnto não possuimos um protocolo de aplicação expecífico em mente_. O servidor tratará os pedidos dos cliente, paralelamente, podendo retornar algum dado ou não.</li>
    <li> <b>Estrutura de Dados:</b> Estará presente na parte do gerenciamento das excessões, seja no lado do servidor ou na do cliente. utilizaremos POO para gerar os pacientes, os médicos, as especiealidades e o próprio consultório. Para a parte de  estrutura de dados, utilizaremos <b>duas</b>: 
        <ol>
            <li>
                <u>Lista Encadeada</u>
                <ol>
                    <li>As especialidades médicas do consúltorio serão armazenadas</li>
                    <li>Cada especialidade deverá ter a sua própria fila de espera, onde o paciente será inserido a partir do valor da sua prioridade e também servirá para que os médicos possam saber qual o paciente que eles deveram consultar.</li>
                    <li>A lista servirá para armazenar os paciente que ainda não foram despachados para a clínica.</li>
                </ol>
            </li>
            <li><u>Árvore Binária de Busca</u>
                <ol>
                    <li>Será usada para armazenar os pacientes que estão dentro da clínica</li>
                    <li>Será usada para armazenar os médico que estão dentro da clínica</li>
                </ol>
            </li>
        </ol>
    </li>
    <li> <b>Sistemas Operacionais</b> <u>sistema de Threads</u>: No servidor, ele utilizará Threads para se comunicar com vários clientes simultâneamente, Os médicos, mos quais poderão consultar os pacientes sem necessitar esperar a realização de um comando. Possuimos diversas variáveis que devem ser protegidas, por isso a  exclusão mútua será crucial: nas comunicações em paralelo entre os clientes com o servidor, a fim de evitar que um cliente altere um paciente que está a ser modificado por um outro; na inserção de um paciente, para evitar que um paciente seja inserido depois que o processo for trocado no processador; quando um médico for consultar um paciente, para que não ocorra de um paciente acaba sendo consultando por mais dois médicos ao mesmo tempo.</li>
</ol>

## O que já Foi feito

#### Básico
- [x] Estruturar as Ideias
- [x] Construir todas classes principais para o programa
- [ ] Enviar os Pacientes da Sala de Espera para o Consultório
- [ ] Programa Princial

#### PIRC
- [x] Discutir a respeito de quem será o Cliente
- [x] Discutir a respeito de quem será o Servidor
- [ ] Construir A parte do Cliente
- [ ] Construir A parte do Servidor

#### Estrutura de Dados
- [x] Criar um gerenciador de Tratamento de Erros 
- [x] Discutir a respeito de quais Estruturas de Dados utilizar
- [x] Construir a classe Cliente
- [x] Construir a classe Consultório
- [x] Incluir as Estruturas de Dados ao programa

#### Sistemas Operacionais
- [x] Discutir a respeito das Threads
- [x] Discutir a respeito de prioridades
- [ ] Discutir a respeito da zona crítica
- [ ] Adicionar as Threads
- [x] Adicionar prioridades
- [ ] Adicionar a Exclussão Mútua
