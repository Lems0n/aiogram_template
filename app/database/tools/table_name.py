from sqlalchemy.ext.declarative import declared_attr



class CreateTableName:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        name = str(cls.__name__.lower())
        if name.endswith("orm"):
            name = name[:-3]
        elif name.endswith("table"):
            name = name[:-5]
        return name + "s"
    