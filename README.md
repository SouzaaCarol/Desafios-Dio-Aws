# ☁️ Repositório de Desafios AWS & Cloud Computing 

Este repositório consolida os desafios práticos de *Cloud Computing* e **DevOps/SRE** realizados na plataforma DIO, com foco em serviços da **Amazon Web Services (AWS)** e na metodologia **Infraestrutura como Código (IaC)**.

## 🎯 Habilidades e Tecnologias Destacadas

| Categoria | Serviço/Tecnologia | Conceitos Aplicados |
| :---: | :--- | :--- |
| **Infraestrutura como Código (IaC)** | **AWS CloudFormation**, YAML | Provisionamento declarativo, Gerenciamento de Stack, Rollback, Funções Intrínsecas (`!Ref`, `!Sub`). |
| **Serverless & Automação** | **AWS Lambda, Amazon S3** | Arquitetura Orientada a Eventos, Triggers S3, Permissões S3-Lambda, Processamento Assíncrono. |
| **IaaS & Gerenciamento** | **Amazon EC2, EBS, Security Groups** | Ciclo de Vida da VM (Launch, Stop, Terminate), Volumes EBS e Snapshots, Controle de Tráfego de Rede (Firewall Virtual). |
| **Redes e Segurança** | **Amazon VPC, IGW, Subnets** | Isolamento de Ambiente, Conectividade à Internet, Segmentação de Redes. |

---

## 📂 Visão Geral dos Projetos (Desafios Práticos)

O repositório está organizado em pastas (ou seções) que refletem os desafios de implementação.

### 1. ⚙️ Infraestrutura como Código (IaC) com CloudFormation

**Foco:** Provisionamento de componentes de Rede e Base de Infraestrutura de forma declarativa e repetível.

| Descrição do Projeto | Conceitos Chave | Arquivos de Referência |
| :--- | :--- | :--- |
| **Provisionamento de Rede Base** | Criação de **VPC**, **Subnet**, **Internet Gateway (IGW)** e **Security Group (SG)**. | `iac-cloudformation/infra_base.yaml` |
| **Princípios de IaC** | Natureza Declarativa, Gestão de Parâmetros (`Parameters`) e Exportação de Variáveis (`Outputs`), Rollback Automático. | *[Leia a documentação detalhada na pasta respectiva]* |

### 2. ⚡ Automação Serverless (Lambda e S3)

**Foco:** Criação de um pipeline de processamento de dados usando serviços *serverless* e orquestrado via CloudFormation.

| Descrição do Projeto | Conceitos Chave | Arquivos de Referência |
| :--- | :--- | :--- |
| **Pipeline S3-Lambda-CFN** | **S3** como gatilho de eventos, **Lambda** para processamento leve (log de metadados). | `serverless-automation/cloudformation-template.yaml` |
| **Permissões Críticas** | Criação da `IAM Role` com Mínimo Privilégio e a importância da `AWS::Lambda::Permission` para autorizar a invocação do S3. | `serverless-automation/index.py` (Código da Lambda) |

### 3. 🖥️ Gerenciamento e Arquitetura Híbrida (EC2, S3, Lambda)

**Foco:** Entendimento do IaaS (EC2) e sua integração com arquiteturas Serverless para cargas de trabalho de alto consumo de recursos.

| Descrição do Projeto | Conceitos Chave | Arquivos de Referência |
| :--- | :--- | :--- |
| **Arquitetura S3-Lambda-EC2** | **Orquestração** onde a Lambda aciona uma **EC2** para *heavy processing* (Ex: Compressão/ETL). | *[Insira a pasta ou o documento de arquitetura]* |
| **Gerenciamento de EC2** | Demonstração do **Ciclo de Vida** da instância (Stop/Start vs. Terminate) e uso de **Security Groups** e **Volumes EBS**. | *[Insira a pasta ou o documento de gerenciamento]* |

---

## 💡 Principais Aprendizados Consolidados

A execução destes desafios reforçou os seguintes pilares de uma carreira em Cloud e DevOps:

| Pilar | Aprendizado Essencial |
| :--- | :--- |
| **IaC** | A fonte única de verdade (Single Source of Truth) para a infraestrutura **sempre** deve ser o template YAML, e não o console da AWS. |
| **Serverless** | O desenvolvimento *serverless* exige foco no **modelo de permissões (IAM)**, especialmente ao integrar diferentes serviços. |
| **Segurança** | **Security Groups** são a primeira linha de defesa. O Mínimo Privilégio deve ser aplicado a cada recurso (IAM Roles). |
| **Resiliência** | A funcionalidade de **Rollback Automático** do CloudFormation é essencial para garantir que falhas no *deployment* não deixem ambientes parcialmente configurados ou inconsistentes. |

## 🔗 Sobre a Autora

* **Nome:** [Ana Carolina Martins Souza]
* **Perfil DIO:** [Ana Souza]
* **Contatos:** [(https://www.linkedin.com/in/cmanasouza,carol22022004@gmail.com ]
