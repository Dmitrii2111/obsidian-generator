// Утилита: возвращает HTML для окраски статуса
async function renderColor(dv, input) {
    let status = input.status || "❓ Неизвестно";

    if (status.includes("❌")) return "<span style='color:red'>" + status + "</span>";
    if (status.includes("⏳")) return "<span style='color:orange'>" + status + "</span>";
    if (status.includes("✅")) return "<span style='color:green'>" + status + "</span>";

    return status;
}

module.exports = renderColor;
