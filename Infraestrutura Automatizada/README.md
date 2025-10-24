# 🚀 Desafio DIO: Implementação de Infraestrutura Automatizada com AWS CloudFormation

## 📋 Sobre o Projeto

Este repositório é o entregável do Desafio de Projeto da [DIO - Digital Innovation One] focado na implementação e documentação de uma infraestrutura automatizada utilizando o serviço **AWS CloudFormation**.

O objetivo principal foi explorar os conceitos de Infraestrutura como Código (IaC), utilizando CloudFormation para provisionar recursos da AWS de forma declarativa, repetível e segura.

## 🎯 Objetivos de Aprendizagem

Ao longo da execução deste desafio, os seguintes objetivos foram alcançados:

1.  **Aplicação Prática de Conceitos:** Provisionamento de uma infraestrutura básica na AWS utilizando um template YAML do CloudFormation.
2.  **Infraestrutura como Código (IaC):** Compreensão do ciclo de vida de um *Stack* (criação, atualização e exclusão).
3.  **Documentação Estruturada:** Criação de um `README.md` detalhado para registrar o processo, as decisões técnicas e os principais *insights* adquiridos.
4.  **Uso do GitHub:** Utilização da plataforma para versionamento, compartilhamento e apresentação do material técnico.

## 🛠 Solução Técnica Implementada

Para demonstrar a proficiência em CloudFormation, foi implementada uma infraestrutura base, que tipicamente inclui:

1.  **Rede Virtual (VPC):** Criação de uma Virtual Private Cloud para isolar o ambiente.
2.  **Subnet:** Criação de pelo menos uma sub-rede dentro da VPC.
3.  **Internet Gateway (IGW):** Para permitir a comunicação da VPC com a internet.
4.  **Security Group (SG):** Para controle de tráfego de entrada e saída.

### ⚙️ Template CloudFormation

O template principal para provisionamento está localizado em `cloudformation/infra_base.yaml`. Este arquivo define a infraestrutura **desejada** no formato YAML.

### 📄 Parâmetros e Outputs

* **Parâmetros (`Parameters`):** O template utiliza parâmetros para permitir a customização da infraestrutura no momento da criação da *Stack* (ex: nome da VPC, CIDR block).
* **Outputs (`Outputs`):** Os valores importantes da infraestrutura provisionada (ex: ID da VPC, ID do Security Group) são exportados para fácil referência ou para uso em outras *Stacks*.

## 💡 Anotações e Insights Adquiridos

### 1. **Natureza Declarativa**
O CloudFormation é declarativo, o que significa que especificamos o **estado final** desejado (o que queremos) e não o processo passo a passo (como fazer). O CloudFormation se encarrega de descobrir as dependências e a ordem correta para provisionar os recursos.

### 2. **Gerenciamento de Dependências**
Recursos como `InternetGateway` e `VPC` são criados em uma ordem específica. CloudFormation infere muitas dessas dependências, mas a propriedade `DependsOn` pode ser usada para garantir uma ordem estrita quando necessário.

### 3. **Rollback Automático**
Um grande benefício é a funcionalidade de *Rollback*. Se qualquer recurso falhar durante a criação da *Stack*, o CloudFormation tenta reverter todas as alterações e excluir os recursos criados, garantindo um estado limpo (ou o estado anterior, se for uma atualização).

### 4. **Funções Intrínsecas**
O uso de funções intrínsecas como `!Ref` (referenciar um recurso) e `!Sub` (substituir variáveis em strings) é essencial para criar templates dinâmicos e reutilizáveis.

### 5. **Ciclo de Vida do Template**
Qualquer alteração na infraestrutura é feita editando o template e **atualizando** a *Stack* existente, e não criando uma nova. Isso garante que o template seja sempre a fonte única de verdade (*Single Source of Truth*).

## 🔗 Recursos Úteis e Referências

* [Automatizando com AWS CloudFormation - Documentação da AWS](https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/cfn-whatis.html)
* [Referência de Recursos AWS CloudFormation](https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)
* [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)
