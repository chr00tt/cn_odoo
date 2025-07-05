/** @odoo-module **/

import { registry } from "@web/core/registry";
import { kanbanView } from "@web/views/kanban/kanban_view";

export const cnKanbanView = {
    ...kanbanView,
    display_name: "看板",
};

registry.category("views").remove("kanban");
registry.category("views").add("kanban", cnKanbanView);
