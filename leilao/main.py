
from leilao.dominio import Usuario, Lance, Leilao

vini = Usuario("Vini", 100.0)
hugo = Usuario("Hugo", 102.0)

leilao = Leilao("Celular")

vini.propoe_lance(leilao, 100.0)
hugo.propoe_lance(leilao, 103.0)

print(vini.carteira)

# assert vini.carteira == -100.0