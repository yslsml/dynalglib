class Item:
    def __init__(
        self,
        name: str | int,
        weight: int = 1,
        value: int = 1,
        quantity: int = 1,
    ) -> None:
        self.name = name
        self.weight = weight
        self.value = value
        self.quantity = quantity

    def __str__(self) -> str:
        return (
            "n={}\t".format(self.name)
            + "w={}\t".format(self.weight)
            + "v={}\t".format(self.value)
            + "q={}".format(self.quantity)
        )
