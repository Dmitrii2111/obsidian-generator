// department.js - JavaScript шаблон для README отделений
const metaedit = app.plugins.plugins["metaedit"]?.api;

async function main() {
  // Берём отдел из фронтматтера текущего файла
  const dept = dv.current().file.frontmatter["отдел"] ?? dv.current().file.name;

    // Фильтруем только помещения этого отделения
    const rooms = dv.pages()
    .where(p => p.отдел === dept && p.помещение)
    .map(p => dv.page(p.file.path))
    .where(p => p && p.file)
    .sort(p => p.помещение ?? p.file.name, 'asc');


  async function calcRoomStatus(page) {
    if (!page?.file?.path) return "❌ Не приступали";
    const text = await dv.io.load(page.file.path).catch(() => null);
    if (!text) return "❌ Не приступали";

    const matches = text.match(/- \[[ xX]\]/g) ?? [];
    if (matches.length === 0) return "❌ Не приступали";

    const done = matches.filter(m => /- \[[xX]\]/.test(m)).length;
    let status = "⏳ В работе";
    if (done === matches.length) status = "✅ Завершено";
    if (done === 0) status = "❌ Не приступали";

    if (metaedit) {
        await metaedit.update("status", status, page.file.path);
    }

    return status;
  }

  let rows = [];
  let statuses = [];
  for (const r of rooms.array()) {
    const status = await calcRoomStatus(r);
    const roomNum = r.file.name.replace(/\.md$/,'');
    rows.push([`[[${r.file.path}|${roomNum}]]`, r.помещение ?? r.file.name, status]);
    statuses.push(status);
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

  dv.table(
  ["Помещение", "Статус"],
  rooms.map(p => [p.file.link, p.status ?? "❌ Не указано"])
);

  if (metaedit) {
      await metaedit.update("status", overall, dv.current().file?.path);
  }
}

main();
