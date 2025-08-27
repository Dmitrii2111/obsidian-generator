// simple.js - Простые Dataview queries
function getDepartmentQuery(deptName) {
    return `TABLE WITHOUT ID file.link AS "№", помещение AS "Помещение", status AS "Статус"
WHERE отдел = "${deptName}" AND помещение
SORT file.name`;
}

function getDashboardQuery() {
    return `TABLE WITHOUT ID file.link AS "Отделение", status AS "Статус"
WHERE отдел AND NOT помещение
SORT этаж, отдел`;
}