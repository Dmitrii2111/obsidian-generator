// Дашборд только на основе статусов отделений
async function renderDashboard(dv) {
    // Отделения (есть "отдел", но нет "помещение")
    let departments = dv.pages().where(p => p.отдел && !p.помещение);

    let tableData = [];
    for (let dep of departments) {
        let status = dep.status || "❓ Неизвестно";
        let roomsCount = dv.pages()
            .where(p => p.отдел == dep.отдел && p.помещение).length;

        // Используем вспомогательную функцию для цвета
        let statusColored = await dv.view("js_templates/status_color", { status });

        tableData.push([dep.отдел, roomsCount, statusColored]);
    }

    dv.table(["Отделение", "Кол-во помещений", "Статус"], tableData);
}

renderDashboard(dv);
