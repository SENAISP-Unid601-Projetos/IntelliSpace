# IntelliSpace

# DevFlow

**Problema:** Automatização De Espaços Por IOT
- **Área:** Elétrica
- **Responsável:** Roberto

**Equipe:**
- Camila Oliveira
- Hiasmin Lorrane
- Kauan Gallo
- Joao Vitor
- Felipe Allan

## 1. Escopo
Desenvolver um sistema de automação para o auditório, proporcionando ao palestrante a capacidade de controlar diversos dispositivos, como luzes, ar condicionado, projetor e computador, de maneira intuitiva e eficiente, por meio da voz (utilizando Alexa) ou de um aplicativo móvel dedicado.

## 2. Objetivos do projeto
- **Controle de Iluminação:**
  - Possibilidade de ligar/desligar as luzes principais do auditório.
  - Controle de intensidade luminosa para criar diferentes ambientes.
- **Gerenciamento do Ar Condicionado:**
  - Controle da temperatura ambiente.
  - Ligação e desligamento do sistema de ar condicionado.
- **Controle do Projetor:**
  - Ligar e desligar o projetor de maneira rápida.
  - Configuração de fontes de entrada para o projetor.
- **Automação do Computador:**
  - Iniciar/desligar o computador de apresentação.
  - Possibilidade de alternar entre aplicativos e apresentações.
- **Integração com Dispositivos de Voz:**
  - Utilização da tecnologia Alexa para comandos de voz.
  - Configuração de palavras-chave específicas para cada ação.
- **Aplicativo Móvel:**
  - Desenvolvimento de um aplicativo para controle remoto.
  - Interface intuitiva para facilitar o acesso às funcionalidades.
  - Conexão segura e estável com o sistema de automação no auditório.
- **Segurança e Privacidade:**
  - Implementação de medidas de segurança para evitar acessos não autorizados.
  - Possibilidade de configurar autenticação e criptografia para proteger os dados.
- **Personalização de Perfis:**
  - Capacidade de salvar e carregar configurações personalizadas para diferentes palestrantes.
  - Ajustes automáticos com base nas preferências pré-definidas de cada usuário.
- **Registro de Atividades:**
  - Manutenção de um log de atividades para monitorar o uso do sistema.
  - Relatórios disponíveis para análise de consumo de energia e eficiência.

## 3. Análise de Riscos
**Risco: Resistência à Adoção do Sistema pelos Funcionários**
- **Estratégias de Mitigação:** Realizar sessões de treinamento abrangentes para garantir a compreensão e aceitação do novo sistema. Envolva os funcionários desde as fases iniciais do projeto para receber feedback e endereçar preocupações.
- **Plano de Contingência:** Disponibilizar suporte técnico contínuo e recursos de aprendizado online. Implementar um programa de incentivo para promover a adoção do aplicativo.

**Risco: Falhas na Rede**
- **Estratégias de Mitigação:** Existir uma internet separada somente para os dispositivos conectados no auditório.
- **Plano de Contingência:** Suporte Técnico ativo para resolver qualquer problema que a rede venha a ter rapidamente.

**Risco: Problemas de Integração com Sistemas Existentes (mesmo que físicos)**
- **Estratégias de Mitigação:** Realizar uma análise detalhada dos sistemas existentes antes da implementação. Envolver a equipe de TI desde o início para garantir uma integração suave.
- **Plano de Contingência:** Manter uma equipe de suporte técnico preparada para lidar rapidamente com problemas de integração. Ter um plano de rollback para restaurar sistemas anteriores, se necessário.

**Risco: Falhas Técnicas no Aplicativo**
- **Estratégias de Mitigação:** Realizar testes rigorosos do aplicativo antes do lançamento. Contratar profissionais de desenvolvimento qualificados e experientes.
- **Plano de Contingência:** Implementar um sistema de backup que permita a rápida restauração em caso de falhas críticas. Manter uma equipe de suporte técnico disponível para resolver problemas imprevistos.

**Risco: Falta de Envolvimento da Alta Administração**
- **Estratégias de Mitigação:** Apresentar regularmente o progresso do projeto à alta administração. Destacar os benefícios estratégicos do sistema de automação do ambiente.
- **Plano de Contingência:** Desenvolver um plano de comunicação de crise para explicar a importância do projeto em momentos de resistência ou dúvida da alta administração.

**Risco: Mudanças nos Requisitos durante o Desenvolvimento**
- **Estratégias de Mitigação:** Realizar uma análise completa dos requisitos antes do início do desenvolvimento. Estabelecer um processo formal para gerenciar alterações nos requisitos.
- **Plano de Contingência:** Avaliar o impacto das mudanças nos prazos e recursos. Comunicar proativamente as alterações aos stakeholders e ajustar o cronograma conforme necessário.

**Risco: Interrupções Operacionais Durante a Implementação**
- **Estratégias de Mitigação:** Agendar a implementação durante períodos de menor atividade operacional. Comunicar claramente as interrupções planejadas e preparar soluções alternativas.
- **Plano de Contingência:** Desenvolver um plano de rollback para reverter temporariamente para processos manuais, se necessário. Garantir uma equipe de suporte pronta para lidar com problemas imprevistos.

## 4. Cronograma
**Janeiro/2024:** Planejamento e Análise
- Formação das equipes
- Processo de empatia
- Identificação de requisitos detalhados
- Início do desenvolvimento do escopo do projeto e documentação da ideia inicial
- Definição do backlog e prioridade das atividades

**Fevereiro/2024:** Desenvolvimento do MVP (Menor produto viável)
- Codificação e validação do MVP com o cliente e adaptação dos documentos de escopo (se necessário)

**Março/2024:** Desenvolvimento do protótipo do aplicativo
- Desenvolvimento das interfaces do usuário, fluxos da aplicação
- Desenvolvimento dos micro serviços e bancos de dados
- Revisão e ajuste do protótipo com feedback da equipe e usuários

**Abril/2024:** Implementação do Painel de Supervisão e Integração
- Início da integração com sistemas existentes
- Testes de integração e ajustes necessários

**Maio/2024:** Testes Finais e Lançamento
- Testes finais do aplicativo e do sistema integrado
- Treinamento final dos funcionários e supervisores
- Lançamento oficial do Sistema de Gestão de Limpeza
- Monitoramento inicial de feedback e desempenho

**Junho/2024:**
- Apresentação do Projeto

## 5. Recursos
**Pessoal:**
- Desenvolvedores de Software: Para a criação do aplicativo para funcionários e do painel de supervisão.
- Eletricista: Para fazer a instalação de lâmpadas, interruptores e fazer a verificação na fiação do auditório
- Gerente de Projeto: Para coordenar e supervisionar todas as atividades.

**Tecnologia:**
- Ambiente de Desenvolvimento Integrado (IDE): Ferramentas adequadas para o desenvolvimento do aplicativo e do painel de supervisão.
- Sistemas de versionamento de código: git e github para manter o código versionado e sempre atualizado.
- Ferramentas de Teste: Para garantir a qualidade e a confiabilidade do sistema.

**Equipamentos:**
- Computadores e Notebooks: Para desenvolvimento, teste e gerenciamento de projeto.
- Dispositivos Móveis: Para testes e treinamento do aplicativo em condições reais.
- Automatização: Lâmpadas, Alexa, interruptores, Ar-Condicionado e Projetor no auditório que serão conectados a Alexa

**Comunicação:**
- Ferramentas de Comunicação Online: Para facilitar a colaboração entre a equipe, como e-mails, mensagens instantâneas e videoconferências.

## 6. Custos
**Pessoal:**
- Desenvolvedores de Software: 5 desenvolvedores trabalhando por 3 dias na semana.
- Gerente de Projeto: 1 gerente de projeto.

**Tecnologia:**
- Ambiente de Desenvolvimento Integrado (IDE): Custo total (considerando licenças): $0
- Servidores e Infraestrutura em Nuvem: Custo total (considerando serviços em nuvem): $0
- Ferramentas de Teste de Software: Custo total (considerando licenças): $0
- API do chat gpt: Custo total (considerando licenças): $25 dólares = 123 reais (valor do dólar cotado dia 01/02/24)
- Amazon Developer Console: Custo total: $0

**Equipamentos:**
- Reles inteligentes: Custo total: R$600 (Seiscentos reais)
- Lâmpadas inteligentes: Custo total: R$760 (Setecentos e sessenta reais)
- Echo com alexa: Custo total: R$:675 (Seiscentos e setenta e cinco reais)
- Controle inteligente: Custo total: R$110 (Cento e dez reais)

**Total Geral:**
- Pessoal: $0
- Tecnologia: R$123,00 reais
- Equipamentos: R$ 2.268

**Custo Total do Projeto com Relés:** R$1.508,00 - 1.600,00
**Custo Total do Projeto com Lâmpadas inteligentes:** R$1.668,00 - 1.700,00

## 7. Documentação
### Requisitos funcionais
Como um Palestrante, eu quero poder realizar os meus comandos de voz e a minha conexão de forma segura e eficiente.
- **Critérios de Aceitação:** Deve ser possível com que a alexia reconheça a minha voz de forma segura para que ela não obedeça nenhum comando exceto o meu. E que o pareamento de celular possa parear apenas o meu no tempo de apresentação.

Como um Palestrante, eu quero ter a opção de poder utilizar tanto o comando de voz quanto por um aplicativo (quando necessário) que exerça a mesma eficiência.
- **Critérios de Aceitação:** O aplicativo deve ter a mesma facilidade quanto a própria Alexa.

Como usuário, eu quero ter uma segurança de dados eficiente.
- **Critérios de Aceitação:** Autenticação Segura: Implemente um sistema robusto de autenticação para garantir que apenas usuários autorizados possam acessar o sistema de automação.

Como palestrante, eu quero poder ligar as luzes e o ar-condicionado do auditório de forma fácil apenas por um comando de voz ou aplicativo.
- **Critérios de Aceitação:** os componentes precisam ser automatizados de forma com que eles sejam interligados com a alexia.

Como palestrante, eu quero poder inicializar o projetor e o modo apresentação com um comando de voz ou aplicativo para que eu tenha uma experiência inovadora ao apresentar o meu projeto.
- **Critérios de Aceitação:** Deve haver uma automatização nesses componentes para que esse comando se realize.

## 8. Avaliação do Projeto
**Objetivo Claro e Alcançável:**
- O objetivo de proporcionar automação ao auditório e oferecer controle intuitivo ao palestrante é claro e alcançável com as tecnologias mencionadas.

**Funcionalidades Abrangentes e Relevantes:**
- As funcionalidades propostas abrangem as necessidades típicas de um auditório, como controle de iluminação, ar condicionado, projetor e computador. São relevantes para otimizar a experiência do usuário.

**Integração de Tecnologias Modernas:**
- A integração com a Alexa e o desenvolvimento de um aplicativo móvel demonstram uma abordagem moderna e alinhada com as tendências tecnológicas atuais.

**Segurança e Privacidade Consideradas:**
- A inclusão de medidas de segurança e privacidade é essencial. No entanto, é necessário garantir que essas medidas sejam robustas para proteger contra ameaças potenciais.

**Tecnologias Escolhidas Adequadas:**
- As tecnologias escolhidas (Alexa Skills Kit) parecem adequadas para o projeto, mas a escolha final dependerá das necessidades específicas e da expertise da equipe de desenvolvimento.

**Etapas do Projeto Bem Definidas:**
- As etapas do projeto estão claramente definidas, proporcionando uma estrutura lógica para o desenvolvimento. No entanto, o sucesso dependerá da execução eficiente de cada etapa.

**Benefícios Tangíveis para Usuários e Meio Ambiente:**
- Os benefícios esperados, como facilitar o controle para palestrantes e reduzir o consumo de energia, são tangíveis e alinhados com os objetivos do projeto.

**Considerações Locais e Preferências do Usuário:**
- É importante considerar as especificidades locais do auditório e as preferências individuais dos usuários para garantir a adaptação eficaz do sistema.

**Desafios Potenciais:**
- Desafios podem surgir na integração com dispositivos específicos no auditório, na calibração dos sistemas de controle e na personalização para diferentes palestrantes. É crucial identificar e abordar esses desafios durante o desenvolvimento.

**Comunicação Efetiva com os Usuários:**
- A inclusão de registros de atividades e relatórios para os usuários, juntamente com uma documentação clara, promoverá a transparência e a compreensão do sistema.
