import tkinter as tk
from tkinter import messagebox

class Product:
    """Представляет товар на складе."""
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity: int) -> None:
        """Устанавливает новое количество товара."""
        self.quantity = new_quantity

    def __str__(self) -> str:
        return f"{self.name} — {self.quantity} шт. — {self.price} руб."


class Warehouse:
    """Управляет списком товаров."""
    def __init__(self):
        self.products: list[Product] = []

    def _find_product_index(self, name: str) -> int:
        """Возвращает индекс товара по имени или выбрасывает ValueError."""
        for i, product in enumerate(self.products):
            if product.name == name:
                return i
        raise ValueError(f"Товар '{name}' не найден.")

    def add_product(self, name: str, quantity: int, price: float) -> None:
        """Добавляет новый товар, проверяя отсутствие дубликата."""
        try:
            self._find_product_index(name)
            raise ValueError(f"Товар '{name}' уже существует.")
        except ValueError as e:
            if "не найден" not in str(e):
                raise e
        self.products.append(Product(name, quantity, price))

    def remove_product(self, name: str) -> None:
        """Удаляет товар по имени."""
        index = self._find_product_index(name)
        self.products.pop(index)

    def update_quantity(self, name: str, new_quantity: int) -> None:
        """Обновляет количество товара."""
        index = self._find_product_index(name)
        self.products[index].update_quantity(new_quantity)

    def list_products(self) -> str:
        """Возвращает строковое представление всех товаров."""
        if not self.products:
            return "Склад пуст."
        return "\n".join(str(p) for p in self.products)

    def total_inventory_value(self) -> float:
        """Вычисляет общую стоимость всех товаров."""
        return sum(p.price * p.quantity for p in self.products)


class WarehouseApp:
    """Графическое приложение для управления складом."""
    def __init__(self, master):
        self.master = master
        master.title("Управление складом")
        master.geometry("500x600")
        master.resizable(False, False)

        self.warehouse = Warehouse()

        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе")
        self.status_label = tk.Label(master, textvariable=self.status_var,
                                     relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=2)

        input_frame = tk.Frame(master)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Название:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Количество:").grid(row=1, column=0, sticky=tk.W)
        self.quantity_entry = tk.Entry(input_frame, width=30)
        self.quantity_entry.grid(row=1, column=1, padx=5)

        tk.Label(input_frame, text="Цена (руб):").grid(row=2, column=0, sticky=tk.W)
        self.price_entry = tk.Entry(input_frame, width=30)
        self.price_entry.grid(row=2, column=1, padx=5)

        button_frame = tk.Frame(master)
        button_frame.pack(pady=5)

        btn_width = 15
        self.add_button = tk.Button(button_frame, text="Добавить", width=btn_width,
                                    command=self.add_product)
        self.add_button.grid(row=0, column=0, padx=2, pady=2)

        self.remove_button = tk.Button(button_frame, text="Удалить", width=btn_width,
                                       command=self.remove_product)
        self.remove_button.grid(row=0, column=1, padx=2, pady=2)

        self.update_button = tk.Button(button_frame, text="Изменить кол-во", width=btn_width,
                                       command=self.update_product)
        self.update_button.grid(row=1, column=0, padx=2, pady=2)

        self.show_button = tk.Button(button_frame, text="Показать всё", width=btn_width,
                                     command=self.show_products)
        self.show_button.grid(row=1, column=1, padx=2, pady=2)

        display_frame = tk.Frame(master)
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(display_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.product_display = tk.Text(display_frame, height=15,
                                        yscrollcommand=scrollbar.set)
        self.product_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.product_display.yview)

        self.warehouse.add_product("Ноутбук", 3, 50000)
        self.warehouse.add_product("Мышь", 10, 1500)
        self._update_display()

    def _update_display(self) -> None:
        """Обновляет текстовое поле и строку состояния."""
        self.product_display.delete(1.0, tk.END)
        products_str = self.warehouse.list_products()
        self.product_display.insert(tk.END, products_str)

        count = len(self.warehouse.products)
        total = self.warehouse.total_inventory_value()
        self.status_var.set(f"Товаров: {count} | Общая стоимость: {total:.2f} руб.")

    def _clear_inputs(self) -> None:
        """Очищает поля ввода."""
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def add_product(self) -> None:
        """Добавляет новый товар."""
        try:
            name = self.name_entry.get().strip()
            if not name:
                raise ValueError("Название товара не может быть пустым.")

            quantity_str = self.quantity_entry.get().strip()
            if not quantity_str:
                raise ValueError("Введите количество.")
            try:
                quantity = int(quantity_str)
            except ValueError:
                raise ValueError("Количество должно быть целым числом.")
            if quantity < 0:
                raise ValueError("Количество не может быть отрицательным.")

            price_str = self.price_entry.get().strip()
            if not price_str:
                raise ValueError("Введите цену.")
            try:
                price = float(price_str)
            except ValueError:
                raise ValueError("Цена должна быть числом.")
            if price < 0:
                raise ValueError("Цена не может быть отрицательной.")

            self.warehouse.add_product(name, quantity, price)
            self._update_display()
            self._clear_inputs()
            self.status_var.set(f"Товар '{name}' добавлен.")
        except ValueError as e:
            self.status_var.set(f"Ошибка: {e}")

    def remove_product(self) -> None:
        """Удаляет товар по имени."""
        try:
            name = self.name_entry.get().strip()
            if not name:
                raise ValueError("Введите название товара для удаления.")

            if not messagebox.askyesno("Подтверждение", f"Удалить товар '{name}'?"):
                return

            self.warehouse.remove_product(name)
            self._update_display()
            self._clear_inputs()
            self.status_var.set(f"Товар '{name}' удалён.")
        except ValueError as e:
            self.status_var.set(f"Ошибка: {e}")

    def update_product(self) -> None:
        """Обновляет количество товара."""
        try:
            name = self.name_entry.get().strip()
            if not name:
                raise ValueError("Введите название товара.")

            quantity_str = self.quantity_entry.get().strip()
            if not quantity_str:
                raise ValueError("Введите новое количество.")
            try:
                new_quantity = int(quantity_str)
            except ValueError:
                raise ValueError("Количество должно быть целым числом.")
            if new_quantity < 0:
                raise ValueError("Количество не может быть отрицательным.")

            self.warehouse.update_quantity(name, new_quantity)
            self._update_display()
            self._clear_inputs()
            self.status_var.set(f"Количество товара '{name}' обновлено.")
        except ValueError as e:
            self.status_var.set(f"Ошибка: {e}")

    def show_products(self) -> None:
        """Обновляет отображение списка товаров."""
        self._update_display()
        self.status_var.set("Список товаров обновлён.")


def main():
    root = tk.Tk()
    app = WarehouseApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()