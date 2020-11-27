"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
import random
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_main(self):
        """Função que testa se a saída do programa corresponde ao que foi especificado."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [str(random.randint(-100, 100))]
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            assert mock_input.call_count == 1
            mock_print.assert_called_with(
                f'O número informado foi {input_returns[0]}')


if __name__ == '__main__':
    unittest.main()
