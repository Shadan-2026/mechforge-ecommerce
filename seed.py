from store.models import Product

product_data = [
    {
        "name": "Tofu65 2.0 Aluminum Kit",
        "description": "Premium 65% gasket mount barebones keyboard kit. Aluminum CNC case.",
        "price": 14500.00
    },
    {
        "name": "Gateron Oil King Switches (90 pcs)",
        "description": "Incredibly smooth factory-lubed linear switches. 55g actuation.",
        "price": 4200.00
    },
    {
        "name": "GMK Botanical Keycaps",
        "description": "Cherry profile double-shot ABS keycaps with a minimalist nature theme.",
        "price": 11500.00
    },
    {
        "name": "Boba U4T Tactile Switches (90 pcs)",
        "description": "Highly tactile switches with a deep, thocky sound signature.",
        "price": 4500.00
    },
    {
        "name": "Keychron Q1 Pro Custom",
        "description": "75% custom wireless mechanical keyboard with a full aluminum body.",
        "price": 17500.00
    },
    {
        "name": "ePBT Kuro/Shiro Keycaps",
        "description": "Minimalist black and white PBT dye-sublimated keycaps. Crisp legends.",
        "price": 8000.00
    },
    {
        "name": "KBD8X Mark III",
        "description": "TKL form factor custom keyboard with a seamless, screwless exterior.",
        "price": 24000.00
    },
    {
        "name": "Krytox 205g0 Switch Lube",
        "description": "Premium grade switch and stabilizer lubricant (5g jar).",
        "price": 950.00
    }
]

# Loop through and add them to the database
for item in product_data:
    Product.objects.get_or_create(
        name=item["name"],
        defaults={"description": item["description"], "price": item["price"]}
    )

print("8 Custom Keyboard Products added to the database successfully!")