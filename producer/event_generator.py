import uuid
import random
from datetime import datetime, timezone
from faker import Faker

fake = Faker()

# ── Product catalogue ──────────────────────────────────
PRODUCTS = [
    {"product_id": "P001", "name": "Wireless Headphones",  "price": 2999.00},
    {"product_id": "P002", "name": "Mechanical Keyboard",  "price": 4500.00},
    {"product_id": "P003", "name": "USB-C Hub",            "price": 1299.00},
    {"product_id": "P004", "name": "Webcam HD",            "price": 3200.00},
    {"product_id": "P005", "name": "Monitor Stand",        "price": 899.00},
    {"product_id": "P006", "name": "Laptop Sleeve",        "price": 650.00},
    {"product_id": "P007", "name": "Gaming Mouse",         "price": 1800.00},
    {"product_id": "P008", "name": "SSD 1TB",              "price": 5500.00},
]

PAGES = ["/home", "/products", "/cart", "/checkout",
         "/product/detail", "/search", "/profile", "/orders"]

STATUSES = ["pending", "confirmed", "shipped", "delivered", "cancelled"]


def generate_order_event() -> dict:
    """Generate a fake order event."""
    product   = random.choice(PRODUCTS)
    quantity  = random.randint(1, 5)
    return {
        "event_type":  "order",
        "event_id":    str(uuid.uuid4()),
        "timestamp":   datetime.now(timezone.utc).isoformat(),
        "user_id":     f"U{random.randint(1000, 9999)}",
        "order_id":    f"ORD-{str(uuid.uuid4())[:8].upper()}",
        "product_id":  product["product_id"],
        "product_name":product["name"],
        "quantity":    quantity,
        "unit_price":  product["price"],
        "total_price": round(product["price"] * quantity, 2),
        "status":      random.choice(STATUSES),
        "currency":    "PHP",
        "shipping_address": {
            "city":    fake.city(),
            "region":  fake.state(),
            "country": "PH",
        },
    }


def generate_click_event() -> dict:
    """Generate a fake page click/view event."""
    return {
        "event_type":    "click",
        "event_id":      str(uuid.uuid4()),
        "timestamp":     datetime.now(timezone.utc).isoformat(),
        "user_id":       f"U{random.randint(1000, 9999)}",
        "session_id":    str(uuid.uuid4())[:8],
        "page":          random.choice(PAGES),
        "referrer":      random.choice(PAGES + [None, None]),
        "device":        random.choice(["mobile", "desktop", "tablet"]),
        "browser":       random.choice(["Chrome", "Firefox", "Safari", "Edge"]),
        "duration_ms":   random.randint(500, 30000),
    }


def generate_user_event() -> dict:
    """Generate a fake user registration/update event."""
    return {
        "event_type":  "user",
        "event_id":    str(uuid.uuid4()),
        "timestamp":   datetime.now(timezone.utc).isoformat(),
        "user_id":     f"U{random.randint(1000, 9999)}",
        "name":        fake.name(),
        "email":       fake.email(),
        "signup_date": fake.date_between(
                           start_date="-2y", end_date="today").isoformat(),
        "country":     "PH",
        "is_premium":  random.choice([True, False]),
    }


# ── Public API ─────────────────────────────────────────
EVENT_GENERATORS = {
    "orders": generate_order_event,
    "clicks": generate_click_event,
    "users":  generate_user_event,
}

def get_event(topic: str) -> dict:
    """Return a random event for the given topic name."""
    generator = EVENT_GENERATORS.get(topic)
    if not generator:
        raise ValueError(f"Unknown topic: {topic}")
    return generator()