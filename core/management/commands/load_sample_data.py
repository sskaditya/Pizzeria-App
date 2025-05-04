from django.core.management.base import BaseCommand
from core.models import Category, MenuItem
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Loads sample data for the pizzeria app"

    def handle(self, *args, **options):
        # Create superuser if none exists
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
            self.stdout.write(
                self.style.SUCCESS("Superuser created: admin/adminpassword")
            )

        # Create categories
        categories = [
            {"name": "Classic Pizzas"},
            {"name": "Specialty Pizzas"},
            {"name": "Sides"},
            {"name": "Drinks"},
            {"name": "Desserts"},
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(**category_data)
            status = "Created" if created else "Already exists"
            self.stdout.write(f"{status}: {category.name}")

        # Menu items for Classic Pizzas
        classic_pizzas = [
            {
                "name": "Margherita",
                "description": "Classic pizza with tomato sauce, mozzarella, fresh basil, salt, and extra-virgin olive oil.",
                "price": 10.99,
                "category": Category.objects.get(name="Classic Pizzas"),
            },
            {
                "name": "Pepperoni",
                "description": "Tomato sauce, mozzarella, and pepperoni slices. A timeless favorite!",
                "price": 12.99,
                "category": Category.objects.get(name="Classic Pizzas"),
            },
            {
                "name": "Cheese Pizza",
                "description": "Simple yet delicious blend of tomato sauce and our signature cheese mix.",
                "price": 9.99,
                "category": Category.objects.get(name="Classic Pizzas"),
            },
            {
                "name": "Veggie",
                "description": "Loaded with bell peppers, mushrooms, onions, olives, and tomatoes on our signature sauce.",
                "price": 13.99,
                "category": Category.objects.get(name="Classic Pizzas"),
            },
        ]

        # Menu items for Specialty Pizzas
        specialty_pizzas = [
            {
                "name": "BBQ Chicken",
                "description": "Grilled chicken, BBQ sauce, red onions, and cilantro make this a customer favorite.",
                "price": 15.99,
                "category": Category.objects.get(name="Specialty Pizzas"),
            },
            {
                "name": "Buffalo Ranch",
                "description": "Spicy buffalo chicken, ranch drizzle, mozzarella and blue cheese crumbles.",
                "price": 15.99,
                "category": Category.objects.get(name="Specialty Pizzas"),
            },
            {
                "name": "Mediterranean",
                "description": "Feta cheese, olives, sun-dried tomatoes, spinach, and a special herb blend.",
                "price": 14.99,
                "category": Category.objects.get(name="Specialty Pizzas"),
            },
            {
                "name": "Supreme",
                "description": "The ultimate combo of pepperoni, sausage, bell peppers, onions, and olives.",
                "price": 16.99,
                "category": Category.objects.get(name="Specialty Pizzas"),
            },
            {
                "name": "Meat Lovers",
                "description": "For the carnivore: pepperoni, sausage, bacon, ham, and ground beef.",
                "price": 17.99,
                "category": Category.objects.get(name="Specialty Pizzas"),
            },
        ]

        # Menu items for Sides
        sides = [
            {
                "name": "Garlic Breadsticks",
                "description": "Freshly baked breadsticks brushed with garlic butter and herbs. Served with marinara sauce.",
                "price": 5.99,
                "category": Category.objects.get(name="Sides"),
            },
            {
                "name": "Chicken Wings",
                "description": "Eight wings tossed in your choice of sauce: Buffalo, BBQ, or Plain with dipping sauce.",
                "price": 9.99,
                "category": Category.objects.get(name="Sides"),
            },
            {
                "name": "Cheese Sticks",
                "description": "Golden-fried mozzarella sticks served with marinara sauce.",
                "price": 6.99,
                "category": Category.objects.get(name="Sides"),
            },
            {
                "name": "Caesar Salad",
                "description": "Crisp romaine, parmesan cheese, croutons, and Caesar dressing.",
                "price": 7.99,
                "category": Category.objects.get(name="Sides"),
            },
        ]

        # Menu items for Drinks
        drinks = [
            {
                "name": "Soda (20oz)",
                "description": "Your choice of Coke, Diet Coke, Sprite, or Dr Pepper.",
                "price": 2.49,
                "category": Category.objects.get(name="Drinks"),
            },
            {
                "name": "Iced Tea",
                "description": "Freshly brewed unsweetened iced tea.",
                "price": 2.49,
                "category": Category.objects.get(name="Drinks"),
            },
            {
                "name": "Bottled Water",
                "description": "Refreshing purified water.",
                "price": 1.99,
                "category": Category.objects.get(name="Drinks"),
            },
            {
                "name": "2-Liter Soda",
                "description": "Your choice of Coke, Diet Coke, Sprite, or Dr Pepper.",
                "price": 3.99,
                "category": Category.objects.get(name="Drinks"),
            },
        ]

        # Menu items for Desserts
        desserts = [
            {
                "name": "Chocolate Chip Cookie",
                "description": "Large warm chocolate chip cookie. Enough to share, but you won't want to!",
                "price": 5.99,
                "category": Category.objects.get(name="Desserts"),
            },
            {
                "name": "Cinnamon Sticks",
                "description": "Freshly baked sticks topped with cinnamon and sugar, served with sweet icing.",
                "price": 5.99,
                "category": Category.objects.get(name="Desserts"),
            },
            {
                "name": "Chocolate Brownie",
                "description": "Rich, fudgy brownie with chocolate chips throughout.",
                "price": 4.99,
                "category": Category.objects.get(name="Desserts"),
            },
        ]

        # Combine all menu items
        all_items = classic_pizzas + specialty_pizzas + sides + drinks + desserts

        # Create menu items
        for item_data in all_items:
            item, created = MenuItem.objects.get_or_create(
                name=item_data["name"],
                defaults={
                    "description": item_data["description"],
                    "price": item_data["price"],
                    "category": item_data["category"],
                },
            )
            status = "Created" if created else "Already exists"
            self.stdout.write(f"{status}: {item.name} (${item.price})")

        self.stdout.write(self.style.SUCCESS("Successfully loaded sample data"))
