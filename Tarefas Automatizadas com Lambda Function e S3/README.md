# 🚀 Desafio DIO: Automação de Tarefas com AWS Lambda, S3 e CloudFormation

## 🎯 Objetivo do Desafio

Este repositório cumpre o desafio de consolidar conhecimentos na criação de soluções automatizadas na AWS. O objetivo principal é **demonstrar a proficiência na prática de Infraestrutura como Código (IaC)**, utilizando o **AWS CloudFormation** para provisionar e gerenciar a integração de uma **AWS Lambda Function** acionada por eventos do **Amazon S3**.

O foco deste documento é detalhar o processo, a arquitetura e os principais aprendizados adquiridos, servindo como material de apoio e documentação técnica.

## ⚙️ Arquitetura e Fluxo de Automação

A solução implementada simula um fluxo de processamento de arquivos assíncrono e é composta por uma Stack CloudFormation com os seguintes componentes:

### Fluxo de Trabalho
1.  **Gatilho (S3 Bucket de Origem):** Um arquivo é carregado (evento `s3:ObjectCreated:*`) em um bucket S3 específico.
2.  **Invocação Assíncrona:** O S3, mediante permissão de notificação, invoca a AWS Lambda Function.
3.  **Processamento (Lambda Function):** A função Lambda é executada. Seu propósito é ler os metadados do evento (nome do bucket, chave do objeto e tamanho do arquivo) e registrar essas informações no CloudWatch Logs.
4.  **Logging e Monitoramento (CloudWatch):** Todos os eventos de invocação e os resultados do processamento da Lambda são registrados no CloudWatch, garantindo a rastreabilidade e monitoramento do sistema.

### Componentes Chave Provisionados por IaC
* **Amazon S3 Bucket:** O recurso de armazenamento que atua como fonte do evento.
* **AWS IAM Role para Lambda:** Uma política de permissões que adere ao Princípio do Mínimo Privilégio, permitindo que a função apenas escreva logs no CloudWatch e leia objetos (`s3:GetObject`) no Bucket de Origem.
* **AWS Lambda Function:** O código de execução (escrito em Python) que processa o evento S3.
* **AWS Lambda Permission:** A política de recurso que explicitamente autoriza o S3 a invocar a função Lambda. Este é um detalhe crucial da integração.

## 🛠️ Detalhes da Implementação de Infraestrutura como Código (IaC)

Toda a infraestrutura acima é definida no arquivo **`cloudformation-template.yaml`** deste repositório.

### O Papel do CloudFormation (IaC)

O CloudFormation foi escolhido para este desafio por oferecer:
* **Repetibilidade:** Criação de ambientes idênticos (dev, staging, prod) a partir do mesmo template.
* **Gerenciamento de Dependências:** O CloudFormation garante que a IAM Role seja criada antes da Lambda e que as permissões S3 sejam configuradas corretamente.
* **Versionamento:** O template YAML pode ser versionado no Git (GitHub), permitindo o rastreamento de todas as alterações de infraestrutura.
* **Desprovisionamento Simplificado:** Toda a arquitetura pode ser removida da AWS com um único comando de exclusão de *stack*, garantindo a limpeza completa dos recursos e evitando custos.

### Estrutura do Template YAML

O template está organizado para definir a sequência lógica de dependências:

1.  **`Resources`:** Seção principal onde cada serviço AWS é declarado.
2.  **IAM Role:** Definida primeiro para que a Lambda possa fazer referência a ela.
3.  **Lambda Function:** Referencia a Role e o código de execução (que está no `index.py`).
4.  **S3 Bucket:** O bucket é configurado com uma propriedade de `NotificationConfiguration` que aponta para a ARN da Lambda Function.
5.  **Lambda Permission:** Recurso final que fecha o ciclo de permissão, garantindo que o S3 consiga invocar a função.

## 💻 Detalhes do Código da Lambda Function

O código de processamento está contido no arquivo **`index.py`**.

### Lógica da Função
A função `handler` do Python:
1.  **Captura o Evento:** Recebe o payload JSON enviado pelo S3 (que contém a lista de `Records`).
2.  **Extração de Dados:** Itera sobre os registros, extraindo o nome do bucket, a chave do objeto e seu tamanho.
3.  **Registro:** Utiliza o módulo `logging` para escrever uma mensagem detalhada e formatada no **CloudWatch Logs**, confirmando a execução bem-sucedida e listando os metadados do arquivo.
4.  **Tratamento de Erros:** Inclui um bloco `try-except` para capturar falhas na execução e garantir que a exceção seja levantada (`raise e`), permitindo que a AWS registre a falha de invocação.

## 🧠 Insights e Aprendizados Essenciais

O desenvolvimento deste desafio proporcionou a consolidação de conceitos cruciais para a automação na AWS:

* **Necessidade da Permissão S3-Lambda (`AWS::Lambda::Permission`):** O principal ponto de atenção no CloudFormation é garantir que o recurso `AWS::Lambda::Permission` esteja presente. Sem ele, a trigger está configurada no lado do S3, mas a política de recurso da Lambda nega a invocação.
* **Uso de `!Sub` e `!GetAtt`:** O domínio dessas funções intrínsecas do CloudFormation foi essencial para referenciar dinamicamente recursos recém-criados, como o ARN da IAM Role (`!GetAtt LambdaExecutionRole.Arn`) e o nome do Bucket no recurso de permissão.
* **Debugging no CloudWatch:** A principal forma de validar a automação é acompanhar os logs de execução da Lambda no CloudWatch. Configurar o `logging` corretamente dentro do `index.py` é a chave para o *debugging* eficaz.
* **O Valor da Documentação:** A criação do template YAML e deste README reforça que o código de infraestrutura é tão importante quanto o código da aplicação e deve ser igualmente documentado e versionado.

## 🔗 Recursos Úteis

* [**`cloudformation-template.yaml`**](cloudformation-template.yaml): O Template de IaC completo.
* [**`index.py`**](index.py): O Código da Lambda Function.
* [Documentação Oficial da AWS - CloudFormation](https://aws.amazon.com/cloudformation/)
* [Documentação Oficial da AWS - S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html)
