import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select



# setup
with open ('excelcsv\MED.csv','r', encoding = 'utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)


    for celda in csv_reader:
        
        cont = 0
        web = webdriver.Chrome()
        web.get('http://ipfl.trabajo.gba.gov.ar/alumnos/crear')

        time.sleep(1)
        # entrada de user y pass
        user = "62052201"
        pathuser  = web.find_element_by_xpath('//*[@id="id_username"]')
        pathuser.send_keys(user)

        contra = "LomasA405"
        pathcontra  = web.find_element_by_xpath('//*[@id="id_password"]')
        pathcontra.send_keys(contra)

        submit = web.find_element_by_xpath('//*[@id="submit-id-submit"]')
        submit.click()

        # ingreso de datos    
    
        pathcuil = web.find_element_by_xpath('//*[@id="id_cuil"]')
        pathcuil.send_keys(celda[0])

        pathdni = web.find_element_by_xpath ('//*[@id="id_dni"]')
        pathdni.send_keys(celda[1])

        pathnombre = web.find_element_by_xpath ('//*[@id="id_nombre"]')
        pathnombre.send_keys(celda[2])

        pathapellido = web.find_element_by_xpath ('//*[@id="id_apellido"]')
        pathapellido.send_keys(celda[3])
        
        pathclick = web.find_element_by_xpath('//*[@id="select2-id_genero-container"]')
        pathclick.click()
        
        if (celda[4] == "F"):
            pathgenero = Select(web.find_element_by_xpath('//*[@id="id_genero"]'))
            pathgenero.select_by_visible_text('FEMENINO')

        if (celda[4] == "M"):
            pathgenero = Select(web.find_element_by_xpath('//*[@id="id_genero"]'))
            pathgenero.select_by_visible_text('MASCULINO')
            
        
        pathemail = web.find_element_by_xpath ('//*[@id="id_email"]')
        pathemail.send_keys(celda[5])
        
        pathtelefono = web.find_element_by_xpath ('//*[@id="id_telefono"]')
        pathtelefono.send_keys(celda[6])

        pathfdnac = web.find_element_by_xpath ('//*[@id="id_fecha_nacimiento"]')
        pathfdnac.send_keys(celda[7])

        pathpdnac = web.find_element_by_xpath ('//*[@id="id_provincia_nacimiento"]')
        pathpdnac.send_keys(celda[8])

        pathpais = web.find_element_by_xpath ('//*[@id="id_nacionalidad"]')
        pathpais.send_keys(celda[9])

        pathdomicilio = web.find_element_by_xpath ('//*[@id="id_domicilio"]')
        pathdomicilio.send_keys(celda[10])

        pathlocalidad = web.find_element_by_xpath ('//*[@id="id_localidad"]')
        pathlocalidad.send_keys(celda[11])

        
        
        time.sleep (2)
        
        submitform = web.find_element_by_xpath('//*[@id="submit-id-submit"]')
        submitform.click()
        time.sleep(1)
        submitform = web.find_element_by_xpath('//*[@id="submit-id-submit"]')
        submitform.click()

        time.sleep(2)
    

            


        
        
       








"""




apellido = "martin"
pathapellido  = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
pathapellido.send_keys(apellido)

dni = "1231245"
pathdni  = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
pathdni.send_keys(dni)



web.get('http://ipfl.trabajo.gba.gov.ar/alumnos/crear')

time.sleep(2)

user = "62052201"
pathuser  = web.find_element_by_xpath('//*[@id="id_username"]')
pathuser.send_keys(user)

contra = "LomasA405"
pathcontra  = web.find_element_by_xpath('//*[@id="id_password"]')
pathcontra.send_keys(contra)

"""