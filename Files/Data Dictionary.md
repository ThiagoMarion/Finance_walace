| Field Name       | Data Type          | Description                                                      |
|------------------|--------------------|------------------------------------------------------------------|
| month            | string (Period: M) | Mês associado ao registro.                                       |
| cash_date        | datetime           | Data em que o registro de caixa foi efetuado.                    |
| transaction_date | datetime           | Data em que a transação ocorreu (ou ocorrerá).                   |
| value            | float              | Valor monetário da transação.                                    |
| invoice          | string             | Identificador da fatura, quando aplicável.                      |
| installment      | string             | Informação sobre parcelas, quando aplicável.                     |
| bank_description | string             | Descrição fornecida pelo banco para a transação.                 |
| description      | string             | Descrição detalhada da transação.                                |
| Category 1       | string             | Categoria primária atribuída à transação.                        |
| Category 2       | string             | Categoria secundária atribuída à transação.                      |
| recorded         | bool               | Indica se a transação já foi realizada ou está agendada.         |
| frequency        | bool               | Indica se a transação é recorrente (mensal).         |
| account          | string             | Conta associada à transação.                                     |
| tag              | string             | Etiqueta ou marcador adicional para a transação.                 |
