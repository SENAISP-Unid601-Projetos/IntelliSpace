import requests

while True:
    # Solicita a URL do endpoint ao usuário
    entrada = input("Digite 1 para lampada acesa e 0 apagada:")
    url = "https://api.thingspeak.com/update?api_key=BEGIT3RV7J2IRHHT&field1="
    url += url + entrada

    try:
        # Envia a solicitação GET
        response = requests.get(url)

        # Verifica se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Se sim, imprime os dados recebidos
            print("Dados recebidos:")
            print(response.json())
        else:
            # Se não, imprime o código de status da resposta
            print("Erro ao acessar o endpoint. Código de status:", response.status_code)
    except requests.exceptions.RequestException as e:
        # Captura e imprime qualquer erro de solicitação
        print("Erro de solicitação:", e)


