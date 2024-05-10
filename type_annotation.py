class Product:
    def __init__(
            self,
            title: str,
            description: str,
            width: int,
            height: int,
            price: float,
            currency: str,
            colors: list,
            image: str,
            video: str,
            isSold: bool,
            discount: float,
            deliveryProviders: dict,
            materials: dict,
            tags: tuple
        ):
        self.title = title
        self.description = description
        self.width = width
        self.height = height
        self.price = price
        self.currency = currency
        self.colors = colors
        self.image = image
        self.video = video
        self.isSold = isSold
        self.discount = discount
        self.deliveryProviders = deliveryProviders
        self.materials = materials
        self.tags = tags


    def getAvailableColors(self) -> list:
        return self.colors

    def getPrice(self) -> str:
        return f"{self.price} {self.currency}"

    def calculateDiscount(self) -> float:
        return round((self.price * self.discount) / 100, 2)
    

title = "Blanket Throw with Xmas Moose Poinsettias Pattern"
description = """
    Stay warm with KEMUSI's new Holiday collection featuring the classic Canadian style 
    Moose and Poinsettias pattern Christmas fleece blanket. 
    This super soft multipurpose throw blanket will enhance your home decor and is suitable 
    for all seasons. Charcoal Grey color with White Elks, lined with Red Maple leaves a tiny blue 
    and white Geometry pattern. This Stunning Elk fleece blanket can be used as a throw for your 
    living room sofa, bedding or will make a great gift.
"""
width = 150
height = 200
price = 50
currency = 'USD'
colors = ["grey", "blue", "red"]
image = "https://m.media-amazon.com/images/I/81eEo+9-vkL._AC_SX679_.jpg"
video = None 
isSold = False
discount = 2.7
deliveryProviders = {
    "provider1": { "phone": "+1122334455", "email": "delivery1@email.com" },
    "provider2": { "phone": "+8822334455", "email": "delivery2@email.com" }
}
materials = {
    "poliester": 90,
    "cotton": 10
}
tags = ("winter", "home", "blanket", "cozy", "christmas")


christmasBlanket = Product(
    title, 
    description, 
    width, 
    height, 
    price, 
    currency, 
    colors, 
    image, 
    video, 
    isSold, 
    discount, 
    deliveryProviders, 
    materials, 
    tags
)

# get blanket price
productPrice = christmasBlanket.getPrice()
print("Price: ", productPrice)

# get discount
myDiscount = christmasBlanket.calculateDiscount()
print("Discount ($): ", myDiscount)

# check if red blanket is available
availableColors = christmasBlanket.getAvailableColors()
if "red" in availableColors:
    print("Red blanket is available")