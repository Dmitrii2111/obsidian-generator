// dashboard.js - JavaScript шаблон для дашборда
const metaedit = app.plugins.plugins["metaedit"]?.api;

const pages = dv.pages()
    .where(p => p.file && p.отдел && p.помещение)
    .sort(p => p.этаж, 'asc');

async function calcRoomStatus(page) {
    if (!page?.file?.path) return "❌ Не приступали";

    let text = await dv.io.load(page.file.path).catch(() => null);
    if (!text) return "❌ Не приступали";

    let matches = text.match(/- \[[ xX]\]/g) ?? [];
    if (matches.length === 0) return "❌ Не приступали";

    let done = matches.filter(m => /- \[[xX]\]/.test(m)).length;
    let status = "⏳ В работе";
    if (done === matches.length) status = "✅ Завершено";
    if (done === 0) status = "❌ Не приступали";

    if (metaedit) {
        await metaedit.update("status", status, page.file.path);
    }

    return status;
}

for (let [floor, floorGroup] of dv.group(pages, p => p.этаж)) {
    dv.header(2, `Этаж ${floor}`);

    let depts = dv.group(floorGroup, p => p.отдел);

    let deptRows = [];
    for (let d of depts) {
        let deptName = d.key;
        let deptFile = dv.page(`${deptName}/${deptName}`);

        let statuses = [];
        for (let r of d.rows) {
            statuses.push(await calcRoomStatus(r));
        }

        let overall = "⏳ В работе";
        if (statuses.length > 0) {
            if (statuses.every(s => s === "✅ Завершено")) {
                overall = "✅ Завершено";
            } else if (statuses.every(s => s === "❌ Не приступали")) {
                overall = "❌ Не приступали";
            } else {
                overall = "⏳ В работе";
            }
        } else {
            overall = "❌ Не приступали";
        }

        deptRows.push([
            `[[${deptFile?.file?.path ?? deptName}|${deptName}]]`,
            overall
        ]);
    }

    dv.table(["Отделение", "Статус"], deptRows);
}