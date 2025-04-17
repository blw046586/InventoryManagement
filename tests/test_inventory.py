# === tests/test_inventory.py ===
def test_add_and_get_product():
    from inventory.manager import InventoryManager
    im = InventoryManager()
    im.add_product("SKU1", {"name": "Item", "quantity": 10, "category": "General"})
    assert im.get_product("SKU1")["name"] == "Item"
