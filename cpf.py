import re  # Biblioteca para trabalhar com expressões regulares (regex)

# Exceção personalizada para CPF
class CPFInvalidoError(Exception):
    """Exceção levantada para CPFs inválidos ou mal formatados."""
    pass  # Não precisa implementar nada extra, apenas herda de Exception

# Classe CPF
class CPF:
    def __init__(self, cpf: str):
        # Remove qualquer caractere que não seja número
        self.cpf = re.sub(r"\D", "", cpf)

        # Verifica se o CPF tem exatamente 11 dígitos
        if len(self.cpf) != 11:
            raise CPFInvalidoError("CPF deve conter 11 dígitos numéricos.")
        
        # Verifica se todos os dígitos são iguais (ex.: 11111111111 → inválido)
        if self.cpf == self.cpf[0] * 11:
            raise CPFInvalidoError("CPF inválido: todos os dígitos iguais.")
        
        # Valida os dígitos verificadores do CPF
        if not self.validar():
            raise CPFInvalidoError("CPF inválido")
        
    def validar(self) -> bool:
        """Valida o CPF usando o cálculo oficial da Receita Federal."""
        cpf_numeros = list(map(int, self.cpf))  # Converte cada caractere em número inteiro

        # ===== Primeiro dígito verificador =====
        soma = sum(cpf_numeros[i] * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        # ===== Segundo dígito verificador =====
        soma = sum(cpf_numeros[i] * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        # Retorna True se os dois dígitos conferem
        return cpf_numeros[9] == digito1 and cpf_numeros[10] == digito2
    
    def __str__(self):
        """Retorna o CPF formatado no padrão XXX.XXX.XXX-XX"""
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
