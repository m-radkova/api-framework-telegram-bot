class Endpoint:
    """Базовый класс-родитель для endpoints. Содержит методы, которыми сможет пользоваться любой дочерний класс"""
    status = None
    base_url = 'https://api.telegram.org/bot'

    def check_response_status_is_ok(self):
        assert self.status == 200, f"Expected status: 200, actual status: {self.status}"
