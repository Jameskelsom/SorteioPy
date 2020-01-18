# -*- coding: UTF-8 -*-
from selenium import webdriver #import driver browser
from selenium.webdriver.support.ui import WebDriverWait #import wait driver
from selenium.webdriver.common.keys import Keys #import send keys
from time import sleep
from tqdm import tqdm


class sorteio:
    def setUp(self, url, qtd):
        self.url_login = "https://www.instagram.com/accounts/login/?source=auth_switcher"
        self.url_base = "https://www.instagram.com/"
        self.url = url
        self.qtd_pessoas = qtd

    def login(self, usuario, senha):
        self.driver = webdriver.Chrome()
        d = self.driver
        d.get(self.url_login)

        i = len(d.find_elements_by_name('username'))

        while i < 1:
            sleep(1) #while element display view true
            i = len(d.find_elements_by_name('username'))

        d.find_element_by_name('username').clear()
        d.find_element_by_name('password').clear()
        d.find_element_by_name('username').send_keys(usuario)
        d.find_element_by_name('password').send_keys(senha)
        d.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

        i = len(self.driver.find_elements_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]'))

        while i < 1:
            sleep(1)
            i = len(self.driver.find_elements_by_xpath(
                '/html/body/div[4]/div/div/div[3]/button[2]'))

        self.seguidores(usuario)

    def seguidores(self, usuario):
        self.driver.get(self.url_base + usuario + '/')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()

        qtd = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text
        qtd = int(qtd.replace('.', ''))

        i = len(self.driver.find_elements_by_xpath(
            '/html/body/div[4]/div/div[1]/div/h1/div'))

        while i < 1:
            sleep(1)
            i = len(self.driver.find_elements_by_xpath(
                '/html/body/div[4]/div/div[1]/div/h1/div'))

        self.listar_seguidores(qtd)

    def listar_seguidores(self, qtd):
        li = len(self.driver.find_elements_by_xpath(
            '/html/body/div[4]/div/div[2]/ul/div/li//a'))
        qtd = 30
        while li <= qtd:
            self.driver.find_elements_by_xpath(
                '/html/body/div[4]/div/div[2]/ul/div/li//a')[-1].location_once_scrolled_into_view
            sleep(1.2)
            li = len(self.driver.find_elements_by_xpath(
                '/html/body/div[4]/div/div[2]/ul/div/li//a'))
            print(f'Quantidade de links: {li}')

        links = self.driver.find_elements_by_xpath(
            '/html/body/div[4]/div/div[2]/ul/div/li//a')

        self.seguidores = []

        for link in links:
            if len(link.text) > 2:
                self.seguidores.append(link.text)
                print(f'Adicionando {link.text} na lista!!!')
        
        self.marcar_seguidores()
        

    def marcar_seguidores(self):
        self.driver.get(self.url)
        qtd = int(len(self.seguidores)/self.qtd_pessoas)
        
        i = len(self.driver.find_elements_by_xpath(
            '/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/textarea'))

        while i < 1:
            sleep(1)
            i = len(self.driver.find_elements_by_xpath(
               '/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/textarea'))

        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').location_once_scrolled_into_view
        for i in range(qtd):
            comentario  = f'@{self.seguidores[0]} , @{self.seguidores[1]} , @{self.seguidores[2]}'
            self.seguidores.pop(0) #retirar primeiro nome
            self.seguidores.pop(1) 
            self.seguidores.pop(2) 
            print(f'Comentarios: {comentario}')
            sleep(5)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys(comentario)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/button').click()
            sleep(1)
            btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div[1]/form/button')
            while btn.get_property('disabled')== False:
                sleep(2)
            

    def deslogar(self):
        
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/div[1]/div/button').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/button[9]').click()
        self.driver.quit()


ig = sorteio()
url = str(input('Digite o endereço do sorteio: '))
qtd_pessoas = int(input('Digite a quantidade de pessoas por marcação: '))
ig.setUp(url, qtd_pessoas)
ig.login('login', 'senha')
# ig.fechar()


#https://www.instagram.com/p/B7I-AZHFVGL/
