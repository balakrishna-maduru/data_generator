from src.type_generator.numeric_generator import IntegerType, DecimalType
from src.type_generator.string_generator import StringType, CharType
from src.type_generator.date_time_generator import DateType, TimestampType
from src.type_generator.boolean_generator import BooleanType

class DataTypes:
    def __init__(self) -> None:
        
        setattr(DataTypes, "IntegerType", IntegerType)
        setattr(DataTypes, "DecimalType", DecimalType)
        setattr(DataTypes, "StringType", StringType)
        setattr(DataTypes, "CharType", CharType)
        setattr(DataTypes, "DateType", DateType)
        setattr(DataTypes, "TimestampType", TimestampType)
        setattr(DataTypes, "BooleanType", BooleanType)
        