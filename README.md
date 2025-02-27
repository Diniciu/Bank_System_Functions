# Explicação do Código
Este programa em Python simula um sistema bancário simples, permitindo operações básicas como depósito, saque, visualização de extrato, criação de usuários, criação de contas correntes e listagem de contas. A seguir, uma descrição detalhada das funcionalidades implementadas:

## Menu de Operações
O programa apresenta um menu de operações que permite ao usuário escolher entre as seguintes opções:

Depositar
Sacar
Visualizar Extrato
Criar Usuário
Criar Conta Corrente
Listar Contas
Sair

## Variáveis Globais
O programa utiliza várias variáveis globais para armazenar informações sobre o saldo, limite de saque, extrato, número de saques, limite de saques, usuários, contas correntes e número da agência.

## Funções
Função de Depósito
A função de depósito permite adicionar um valor ao saldo e registrar a transação no extrato. Os argumentos são passados por posição.

## Função de Saque
A função de saque permite retirar um valor do saldo, respeitando o limite de saque e o número máximo de saques permitidos por dia. A função também registra a transação no extrato. Os argumentos são passados por nome.

## Função de Mostrar Extrato
A função de mostrar extrato exibe todas as transações registradas no extrato e o saldo atual. O saldo é passado por posição e o extrato por nome.

## Função de Criar Usuário
A função de criar usuário permite adicionar um novo usuário ao sistema. O usuário é composto por nome, data de nascimento, CPF e endereço. O CPF é armazenado apenas com números e não pode haver dois usuários com o mesmo CPF.

## Função de Criar Conta Corrente
A função de criar conta corrente permite criar uma nova conta corrente para um usuário existente. A conta é composta por agência, número da conta e usuário. O número da conta é sequencial e a agência é fixa. A função verifica se o CPF informado pertence a um usuário existente e associa a conta a esse usuário.

## Função de Listar Contas
A função de listar contas exibe todas as contas correntes existentes, mostrando a agência, número da conta, nome do usuário e CPF do usuário.

## Loop Principal
O programa entra em um loop infinito, exibindo o menu de operações e aguardando a escolha do usuário. Dependendo da opção escolhida, o programa executa a função correspondente. O loop é interrompido quando o usuário escolhe a opção de sair.
