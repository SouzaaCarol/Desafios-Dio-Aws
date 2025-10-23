# 🚀 AWS Step Functions: Workflows Automatizados e Orquestração

Este repositório documenta o aprendizado e a prática realizada no desafio de consolidação de workflows automatizados utilizando o **AWS Step Functions**. O objetivo foi aplicar os conceitos de State Machines para orquestrar e gerenciar fluxos de trabalho distribuídos, resistentes a falhas e escaláveis.

## 🎯 Objetivo de Aprendizagem

O foco principal deste laboratório foi:

1.  **Compreender a Arquitetura:** Entender como o AWS Step Functions funciona como um orquestrador de serviços sem servidor (serverless).
2.  **Modelagem de Workflows:** Praticar a definição de State Machines utilizando a linguagem Amazon States Language (ASL) em formato JSON.
3.  **Integração de Serviços:** Configurar o Step Functions para invocar e gerenciar a execução de outros serviços AWS (como Lambda Functions, SQS, SNS, ou ECS) em uma ordem definida.
4.  **Tratamento de Falhas:** Implementar mecanismos de `Retry` (tentativa) e `Catch` (captura de erro) para tornar o workflow robusto.

## 💡 O que é AWS Step Functions?

AWS Step Functions é um serviço que permite coordenar os componentes de aplicações distribuídas e microsserviços usando *workflows* visuais. Ele é ideal para gerenciar tarefas de longa duração e garantir que o estado de cada etapa seja mantido, facilitando a depuração e o monitoramento.

### Conceitos Chave Abordados

| Conceito | Descrição |
| :--- | :--- |
| **State Machine** | O workflow completo, definido por uma série de estados (Stages). |
| **Task (Tarefa)** | Um estado que executa uma unidade de trabalho (ex: invocar uma AWS Lambda Function, chamar uma API). |
| **Choice (Escolha)** | Um estado que adiciona lógica condicional (`if/else`) ao workflow, direcionando o fluxo. |
| **Wait (Espera)** | Um estado que atrasa a execução por um tempo específico ou até uma data/hora. |
| **Parallel (Paralelo)** | Um estado que permite executar múltiplos branches de forma simultânea. |
| **Amazon States Language (ASL)** | A linguagem baseada em JSON utilizada para definir a State Machine. |

## 💻 Código de Exemplo: Definição da State Machine

O coração do Step Functions é a sua definição em JSON (Amazon States Language - ASL). O arquivo abaixo contém um exemplo de uma **State Machine Simples** que demonstra os estados `Task` (execução), `Choice` (decisão) e `Wait` (pausa).

> **Acesse o código de definição completo aqui:**
> [**`state-machine-definition.json`**](./state-machine-definition.json)

### 📝 Insights do Exemplo:

* **`Processar Dados`:** O estado inicial que invoca uma Função Lambda para executar uma tarefa.
* **`Verificar Status`:** Um estado `Choice` que examina a saída do passo anterior para decidir o próximo fluxo (Sucesso, Falha ou Aguardar).
* **`Aguardar Processamento`:** Demonstra o estado `Wait`, que pode ser usado para *polling* ou atrasos programados.

## 🔗 Recursos Adicionais

* [AWS Step Functions - Documentação Oficial](https://aws.amazon.com/step-functions/)
* [Amazon States Language (ASL) - Guia de Referência](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-asl.html)
* [GitHub Markdown - Guia de Sintaxe](https://guides.github.com/features/mastering-markdown/)
