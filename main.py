from sqlite3.dbapi2 import OperationalError
import requests
from bs4 import BeautifulSoup
from time import gmtime, sleep, time
import sqlite3
from sqlite3 import Error
# GERAR A DATA #
a = gmtime()
data_atual = f'{a[2]}/{a[1]}/{a[0]}'

# CONECTAR DB #
def DataConnect():
    path = 'C:\\python\\Banco de dados\\AutoSearcher.db'
    connect = None
    
    try:
        connect = sqlite3.connect(path)
    
    except Error as ex:
        print(f'{ex} na conexao do db')
    
    return connect

# CRIAR COLUNA DB #
def new_clmn(connection, data):
    AddQuery = """ALTER TABLE tb_precos 
                ADD COLUMN [{}];""".format(data)
    
    c = connection.cursor()
    c.execute(AddQuery)
    connection.commit()
#################################################################################################################

# UPDATE RYZEN DB
#################################################################################################################
def NewUpdateDayAMD(connection):
    
    NameProductsAMD = ['Ryzen 5 1600', 'Ryzen 5 3600','Ryzen 5 5600X', 'Ryzen 7 2700','Ryzen 7 3700X', 'Ryzen 7 3800','Ryzen 7 3800X','Ryzen 7 3800XT','Ryzen 7 5800X', 'Ryzen 9 3900X','Ryzen 9 5900X','Ryzen 9 5950X']
    
    try:
        archive = open(path(1), 'r', encoding='utf-8')
        lista_linha = archive.readlines()

        sep = []
        pre_produto = []
        produto_final = []

        for item in lista_linha:
            sep.append(item.split('%'))

        for item in sep:
            pre_produto.append(item)

        for produto in pre_produto:
            i = 0; j = 1; k = 2; l = 3
            data = produto[i][7:]
            modelo = produto[j][7:]
            preco = produto[k][10:18]
            link = produto[l][7:]
            produtos = [data, modelo, preco, link]
            produto_final.append(produtos)
            archive.close()
        
    except:
        print('erro')

    produtos_selecionadosAMD = []

    for p in range(len(produto_final)):
        for k in NameProductsAMD:
            nome_produto = produto_final[p][1]
            if k in str(nome_produto):
                produto_final[p][1] = k
                link_zuado = f'{produto_final[p][3]}'
                link_novo = link_zuado[:-1]
                produto_final[p][3] = link_novo
                produtos_selecionadosAMD.append(produto_final[p])
            else: 
                pass

    for i in range(len(produtos_selecionadosAMD)):
        for item in produtos_selecionadosAMD:
            data_para_db_AMD = produtos_selecionadosAMD[i][0]
            produto_para_db_AMD = produtos_selecionadosAMD[i][1]
            preco_para_db_AMD = produtos_selecionadosAMD[i][2]
            link_para_db_AMD = produtos_selecionadosAMD[i][3]
        
        UpdateQuery = """INSERT INTO tb_precos 
                    (PRODUTO, LINKPRODUTO, [{}])
                    VALUES('{}', '{}', '{}')
                    """.format(data_para_db_AMD, produto_para_db_AMD, link_para_db_AMD, preco_para_db_AMD)

        a = connection.cursor()
        a.execute(UpdateQuery)
        connection.commit()

#################################################################################################################
# UPDATE INTEL DB
##################################################################################################################
def NewUpdateDayINTEL(connection):
    
    NameProductsINTEL = ['Intel Core i5-9600KF', 'Intel Core i5 9600KF', 'Intel Core I5-10400','Intel Core I5 10400','Intel Core i5-10400F','Intel Core i5 10400F','Intel Core i5-10600K','Intel Core i5 10600K','Intel Core i5 10600KF','Intel Core i5-10600KF','Intel Core i5 11400','Intel Core i5-11400','Intel Core i5 11400F','Intel Core i5-11400F', 'Intel Core i7-9700F','Intel Core i7 9700F', 'Intel Core i7-9700KF','Intel Core i7 9700KF','Intel Core i7 10700','Intel Core i7-10700','Intel Core i7 10700F','Intel Core i7-10700F', 'Intel Core i7-10700K','Intel Core i7 10700K','Intel Core i7 10700KA','Intel Core i7-10700KA', 'Intel Core i9-9900K','Intel Core i9 9900K', 'Intel Core i9-10850K','Intel Core i9 10850K','Intel Core i9 10900','Intel Core i9-10900', 'Intel Core i9-10900F','Intel Core i9 10900F', 'Intel Core i9-10900X','Intel Core i9 10900X','Intel Core i9 11900K', 'Intel Core i9-11900K']               
    
    try:
        archive = open(path(2), 'r', encoding='utf-8')
        lista_linha = archive.readlines()

        sep = []
        pre_produto = []
        produto_final = []

        for item in lista_linha:
            sep.append(item.split('%'))

        for item in sep:
            pre_produto.append(item)

        for produto in pre_produto:
            i = 0; j = 1; k = 2; l = 3
            data = produto[i][7:]
            modelo = produto[j][7:]
            preco = produto[k][10:18]
            link = produto[l][7:]
            produtos = [data, modelo, preco, link]
            produto_final.append(produtos)
            archive.close()
        
    except:
        print('erro')

    produtos_selecionadosINTEL = []

    for p in range(len(produto_final)):
        for k in NameProductsINTEL:
            nome_produto = produto_final[p][1]
            if k in str(nome_produto):
                produto_final[p][1] = k
                link_zuado = f'{produto_final[p][3]}'
                link_novo = link_zuado[:-1]
                produto_final[p][3] = link_novo
                produtos_selecionadosINTEL.append(produto_final[p])
            else: 
                pass
            
    for i in range(len(produtos_selecionadosINTEL)):
        for item in produtos_selecionadosINTEL:
            data_para_db_INTEL = produtos_selecionadosINTEL[i][0]
            produto_para_db_INTEL = produtos_selecionadosINTEL[i][1]
            preco_para_db_INTEL = produtos_selecionadosINTEL[i][2]
            link_para_db_INTEL = produtos_selecionadosINTEL[i][3]
        
        UpdateQuery = """INSERT INTO tb_precos 
                    (PRODUTO, LINKPRODUTO, [{}])
                    VALUES('{}', '{}', '{}')
                    """.format(data_para_db_INTEL, produto_para_db_INTEL, link_para_db_INTEL, preco_para_db_INTEL)

        b = connection.cursor()
        b.execute(UpdateQuery)
        connection.commit()


#################################################################################################################
# UPDATE GPU DB
#################################################################################################################
def NewUpdateDayGPU(connection):

    NameProductsGPU = ['GTX 1650','GTX 1660', 'RTX 2060','RTX 3060','RTX 3070','RTX 3080','RTX 3090', 'RX 6700','RX 6800XT','RX 6900']
    
    try:
        archive = open(path(3), 'r', encoding='utf-8')
        lista_linha = archive.readlines()

        sep = []
        pre_produto = []
        produto_final = []

        for item in lista_linha:
            sep.append(item.split('%'))

        for item in sep:
            pre_produto.append(item)

        for produto in pre_produto:
            i = 0; j = 1; k = 2; l = 3
            data = produto[i][7:]
            modelo = produto[j][7:]
            preco = produto[k][10:18]
            link = produto[l][7:]
            produtos = [data, modelo, preco, link]
            produto_final.append(produtos)
            archive.close()
        
    except:
        print('erro')

    produtos_selecionadosGPU = []

    for p in range(len(produto_final)):
        for k in NameProductsGPU:
            nome_produto = produto_final[p][1]
            if k in str(nome_produto):
                produto_final[p][1] = k
                link_zuado = f'{produto_final[p][3]}'
                link_novo = link_zuado[:-1]
                produto_final[p][3] = link_novo
                produtos_selecionadosGPU.append(produto_final[p])
            else: 
                pass
    for i in range(len(produtos_selecionadosGPU)):
        for item in produtos_selecionadosGPU:
            data_para_db_GPU = produtos_selecionadosGPU[i][0]
            produto_para_db_GPU = produtos_selecionadosGPU[i][1]
            preco_para_db_GPU = produtos_selecionadosGPU[i][2]
            link_para_db_GPU = produtos_selecionadosGPU[i][3]
        
        UpdateQuery = """INSERT INTO tb_precos 
                    (PRODUTO, LINKPRODUTO, [{}])
                    VALUES('{}', '{}', '{}')
                    """.format(data_para_db_GPU, produto_para_db_GPU, link_para_db_GPU, preco_para_db_GPU)

        c = connection.cursor()
        c.execute(UpdateQuery)
        connection.commit()


#################################################################################################################
#################################################################################################################

def clear(connection, data):
    DeleteQuery = """DELETE from tb_precos"""

    c = connection.cursor()
    c.execute(DeleteQuery)
    connection.commit()

    DropQuery = """ALTER TABLE tb_precos DROP COLUMN [{}]""".format(data)
    d = connection.cursor()
    d.execute(DropQuery)
    connection.commit()

# CAMINHOS PARA OS RELATORIOS #
def path(serie):
        if serie == 1:
            path = r'C:\python\AutoSearcher\precosCPUAMD.txt'

        elif serie == 2:
            path = r'C:\python\AutoSearcher\precosCPUINT.txt'

        elif serie == 3:
            path = r'C:\python\AutoSearcher\precosGPU.txt'

        else:
            return 'Erro.'

        return path

# MENU *-* #
def menu():
    print('[1] Relatório CPU AMD')
    print('[2] Relatório CPU INTEL')
    print('[3] Relatório GPU')
    print('[4] Relatório Completo')
    print('[5] Enviar relatórios ao DB')
    # print('[6] ')
    # print('[7] ')
    print()
    print('[8] Limpar relatórios antigos')
    print('[9] Resetar banco de dados')
    print('[0] Sair do app')

    seletor = int(input('-> '))

    URL = ''

    # Seleção de AMD #
    if seletor == 1:
        URL = 'https://www.google.com/search?q=processador+amd&biw=1360&bih=657&tbm=shop&sxsrf=ALeKk02tqcjHCBIvCbHBdd7mENUjpI3TNQ%3A1628908761591&ei=2SwXYY_AI_XG5OUP-IS6wAs&oq=processador+amd&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgQIABBDUJHhAVjJ5AFgj-UBaABwAHgAgAFliAGFA5IBAzMuMZgBAKABAcABAQ&sclient=products-cc&ved=0ahUKEwjPkOyAvq_yAhV1I7kGHXiCDrgQ4dUDCAs&uact=5'
        a = gmtime()
        data = f'{a[2]}/{a[1]}/{a[0]}'
        main(URL, data, seletor=1)

    # Seleção de Intel #
    elif seletor == 2:
        URL = 'https://www.google.com/search?q=processador+intel&biw=1360&bih=657&tbm=shop&sxsrf=ALeKk01MGH5X3ykngk-9EJhTg0Abt4Z6BA:1628908599258&tbs=p_ord:r&ei=NywXYZWnD6uf5OUP9ZWeiAE&ved=0ahUKEwjVnrizva_yAhWrD7kGHfWKBxEQuw0I7QQoAA'
        a = gmtime()
        data = f'{a[2]}/{a[1]}/{a[0]}'
        main(URL, data, seletor=2)

    # Seleção de GPU #
    elif seletor == 3:
        URL = 'https://www.google.com/search?q=placa+de+video+kabum&sxsrf=ALeKk035Tdse8N0I1iOGgAo89aCxz-ASZw:1628891150480&source=lnms&tbm=shop&sa=X&sqi=2&ved=2ahUKEwjhm5uz_K7yAhUOpJUCHTsPDYUQ_AUoAXoECAEQAw&biw=1360&bih=657'
        a = gmtime()
        data = f'{a[2]}/{a[1]}/{a[0]}'
        main(URL, data, seletor=3)

    # Seleção de Todos! #
    elif seletor == 4:
        URL1 = 'https://www.google.com/search?q=processador+amd&biw=1360&bih=657&tbm=shop&sxsrf=ALeKk02tqcjHCBIvCbHBdd7mENUjpI3TNQ%3A1628908761591&ei=2SwXYY_AI_XG5OUP-IS6wAs&oq=processador+amd&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgQIABBDUJHhAVjJ5AFgj-UBaABwAHgAgAFliAGFA5IBAzMuMZgBAKABAcABAQ&sclient=products-cc&ved=0ahUKEwjPkOyAvq_yAhV1I7kGHXiCDrgQ4dUDCAs&uact=5'
        URL2 = 'https://www.google.com/search?q=processador+intel&biw=1360&bih=657&tbm=shop&sxsrf=ALeKk01MGH5X3ykngk-9EJhTg0Abt4Z6BA:1628908599258&tbs=p_ord:r&ei=NywXYZWnD6uf5OUP9ZWeiAE&ved=0ahUKEwjVnrizva_yAhWrD7kGHfWKBxEQuw0I7QQoAA'
        URL3 = 'https://www.google.com/search?q=placa+de+video+kabum&sxsrf=ALeKk035Tdse8N0I1iOGgAo89aCxz-ASZw:1628891150480&source=lnms&tbm=shop&sa=X&sqi=2&ved=2ahUKEwjhm5uz_K7yAhUOpJUCHTsPDYUQ_AUoAXoECAEQAw&biw=1360&bih=657'
        a = gmtime()
        data = f'{a[2]}/{a[1]}/{a[0]}'

        print('Realizando relatório de processadores AMD.')
        main(URL1, data, seletor=1)
        sleep(2)

        print('Realizando relatório de processadores INTEL.')
        main(URL2, data, seletor=2)
        sleep(2)

        print('Realizando relatório de Placas de vídeo.')
        main(URL3, data, seletor=3)
        sleep(2)

    # Seleção de Sair #
    elif seletor == 5:
        new_clmn(DataConnect(), data=data_atual)
        sleep(2)
        NewUpdateDayAMD(DataConnect())
        NewUpdateDayINTEL(DataConnect())
        NewUpdateDayGPU(DataConnect())
        print('Relatório enviado com sucesso.')
        sleep(2)

    # Seleção de Limpar tudo #
    elif seletor == 6:
        pass
    
    elif seletor == 7:
        pass

    elif seletor == 8:
        try:
            a = open('precosCPUAMD.txt', 'w', encoding='utf-8')
            a.write('')
            a.close()

            b = open('precosCPUINT.txt', 'w', encoding='utf-8')
            b.write('')
            b.close()

            c = open('precosGPU.txt', 'w', encoding='utf-8')
            c.write('')
            c.close()

            print('Relatórios limpos com sucesso.')
            print()
        
        except:
            pass
    
    elif seletor == 9:
        tirar_data = str(input('Data para remoção: '))
        clear(DataConnect(), tirar_data)

    elif seletor == 0:
        exit()
    
    else:
        menu()


# WEBSCRAPING #
def main(URL, data, seletor):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    placas = soup.find_all('div', class_='KZmu8e')

    for placa in placas:

        marca = placa.find('div', class_='sh-np__product-title translate-content').get_text().strip()

        preco = placa.find('span', class_='T14wmb').get_text(' // ').strip()
        
        link_href = placa.find_all('a', href=True)
        href = ''
        for tag in link_href:
            href = tag['href']
        replace_link = href.replace('amp;', '')
        final_link = f'https://www.google.com{replace_link}'

        final1 = data
        final2 = marca
        final3 = preco
        final4 = final_link

        if seletor == 1:
            try:
                a = open('precosCPUAMD.txt', 'a', encoding='utf-8')
                a.write(f'DataZZ:{final1}%Modelo:{final2}%PreçoZ:{final3}%LinkZZ:{final4}')
                a.write('\n')
                a.close()
            except:
                print('Erro: Sel = 1')

        elif seletor == 2:
            try:
                a = open('precosCPUINT.txt', 'a', encoding='utf-8')
                a.write(f'DataZZ:{final1}%Modelo:{final2}%PreçoZ:{final3}%LinkZZ:{final4}')
                a.write('\n')
                a.close()
            except:
                print('Erro: Sel = 2')

        elif seletor == 3:
            try:
                a = open('precosGPU.txt', 'a', encoding='utf-8')
                a.write(f'DataZZ:{final1}%Modelo:{final2}%PreçoZ:{final3}%LinkZZ:{final4}')
                a.write('\n')
                a.close()
            except:
                print('Erro: Sel = 3')

while True:
    print()
    menu()