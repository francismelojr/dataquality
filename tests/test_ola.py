from app.funcao import ola


def test_imprime_ola():
    funcao = ola()
    gabarito = 'ola'
    assert funcao == gabarito
