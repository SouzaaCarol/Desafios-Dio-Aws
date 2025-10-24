# 🚀 Desafio DIO - Implementando sua Primeira Stack com AWS CloudFormation

Este repositório documenta a execução do desafio **"Implementando sua Primeira Stack com AWS CloudFormation"** da Digital Innovation One (DIO).

O foco deste projeto é aplicar os princípios de **Infraestrutura como Código (IaC)**, utilizando o serviço **AWS CloudFormation** para provisionar, atualizar e gerenciar recursos na Amazon Web Services de forma automatizada, repetível e segura.

## 🎯 Objetivos de Aprendizagem e Conclusões

Ao completar este desafio, os seguintes objetivos foram alcançados:

| Objetivo | Status | Conclusão |
| :--- | :--- | :--- |
| **Modelagem IaC** | ✅ Concluído | Capacidade de descrever a infraestrutura desejada usando templates YAML/JSON. |
| **Criação de Stack** | ✅ Concluído | Provisionamento bem-sucedido de uma Stack na AWS via Console ou AWS CLI. |
| **Gerenciamento de Ciclo de Vida** | ✅ Concluído | Compreensão do processo de criação, atualização e exclusão de recursos controlados pelo CloudFormation. |
| **Documentação Técnica** | ✅ Concluído | Estruturação e detalhamento do processo e dos aprendizados em um repositório GitHub. |

## 📝 Anotações e Insights Aprofundados

### 1. O Conceito de Stack e Change Sets

* **Stack:** No CloudFormation, uma *Stack* é a unidade fundamental de gerenciamento. Ela é uma coleção de recursos da AWS que você gerencia como uma única unidade. Por exemplo, uma Stack pode conter uma VPC, um Load Balancer e um grupo de Auto Scaling. A grande vantagem é que o ciclo de vida (criação, atualização e exclusão) de todos esses recursos é gerenciado em conjunto.
* **Change Sets (Conjuntos de Alterações):** Antes de aplicar uma atualização em uma Stack ativa, o CloudFormation permite criar um *Change Set*. Isso é crucial! O Change Set mostra exatamente quais recursos serão adicionados, modificados ou excluídos, e como. Isso aumenta drasticamente a segurança e a previsibilidade das alterações de infraestrutura, agindo como uma pré-visualização.

### 2. A Importância das Funções Intrínsecas

Templates de CloudFormation raramente são estáticos. Para criar infraestruturas interconectadas (ex: um Security Group que precisa referenciar a VPC criada no mesmo template), utilizamos **Funções Intrínsecas**.

| Função Intrínseca | Descrição | Exemplo de Uso |
| :--- | :--- | :--- |
| **`!Ref`** (ou `Fn::Ref`) | Retorna o valor de um Parâmetro ou o ID/Nome de um Recurso. | `Value: !Ref MyVPC` (referencia o ID da VPC) |
| **`!GetAtt`** (ou `Fn::GetAtt`) | Retorna um atributo específico de um recurso. | `Value: !GetAtt MyBucket.Arn` (retorna o ARN do Bucket) |
| **`!Sub`** (ou `Fn::Sub`) | Permite a substituição de variáveis em uma string (muito útil para nomes e URLs). | `BucketName: !Sub 'my-${AWS::AccountId}-data'` |

### 3. Gerenciamento de Falhas e Rollbacks

Um dos maiores benefícios do CloudFormation é seu mecanismo de *rollback*.

* **Processo de Falha:** Se a criação ou atualização de uma Stack falhar (por exemplo, tentativa de criar um nome de S3 Bucket que já existe), o CloudFormation, por padrão, tenta reverter (rollback) o processo para o último estado estável da Stack.
* **Estado Consistente:** Isso garante que a infraestrutura não fique em um estado parcialmente configurado, o que é um grande risco na criação manual de recursos. O estado da Stack volta a ser `ROLLBACK_COMPLETE` ou permanece em `UPDATE_ROLLBACK_COMPLETE`.

---

## 🛠️ Passos para a Implementação (CloudFormation)

Este é um resumo dos passos executados para implementar a Stack na AWS, conforme a prática do desafio:

### 1. Modelagem do Template
O template inicial foi criado em formato **YAML** (mais legível que JSON) para provisionar um recurso fundamental, como um S3 Bucket.

* **Arquivo:** `templates/s3-bucket-template.yaml` (localizado neste diretório).
* **Foco:** Utilizar `Parameters` e `Outputs` para demonstrar flexibilidade e rastreabilidade da IaC.

### Template Exemplo (s3-bucket-template.yaml)
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Template para criar um S3 Bucket de exemplo para o Desafio DIO.

Parameters:
  BucketNameParameter:
    Type: String
    Description: Nome globalmente único para o S3 Bucket (deve ser em letras minúsculas, sem espaços).
    MinLength: 3

Resources:
  MySimpleS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      # Referencia o nome do Parâmetro
      BucketName: !Ref BucketNameParameter
      
      # Bloqueio de acesso público por segurança
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
        
      # Tags para organização
      Tags:
        - Key: Environment
          Value: Development
        - Key: Project
          Value: DIO-CloudFormation-Challenge

Outputs:
  # Exporta o nome e o ARN do Bucket criado
  BucketNameOutput:
    Description: Nome do S3 Bucket criado.
    Value: !Ref MySimpleS3Bucket
  BucketArnOutput:
    Description: ARN do S3 Bucket criado.
    Value: !GetAtt MySimpleS3Bucket.Arn
