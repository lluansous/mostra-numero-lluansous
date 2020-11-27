"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_0(self):
        """Função que testa o 0."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['0']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O número informado foi 0')

    def test_10(self):
        """Função que testa o 10."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['10']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O número informado foi 10')

    def test_1234(self):
        """Função que testa o 1234."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['1234']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O número informado foi 1234')


if __name__ == '__main__':
    unittest.main()
