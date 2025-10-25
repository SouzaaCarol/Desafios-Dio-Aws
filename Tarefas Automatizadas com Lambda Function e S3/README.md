# 🚀 Desafio DIO: Automação de Tarefas com AWS Lambda, S3 e CloudFormation

## 🎯 Objetivo do Desafio

Este repositório documenta a implementação prática de uma solução de automação na AWS, utilizando **Lambda Function** para processamento, **Amazon S3** para armazenamento e **AWS CloudFormation** para gerenciamento de infraestrutura como código (IaC). O objetivo central foi consolidar o conhecimento na integração destes serviços e na documentação técnica do processo, garantindo a criação de uma infraestrutura robusta, escalável e versionável.

## ⚙️ Arquitetura Proposta (Cenário)

Para este desafio, foi implementada uma automação básica de **processamento de arquivos assíncrono**, demonstrando a capacidade de resposta a eventos de armazenamento.

**Cenário:** *Processamento de Metadados de Arquivo*
1.  Um usuário (ou sistema) faz o upload de um arquivo para o **S3 Bucket de Origem** (`SourceBucket`).
2.  O evento de `ObjectCreated` no S3 dispara a **AWS Lambda Function** (`FileProcessorLambda`).
3.  A Lambda Function lê o evento de notificação e registra metadados cruciais do arquivo (nome, tamanho e chave) no **Amazon CloudWatch Logs**.
4.  Esta estrutura serve como base para cenários mais complexos (ex: redimensionamento de imagens, indexação de documentos, processamento de ETL).

## 🛠️ Infraestrutura como Código (CloudFormation)

Toda a infraestrutura foi provisionada utilizando um template CloudFormation no formato YAML. O template garante a criação e o gerenciamento de todos os componentes necessários de forma atômica.

### 📄 Template Principal

O arquivo [**`cloudformation-template.yaml`**](cloudformation-template.yaml) define os seguintes recursos:

| Recurso AWS | Tipo | Função |
| :--- | :--- | :--- |
| **IAM Execution Role** | `AWS::IAM::Role` | Define as permissões mínimas para a Lambda (acesso ao S3 para leitura e gravação de logs no CloudWatch). |
| **Lambda Function** | `AWS::Lambda::Function` | Contém o código de processamento. |
| **S3 Bucket de Origem** | `AWS::S3::Bucket` | Onde os arquivos são carregados, atuando como o gatilho da automação. |
| **Lambda Permission** | `AWS::Lambda::Permission` | Concede ao S3 a autoridade para invocar a Lambda quando um objeto é criado. |
| **S3 Notification** | Configuração do Bucket | Define a trigger que liga o evento de `s3:ObjectCreated:*` à `FileProcessorLambda`. |

### Snippet do Template (CloudFormation - YAML)

Este snippet demonstra a definição da Função Lambda e a Role de execução, que são recursos interdependentes essenciais:

```yaml
# cloudformation-template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Desafio DIO - Lambda, S3 e CloudFormation

Resources:
  # 1. IAM Role para a Lambda
  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal: { Service: lambda.amazonaws.com }
            Action: sts:AssumeRole
      ManagedPolicyArns:
        # Política padrão para escrita de logs no CloudWatch
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
      Policies:
        - PolicyName: S3AccessPolicy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:GetObjectTagging
                Resource: !Sub 'arn:aws:s3:::${SourceBucket}/*'

  # 2. Lambda Function
  FileProcessorLambda:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: FileProcessorLambdaDIO
      Runtime: python3.9
      Handler: index.handler
      Role: !GetAtt LambdaExecutionRole.Arn
     
