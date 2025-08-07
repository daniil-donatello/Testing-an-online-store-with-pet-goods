class Checks:

    @staticmethod
    def equality(val_1, val_2):
        """
        Метод сравнения двух значений.
        :param val_1: первое значение.
        :param val_2: второе значение.
        """
        assert val_1 == val_2

    @staticmethod
    def is_true(val):
        """
        Метод проверки, что передаваемое значение is True.
        :param val: значение для сравнения.
        """
        assert val is True
