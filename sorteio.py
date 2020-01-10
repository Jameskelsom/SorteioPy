# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
            sleep(1)
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

        while li <= qtd:
            self.driver.find_elements_by_xpath(
                '/html/body/div[4]/div/div[2]/ul/div/li//a')[-1].location_once_scrolled_into_view
            sleep(1.2)
            li = len(self.driver.find_elements_by_xpath(
                '/html/body/div[4]/div/div[2]/ul/div/li//a'))
            print(f'Quantidade de links: {li}')

        links = self.driver.find_elements_by_xpath(
            '/html/body/div[4]/div/div[2]/ul/div/li//a')

        seguidores = []

        for link in links:
            if len(link.text) > 2:
                seguidores.append(link.text)
                print(f'Adicionando {link.text} na lista!!!')
        
        self.marcar_seguidores()

    def marcar_seguidores(self):
        self.driver.get(self.url)
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
ig.login('teste', 'teste')
# ig.fechar()


#https://www.instagram.com/p/B7I-AZHFVGL/