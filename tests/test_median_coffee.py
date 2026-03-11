from coffee_reports.reports.median_coffee import MedianCoffeeReport


def test_median_coffee_report_builds_sorted_result() -> None:
    rows = [
        {"student": "Иван", "coffee_spent": "600"},
        {"student": "Иван", "coffee_spent": "700"},
        {"student": "Иван", "coffee_spent": "650"},
        {"student": "Мария", "coffee_spent": "100"},
        {"student": "Мария", "coffee_spent": "150"},
        {"student": "Мария", "coffee_spent": "120"},
        {"student": "Павел", "coffee_spent": "380"},
        {"student": "Павел", "coffee_spent": "470"},
        {"student": "Павел", "coffee_spent": "420"},
    ]

    report = MedianCoffeeReport()
    result = report.build(rows)

    assert result == [
        {"student": "Иван", "median_coffee_spent": 650.0},
        {"student": "Павел", "median_coffee_spent": 420.0},
        {"student": "Мария", "median_coffee_spent": 120.0},
    ]