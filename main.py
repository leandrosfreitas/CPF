# Importa a classe CPF e a exceção CPFInvalidoError definidas no arquivo cpf.py
from cpf import CPF, CPFInvalidoError

while True:
    cpf_digitado = input("Digite o CPF (ou 'sair' para encerrar): ").strip()

    # Se o usuário digitar "sair", encerra o loop
    if cpf_digitado.lower() == "sair":
        break

    try:
        # Tenta criar um objeto CPF
        cpf_obj = CPF(cpf_digitado)
        # Se não lançar exceção, é válido
        print(f"✅ CPF válido: {cpf_obj}")
    except CPFInvalidoError as e:
        # Captura e mostra a mensagem de erro da exceção personalizada
        print(f"❌ Erro: {e}")
