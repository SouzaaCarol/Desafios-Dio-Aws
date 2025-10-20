# 🚀 Desafio DIO: Gerenciamento e Arquitetura Serverless/EC2 na AWS

Este repositório documenta a experiência prática e os conhecimentos consolidados em serviços-chave da AWS, com foco no Gerenciamento de Instâncias EC2 e na construção de um fluxo de processamento de arquivos.

## 🎯 Objetivo do Laboratório

O desafio teve um duplo objetivo:
1.  **Consolidar** os conhecimentos práticos sobre o ciclo de vida e gerenciamento de uma instância Amazon EC2.
2.  **Documentar** uma arquitetura de exemplo que utiliza a integração entre **S3, AWS Lambda e EC2** para processamento de arquivos.

---

## 🎨 1. Arquitetura Proposta: Fluxo de Processamento de Arquivos

A arquitetura abaixo ilustra um fluxo comum na AWS onde um evento de armazenamento (**S3**) dispara uma função *serverless* (**Lambda**), que, por sua vez, orquestra o trabalho pesado em uma máquina virtual (**EC2**).

*Diagrama de Arquitetura (S3, Lambda, EC2)*

[Insira aqui a imagem da sua arquitetura final (ex: `image_7628c9.png`) usando a sintaxe Markdown: `![Diagrama AWS S3-Lambda-EC2](images/nome_do_seu_arquivo.png)`]

### ➡️ Detalhamento do Fluxo

| Etapa | Serviço(s) | Ação e Conceito |
| :---: | :--- | :--- |
| **1. Input** | S3 (Bucket de Origem) | O fluxo começa com o **Upload de Arquivo**. O Amazon S3 armazena o arquivo de entrada. |
| **2. Gatilho** | S3 → Lambda | A criação do objeto no Bucket de Origem dispara a **AWS Lambda Function**. Este é um padrão *serverless* de processamento orientado a eventos. |
| **3. Orquestração** | Lambda → EC2 | A Lambda Function executa o código para **Invocar ou Comandar a Instância EC2**, transferindo o controle da execução. |
| **4. Processamento** | EC2 | A instância **Amazon EC2 (Instância de Processamento)** realiza a tarefa pesada (Ex: compressão de vídeo, análise de dados complexa). |
| **5. Output** | EC2 → S3 | Após o processamento, a instância EC2 salva o resultado final no **Amazon S3 (Bucket de Destino/Resultado)**. |

---

## ⚙️ 2. Gerenciamento de Instâncias EC2 (Requisito Principal)

Para que a **Instância de Processamento EC2** no diagrama funcione, é essencial entender seu gerenciamento e ciclo de vida:

### A. Ciclo de Vida da Instância

| Ação no Console (ou CLI) | Descrição e Observações |
| :---: | :--- |
| **Lançar Instância (Launch)** | Cria a VM, definindo AMI, Tipo de Instância e Chave de Acesso. |
| **Em Execução (Running)** | A instância está ativa e gerando custos. |
| **Parar (Stop)** | Desliga a instância, **mantendo o disco (EBS)** e os dados intactos. O custo de computação é interrompido. |
| **Iniciar (Start)** | Coloca a instância em "Running" novamente. |
| **Encerrar (Terminate)** | Destrói a instância e, por padrão, o volume EBS. Os dados são perdidos. |

### B. Segurança e Armazenamento

* **Security Groups:** Atuam como um firewall virtual, controlando o tráfego de entrada (`inbound`) e saída (`outbound`) da instância.
* **Volumes EBS:** É o armazenamento de bloco persistente que a EC2 usa como disco rígido. Os dados persistem mesmo quando a instância é parada.
* **Snapshots de EBS:** Backups incrementais do seu Volume EBS, essenciais para a recuperação de desastres (DR) e migração de dados.

---

## 🔗 Links e Recursos

* **Documentação Oficial:** [Gerenciando EC2 instâncias da Amazon - Documentação AWS](https://docs.aws.amazon.com/pt_br/ec2/index.html)
* **Perfil DIO:** [Ana Carolina Martins Souza]
