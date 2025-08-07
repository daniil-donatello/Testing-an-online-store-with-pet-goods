from enum import Enum


class FoodPurpose(Enum):
    STERILIZED = 'стерилизованные'
    CASTRATES = 'кастраты'
    SENSITIVE_DIGESTION = 'чувствительное пищеварение'
    HYPOALLERGENIC = 'гипоаллергенный'
    WEIGHT_CONTROL = 'контроль веса'
    FOR_SKIN = 'для кожи/шерсти'
    ALLERGY = 'аллергия'
    HAIR_REMOVAL = 'вывод шерсти'
    FOR_ACTIVE = 'для активных'
    FOR_INDOOR_CATS = 'для кошек живущих в помещении'
    FOR_ELDERLY = 'для пожилых'
    FOR_PICKY = 'для привередливых'
    UROLITHIASIS_PREVENTION = 'профилактика МКБ'
    TARTAR_REMOVAL = 'устранение и профилактика зубного камня'
