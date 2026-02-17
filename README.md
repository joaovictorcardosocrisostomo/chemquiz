# ChemQuiz: Ferramenta de Avaliação de Conhecimentos em Química

O **ChemQuiz** é uma aplicação interativa baseada em interface de linha de comando (CLI), desenvolvida em Python. O software tem como objetivo testar e reforçar conceitos fundamentais de química através de um sistema de perguntas e respostas dinâmico, aplicando conceitos de Programação Orientada a Objetos (POO) para estruturar a lógica do jogo e o gerenciamento de dados.

## Visão Geral

Este projeto foi desenvolvido como aplicação prática dos conceitos abordados no livro *Python Crash Course*, servindo como um estudo de caso sobre a transição de paradigmas procedurais para a orientação a objetos. O sistema permite ao usuário selecionar níveis de dificuldade progressivos, abrangendo desde a tabela periódica básica até conceitos de físico-química e química orgânica.

## Funcionalidades Principais

* **Seleção Dinâmica de Dificuldade:** O usuário pode optar por bancos de questões segregados por nível de complexidade (Fácil, Médio, Difícil) ou um modo Aleatório que unifica todas as bases de dados.
* **Sistema de Pontuação:** Acompanhamento em tempo real do desempenho do usuário durante a sessão.
* **Validação de Entradas:** Tratamento robusto de inputs do usuário para prevenir erros de execução e garantir a fluidez da navegação.
* **Arquitetura Modular:** Separação clara entre a camada de dados (`banco_questoes`), a lógica de entidade (`Question`) e o controlador do jogo (`Gamequiz`).
* **Controle de Fluxo:** Mecanismos para interrupção segura da execução a qualquer momento.

## Arquitetura do Projeto

O projeto segue uma arquitetura orientada a objetos simplificada, composta por dois componentes principais:

1.  **Classe `Question`:** Responsável pelo encapsulamento dos dados de cada questão individual (enunciado, opções e resposta correta) e pelo método de verificação da resposta.
2.  **Classe `Gamequiz`:** Atua como o "Game Engine", gerenciando o estado da aplicação, a pontuação, o ciclo de vida das rodadas e a interação com o usuário via terminal.

## Requisitos do Sistema

* **Linguagem:** Python 3.8 ou superior.
* **Dependências:** Biblioteca padrão do Python (`random`).
* **Sistema Operacional:** Compatível com Windows, Linux e macOS.

## Instalação e Execução

Para executar o projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/chemquiz.git](https://github.com/seu-usuario/chemquiz.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd chemquiz
    ```

3.  **Certifique-se de que os arquivos necessários estão presentes:**
    * `chemquiz.py` (Script principal)
    * `banco_questoes.py` (Módulo de dados)

4.  **Execute a aplicação:**
    ```bash
    python chemquiz.py
    ```

## Estrutura de Arquivos

A organização do código fonte segue a seguinte estrutura:

```text
chemquiz/
├── banco_questoes.py    # Repositório de dados contendo as listas de dicionários
├── chemquiz.py          # Ponto de entrada e lógica principal (Classes Question e Gamequiz)
└── README.md            # Documentação do projeto# chemquiz
