import datetime
import pytest
from app.main import outdated_products


def test_outdated_products(monkeypatch: pytest.MonkeyPatch) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return datetime.date(2022, 2, 2)

    monkeypatch.setattr(datetime, "date", MockDate)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "egg",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 16,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160,
        },
        {
            "name": "old_beef",
            "expiration_date": datetime.date(2022, 1, 31),
            "price": 300,
        },
    ]

    result = outdated_products(products)

    assert sorted(result) == sorted(["duck", "old_beef"])
