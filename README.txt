## Project: Inventory and Order Management System for Corollary Warehousing

# === README.md ===

# Corollary Warehousing Inventory & Order Management System

A scalable, fault-tolerant inventory and order management platform designed for Corollary Warehousing by Pruhart Tech Solutions. Built with FastAPI, Celery, Redis, and custom data structures for efficiency and real-time analytics.

---

## 👤 Student Info

- **Name**: Brittney Weaver  
- **Student ID**: 012616732  
- **Python Version**: 3.11

---

## 🚀 Features

- 📦 Real-time inventory access and updates using Hash Tables and AVL Trees
- 🚚 FIFO and priority-based order processing using Queues and Heaps
- 🧠 Smart space optimization using Graphs for warehouse routing
- 📈 Real-time analytics using Pandas and FastAPI endpoints
- ⚙️ Background task processing with Celery + Redis
- 🐳 Containerized using Docker & Docker Compose

---

## 🔍 Part B3 Function Descriptions

### `InventoryManager.add_product(sku, product_info)`
Adds a product to the inventory using its SKU, stores it in a hash map, and indexes it in a balanced AVL Tree for quantity-based queries.
- **Edge Case Handling**: If a product with the same SKU already exists, it will overwrite it.

### `InventoryManager.get_product(sku)`
Fetches the product details using the SKU.
- **Edge Case Handling**: Returns `None` if SKU is not found.

### `InventoryManager.update_quantity(sku, new_quantity)`
Updates the inventory quantity for a specific SKU and rebalances the AVL Tree.
- **Edge Case Handling**: Safely does nothing if SKU is not found.

### `OrderProcessor.add_order(order, urgent=False)`
Adds an order to a FIFO queue or a min-heap depending on its urgency.
- **Edge Case Handling**: Accepts all dictionaries regardless of structure; assumes caller ensures proper schema.

### `OrderProcessor.process_next_order()`
Processes the next priority order if available, else FIFO.
- **Edge Case Handling**: Returns `None` if both queues are empty.

### `WarehouseGraphManager.shortest_path(start, end)`
Uses Dijkstra’s algorithm via `networkx` to find the optimal path between warehouse zones.
- **Edge Case Handling**: Raises `NetworkXNoPath` or `NodeNotFound` exceptions if invalid zones are given.

### `ReportGenerator.stock_report()`
Generates a pandas report summarizing inventory quantities per category.
- **Edge Case Handling**: Returns empty DataFrame if inventory is empty.

---

## 🧪 Running Part B3 Functions

### Run Inventory Functions
```python
from inventory.manager import InventoryManager
im = InventoryManager()
im.add_product("SKU001", {"name": "Widget", "quantity": 100, "category": "Tools"})
print(im.get_product("SKU001"))
im.update_quantity("SKU001", 120)
```

### Run Order Functions
```python
from order.processor import OrderProcessor
op = OrderProcessor()
op.add_order({"order_id": 101}, urgent=True)
print(op.process_next_order())
```

### Run Warehouse Graph Functions
```python
from warehouse.layout import WarehouseGraphManager
wg = WarehouseGraphManager()
wg.add_zone("A")
wg.add_zone("B")
wg.add_path("A", "B", 5)
print(wg.shortest_path("A", "B"))
```

### Run Analytics
```python
from analytics.reports import ReportGenerator
rg = ReportGenerator(im)
print(rg.stock_report())
```

---

## 🧱 Project Structure

```
├── inventory/            # Inventory management logic
│   ├── avl_tree.py       # AVL Tree structure
│   └── manager.py        # InventoryManager class
├── order/                # Order processing logic
│   └── processor.py      # OrderProcessor with FIFO + Heap
├── warehouse/            # Graph-based warehouse routing
│   └── layout.py
├── analytics/            # Reporting module
│   └── reports.py
├── services/             # Celery background task workers
│   └── restock_worker.py
├── api/                  # FastAPI REST API
│   └── app.py
├── tests/                # Unit tests
│   └── test_inventory.py
│   └── test_order.py
├── Dockerfile            # Docker image for app
├── docker-compose.yml    # Dev environment
├── requirements.txt      # Dependencies
└── README.md             # Project overview (you are here)
```

---

## ⚡ Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/your-org/corollary-inventory.git
cd corollary-inventory
```

### 2. Start the system using Docker
```bash
docker-compose up --build
```
Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

### 3. Run Tests
```bash
pytest tests/
```

---

## 🔧 Key Tech & Libraries

- Python 3.11
- FastAPI — RESTful API layer
- Celery — Async task management
- Redis — Task broker for Celery
- pandas — Reporting/analytics
- networkx — Warehouse zone routing
- Docker & docker-compose — Deployment

---

## 📬 API Overview

### Add Product
```http
POST /product/add
{
  "sku": "SKU001",
  "name": "Widget",
  "quantity": 100,
  "category": "Tools"
}
```

### Place Order
```http
POST /order
{
  "order_id": 1,
  "sku": "SKU001",
  "urgent": true
}
```

### Get Next Order
```http
GET /order/next
```

---

## 👥 Contributors

- Brittney Weaver – Lead Developer @ Pruhart Tech Solutions

---

## 📝 License

MIT License. See `LICENSE` file for details.