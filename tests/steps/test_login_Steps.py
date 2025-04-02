from pytest_bdd import given, when, then, scenarios 
from playwright.sync_api import expect, Page 
from credenciais import email, senha

scenarios('../feature/login.feature')



@given('que estou na tela de login do DUON')
def pagina_de_login(browser: Page):
    browser.goto('https://app.hml.dsgtechnology.com.br:8443/#/login')



@when('quando preencho os campos de username e password e clico em entrar')
def preencher_campos_email_senha_clicar_em_acessar(browser: Page):
    browser.locator('[type="text"]').fill(email)
    browser.locator('[type="password"]').fill(senha)
    browser.locator('[type="button"]').click()


@then('devo validar se acessei a tela home')
def usurio_deve_ser_redirecionado_tela_boas_vindas(browser: Page):
    expect(browser).to_have_url("https://app.hml.dsgtechnology.com.br:8443/#/painel")