# Validador de CPF em Python 🪪

## 1. Descrição do projeto

Este projeto implementa uma **classe `CPF`** em Python para validar e formatar números de CPF de acordo com as regras da Receita Federal.  
Ele também inclui uma **exceção personalizada** (`CPFInvalidoError`) para tratar CPFs inválidos ou mal formatados.  

Funcionalidades principais:  
- Aceita CPFs nos formatos `XXX.XXX.XXX-XX` ou `XXXXXXXXXXX`.  
- Verifica se o CPF tem 11 dígitos.  
- Detecta CPFs com todos os dígitos iguais como inválidos.  
- Valida os dígitos verificadores de acordo com o algoritmo oficial.  
- Retorna o CPF formatado (`XXX.XXX.XXX-XX`).  
- Lança mensagens de erro claras quando o CPF é inválido.  

---

## 2. Como instalar e executar

1. Clone o repositório ou baixe os arquivos `cpf.py` e `main.py` para sua máquina.  

```bash
git clone <link-do-repositorio>
cd <nome-do-repositorio>
```

2. Certifique-se de ter **Python 3.8 ou superior** instalado.  

3. Execute o programa principal:

```bash
python main.py
```

4. O programa irá pedir para digitar um CPF. Digite no formato desejado ou `sair` para encerrar.

---

## 3. Exemplo de uso

```python
from cpf import CPF, CPFInvalidoError

try:
    cpf_obj = CPF("529.982.247-25")  # CPF válido
    print(f"CPF válido: {cpf_obj}")
except CPFInvalidoError as e:
    print(f"Erro: {e}")

try:
    cpf_obj = CPF("11111111111")  # CPF inválido
    print(f"CPF válido: {cpf_obj}")
except CPFInvalidoError as e:
    print(f"Erro: {e}")
```

Saída esperada:

```
CPF válido: 529.982.247-25
Erro: CPF inválido: todos os dígitos iguais.
```

---

## 4. Contribuições futuras

Algumas melhorias e funcionalidades que podem ser implementadas:  

- Implementar **validação de CPFs estrangeiros ou provisórios**.  
- Adicionar suporte para **entrada em lote** (lista de CPFs).  
- Criar uma **interface gráfica** (GUI) para facilitar o uso.  
- Incluir **testes automatizados** usando `pytest`.  
- Criar **mensagens de erro ainda mais detalhadas** dependendo do tipo de falha (tamanho incorreto, dígitos repetidos, dígito verificador incorreto).
