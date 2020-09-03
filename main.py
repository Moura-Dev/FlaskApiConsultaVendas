import psycopg2


def inserirdados():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="jYMoiF21Yw8KzWNYRSsc",
                                      host="database-teste.c0rzxyeauhjq.us-east-1.rds.amazonaws.com",
                                      port="5432",
                                      database="postgres",)
        cursor = connection.cursor()

        with open("VENDAS_CARTAO.txt", "r") as data:
            contador = 0
            for line in data:
                contador += 1
                valores = [
                    item.strip(' ') for item in line.split()]
                if valores[1] == 'PAR':
                    valores.pop(1)
                    valores.pop(0)
                    valores.insert(0, "VENDA PAR")
                tipo_transacao = valores[0]
                documento = valores[1]
                empresa = valores[2]
                moeda = valores[3]
                valor_bruto = valores[4]
                valor_liquido = valores[5]
                taxa_adm = valores[6]
                adquirente = valores[7]
                bandeira = valores[8]
                produto = valores[9]
                meio_captura = valores[10]
                filial = valores[11]
                data_transacao = '2020-08-26'    #Resposta Mockava, Erro no Banco ao executar current_date

                cursor.execute("""INSERT INTO vendas_adquirente (tipo_transacao, documento, empresa, moeda, valor_bruto, valor_liquido,
                                    taxa_adm, data_transacao, adquirente, bandeira, produto, meio_captura ,filial)
                                    VALUES(%s, %s, %s, %s, %s, %s , %s , %s, %s , %s, %s, %s, %s)""",
                               (tipo_transacao, documento, empresa, moeda, valor_bruto, valor_liquido, taxa_adm, data_transacao,
                               adquirente, bandeira, produto, meio_captura, filial))
                print(valores)
                #connection.commit()
                with open("log.txt", "w") as log:
                    log.write('Quantidade de registros gravadas : {} '.format(contador))

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #Fechando Conexao Banco de dados
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


inserirdados()
