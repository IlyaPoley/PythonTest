#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium import webdriver 
driver = webdriver.Chrome(executable_path='/Users/fenix/Documents/PyTest/chromedriver')

driver.get('https://iepolei.ru')
time.sleep(2)

linkskill = driver.find_element_by_xpath('//*[@id="up"]/div/div/nav/a[2]')
linkskill.click()
time.sleep(3)

upbatton = driver.find_element_by_class_name('pageup')
upbatton.click()
time.sleep(3)

writeme = driver.find_element_by_xpath('/html/body/section[1]/div/div/div/button[1]')
writeme.click()
time.sleep(3)

writename = driver.find_element_by_xpath('/html/body/div[1]/div/form/input[1]')
writename.send_keys('Ilya')
time.sleep(2)

writephone = driver.find_element_by_xpath('/html/body/div[1]/div/form/input[2]')
writephone.send_keys('9236723149')
time.sleep(3)

writemessage = driver.find_element_by_xpath('/html/body/div[1]/div/form/p/textarea')
writemessage.send_keys('Меня зовут Илья и это мой первый проект: резюме-портфолио-полигон для моего продолжительного обучения программированию. На данном сайте представлены мой опыт работы, мои навыки, а так же мои планы по дальнейшему развитию. Прошло не мало времени, в ходе которого было проделано много работы, много ошибок и работы над ошибками, и все это позволило мне прийти к единому мнению, что программирование - это не просто работа или средство заработка, но и очень увлекательное путешествие, которое может стать длиною в жизнь. В связи с этим было принято решение познавать данную область, при этом многим пожертвовав. Данный проект, а так же параллельно и другие, будут совершенствоваться по мере повышения моей квалификации. Спасибо за внимание, и огромное спасибо, что дочитали до конца!')
time.sleep(3)

writeclose = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]')
writeclose.click()
time.sleep(2)



driver.quit()



