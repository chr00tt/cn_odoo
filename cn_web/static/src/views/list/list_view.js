/** @odoo-module */

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";

export const cnListView = {
    ...listView,
    display_name: "列表",
};

registry.category("views").remove("list");
registry.category("views").add("list", cnListView);
