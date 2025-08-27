// room.js — обновление статуса помещения

const page = dv.current();
const filePath = page.file?.path;

if (filePath && app.plugins.plugins["metaedit"]?.api) {
    const metaedit = app.plugins.plugins["metaedit"].api;

    // Берём статус из frontmatter (если есть)
    let status = page.status;

    // Если статуса нет — ставим по умолчанию ❌
    if (!status || status.trim() === "") {
        status = "❌ Не приступали";
    }

    // Обновляем статус помещения в frontmatter
    await metaedit.update("status", status, filePath);

    // Отображаем таблицу для проверки
    dv.table(
        ["Поле", "Значение"],
        [
            ["Файл", page.file.link],
            ["Статус", status]
        ]
    );
} else {
    dv.span("❌ MetaEdit не доступен или нет пути к файлу");
}
