from src.data_generator.data_types import DataTypes



class RowDataGenerator(DataTypes):
    
    def __init__(self, row_count=1) -> None:
        super().__init__()
        self.row_count = row_count
    
    def generate(self, schema):
        record = []
        for key, value in schema.items():
            obj = getattr(self,value.get("type"))()
            record.append(obj.generate(value))
        return record
