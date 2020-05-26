#! python

# '*parameters' gera uma tupla
def calculate_final_price(gross_price, calculate_tax, *parameters):
    return gross_price + gross_price * calculate_tax(*parameters)


def tax_1(imported):
    return 0.22 if imported else 0.13


def tax_2(flammable, multiplication_factor=1):
    return 0.11 * multiplication_factor if flammable else 0


if __name__ == "__main__":
    gross_price = 134.98

    # Os valores após 'tax_1()' e 'tax_2()' referem-se aos parâmetros das respectivas funções, coletados por '*parameters'
    final_price = calculate_final_price(gross_price, tax_1, True)

    final_price = calculate_final_price(final_price, tax_2, True, 1.5)

    print('Product price (R$): %.2f' % (final_price))
