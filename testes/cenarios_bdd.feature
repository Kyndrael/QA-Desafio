Feature: Login

  Scenario: Usuário entra com dados válidos
    Given que o usuário está na tela de login
    When ele preenche e-mail e senha corretos
    And clica em "Login"
    Then ele deve acessar o dashboard
    And ver uma mensagem de boas-vindas

Feature: Cadastro

  Scenario: Tentar se cadastrar com e-mail já usado
    Given que o e-mail já existe no sistema
    When o usuário tenta se cadastrar com esse e-mail
    Then o sistema deve mostrar a mensagem "Este e-mail já está em uso"
