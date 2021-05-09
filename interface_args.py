from abc import ABC, abstractmethod

from debug_log import p

class AbstractService(ABC):

    # abstractmethodには引数がない
    @abstractmethod
    def test(self) -> int:
        pass


class ImplService(AbstractService):

    # 具象methodには引数がある
    def test(self, a: int, b: int) -> int:
        return a + b


def print_method(service: AbstractService) -> int:
    return service.test(a=1, b=2)


service = ImplService()

test_value = print_method(service=service)

p(test_value)