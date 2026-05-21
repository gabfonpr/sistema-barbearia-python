# ============================
# Sistema de Caixa da Barbearia
# ============================

# 1. Entradas (inputs)
servico = "Combo"
idade = 65
dia_semana = "Quinta-feira"

# 2. Preço base
if servico == "Cabelo":
    valor = 40
elif servico == "Barba":
    valor = 30
elif servico == "Combo":
    valor = 60

# 3. Desconto por idade
if (idade < 12 or idade > 60) and (servico == "Cabelo" or servico == "Combo"):
    valor -= 15

# 4. Promoção de terça e quarta
if dia_semana == "Terça-feira" or dia_semana == "Quarta-feira":
    valor -= 5

# 5. Quinta do combo
if dia_semana == "Quinta-feira" and servico == "Combo":
    valor -= 10

# 6. Taxa de sábado
if dia_semana == "Sábado":
    valor += 10

# 7. Resultado final
print("Serviço escolhido:", servico)
print("Idade do cliente:", idade)
print("Dia da semana:", dia_semana)
print("Valor final: R$", valor)
```
