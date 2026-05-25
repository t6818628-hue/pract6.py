const expenseTracker = {
    expenses: [],
    nextId: 1,

    addExpense(title, amount, category) {
        if (typeof title !== 'string' || title === '') {
            console.log('Ошибка: название не может быть пустым');
            return;
        }
        if (typeof amount !== 'number' || amount <= 0) {
            console.log('Ошибка: сумма должна быть положительным числом');
            return;
        }
        if (typeof category !== 'string' || category === '') {
            console.log('Ошибка: категория не может быть пустой');
            return;
        }

        const expense = {
            id: this.nextId++,
            title: title,
            amount: amount,
            category: category
        };
        this.expenses.push(expense);
        console.log('Расход добавлен:', expense);
    },

    printAllExpenses() {
        if (this.expenses.length === 0) {
            console.log('Список расходов пуст');
            return;
        }
        console.log('=== Список всех расходов ===');
        for (let i = 0; i < this.expenses.length; i++) {
            const exp = this.expenses[i];
            console.log(`ID: ${exp.id}, Название: ${exp.title}, Сумма: ${exp.amount}, Категория: ${exp.category}`);
        }
    },

    getTotalAmount() {
        let total = 0;
        for (let i = 0; i < this.expenses.length; i++) {
            total += this.expenses[i].amount;
        }
        console.log(`Общая сумма расходов: ${total}`);
        return total;
    },

    getExpensesByCategory(category) {
        if (typeof category !== 'string' || category === '') {
            console.log('Ошибка: категория не может быть пустой');
            return [];
        }
        let filtered = [];
        for (let i = 0; i < this.expenses.length; i++) {
            if (this.expenses[i].category.toLowerCase() === category.toLowerCase()) {
                filtered.push(this.expenses[i]);
            }
        }
        if (filtered.length === 0) {
            console.log(`Расходы в категории "${category}" не найдены`);
            return [];
        }
        let total = 0;
        for (let i = 0; i < filtered.length; i++) {
            total += filtered[i].amount;
        }
        console.log(`Категория: "${category}"`);
        console.log(`Количество расходов: ${filtered.length}`);
        console.log(`Общая сумма: ${total}`);
        for (let i = 0; i < filtered.length; i++) {
            const exp = filtered[i];
            console.log(`ID: ${exp.id}, Название: ${exp.title}, Сумма: ${exp.amount}`);
        }
        return filtered;
    },

    findExpenseByTitle(searchString) {
        if (typeof searchString !== 'string' || searchString === '') {
            console.log('Ошибка: строка поиска не может быть пустой');
            return null;
        }
        for (let i = 0; i < this.expenses.length; i++) {
            if (this.expenses[i].title.toLowerCase().indexOf(searchString.toLowerCase()) !== -1) {
                const found = this.expenses[i];
                console.log('Найден расход:');
                console.log(`ID: ${found.id}, Название: ${found.title}, Сумма: ${found.amount}, Категория: ${found.category}`);
                console.log('Вы можете использовать найденный расход для дальнейших действий.');
                return found;
            }
        }
        console.log(`Расход с названием, содержащим "${searchString}", не найден`);
        return null;
    },

    deleteExpenseById(id) {
        if (typeof id !== 'number' || id <= 0) {
            console.log('Ошибка: некорректный ID');
            return false;
        }
        const initialLength = this.expenses.length;
        this.expenses = this.expenses.filter(exp => exp.id !== id);
        if (this.expenses.length === initialLength) {
            console.log(`Расход с ID ${id} не найден`);
            return false;
        }
        console.log(`Расход с ID ${id} удалён`);
        return true;
    },

    getCategoryStatistics() {
        if (this.expenses.length === 0) {
            console.log('Нет расходов для статистики');
            return {};
        }
        let stats = {};
        for (let i = 0; i < this.expenses.length; i++) {
            const cat = this.expenses[i].category;
            if (!stats[cat]) {
                stats[cat] = { count: 0, total: 0 };
            }
            stats[cat].count++;
            stats[cat].total += this.expenses[i].amount;
        }
        console.log('=== Статистика по категориям ===');
        for (let category in stats) {
            console.log(`Категория: ${category}, Количество: ${stats[category].count}, Сумма: ${stats[category].total}`);
        }
        return stats;
    }
};

expenseTracker.addExpense('Кофе', 250, 'Еда');
expenseTracker.addExpense('Обед', 500, 'Еда');
expenseTracker.addExpense('Такси', 300, 'Транспорт');
expenseTracker.addExpense('Кино', 400, 'Развлечения');

expenseTracker.printAllExpenses();
expenseTracker.getTotalAmount();
expenseTracker.getExpensesByCategory('Еда');
expenseTracker.findExpenseByTitle('Кофе');
expenseTracker.deleteExpenseById(2);
expenseTracker.printAllExpenses();
expenseTracker.getCategoryStatistics();
expenseTracker.addExpense('', 100, 'Еда');
expenseTracker.addExpense('Книга', -50, 'Развлечения');
expenseTracker.addExpense('Книга', 300, '');
expenseTracker.findExpenseByTitle('');
expenseTracker.deleteExpenseById(999);