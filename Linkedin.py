from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random

class Linkedin_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.path = os.getcwd() + "\geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path =r"{}".format(self.path))

    def login(self):
        driver = self.driver
        driver.get('https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        time.sleep(2)
        driver.find_element_by_name('session_key').send_keys(self.username)
        driver.find_element_by_name('session_password').send_keys(self.password + Keys.RETURN)
        time.sleep(5)

    def pesquisa(self, palavrachave):
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[6]/header/div/div/div/div[1]/input').send_keys(palavrachave + Keys.RETURN)
        time.sleep(15)
        botao = driver.find_elements_by_xpath("//*[@class='search-reusables__primary-filter']")
        qtd_botao = len(botao)
    

        for i in range(0, qtd_botao):
            nome_botao = botao[i].text
            if nome_botao == 'Pessoas':
                botao[i].click()
                break
        
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    @staticmethod
    def digite_como_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,2)/60)

    def printt(self): #Este foi apenas um estudo para criar arquivo txt com dados extraidos da web.
        driver = self.driver
        with open('arquivo.txt', 'w') as arquivo:
            qtd_tag = len(driver.find_elements_by_tag_name('span'))
            print(qtd_tag)
            for cada_tag in range(0, int(qtd_tag)):
                try:
                    arquivo.write('esse é o print ' + str(cada_tag) + ' ' + driver.find_elements_by_tag_name('span')[cada_tag].text + '\n') #Lembre sempre do caraio do 'str' quando for printar ou write.
                except:
                    print('erro na tag ' + str(cada_tag) + '!')

    def cria_conexoes(self, mensagem):
        driver = self.driver
        for paginas in range(1,100):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            qtd_conexoes = len(driver.find_elements_by_class_name('reusable-search__result-container '))
            print('Quantidade de conexões nesta página é de: '+ str(qtd_conexoes))
            for cada_conexao in range(0, int(qtd_conexoes)): #contagem inicia de 0
                try:
                    driver.find_element_by_xpath('/html/body/div[6]/aside/div[2]/header/section[2]/button[3]').click() #Se tiver algum chat aberto, o que atrapalha as conexões, será fechado
                except:
                    pass
                
                #Confere se é conexão, ou apenas para seguir, mensagem entre outros
                nome_botao_conexao = driver.find_element_by_xpath("//*[@class='reusable-search__result-container '][{}]//*[@class='artdeco-button__text']".format(cada_conexao + 1)).text # Por algum motivo, a pesquisa neste formado de fato inicia com o numero 1 ao invés de 0
                nome_da_conexao = driver.find_elements_by_class_name('reusable-search__result-container ')[cada_conexao].find_element_by_xpath('div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text
                print('Verificando conexão com {}'.format(nome_da_conexao))

                if nome_botao_conexao == 'Conectar':
                    try:
                        texto_frase = 'Olá, ' + nome_da_conexao + ', tudo bem? ' + mensagem
                        time.sleep(1)
                        driver.find_element_by_xpath("//*[@class='reusable-search__result-container '][{}]//*[@class='artdeco-button__text']".format(cada_conexao + 1)).click()
                        #driver.find_elements_by_class_name('reusable-search__result-container ')[cada_conexao].find_element_by_xpath('div/div/div[3]/div/button/span').click()
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]/span').click()
                        local_onde_digitar = driver.find_element_by_id('custom-message')
                        self.digite_como_pessoa(texto_frase, local_onde_digitar)
                        time.sleep(random.randint(1, 3))
                        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]/span').click()
                        time.sleep(2)

                    except:
                        nome_da_conexao = driver.find_elements_by_class_name('reusable-search__result-container ')[cada_conexao].find_element_by_xpath('div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text
                        print('Erro ao conectar com ' + nome_da_conexao + '!')
                else:
                    print('não foi possível conectar com {}'.format(nome_da_conexao))


            qtd_tag = len(driver.find_elements_by_tag_name('span'))
            for cada_tag in range(0, int(qtd_tag)):
                try:
                    if driver.find_elements_by_tag_name('span')[cada_tag].text == 'Avançar':
                        driver.find_elements_by_tag_name('span')[cada_tag].click()
                except:
                    print(str(cada_tag))




        


if __name__ == '__main__':
    boot = Linkedin_bot('seuemail@gmail.com','suasenha')
    boot.login()
    boot.pesquisa('cargo a ser pesquisado')
    boot.cria_conexoes('complementação da sua mensagem para a conexão')
