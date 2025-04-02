Feature: Login com credenciais validas 

Scenario: login Válido
    Given que estou na tela de login do DUON
    When quando preencho os campos de username e password e clico em entrar
    Then devo validar se acessei a tela home