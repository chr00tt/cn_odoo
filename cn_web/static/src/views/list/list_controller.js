/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { ListController } from "@web/views/list/list_controller";
import {
    deleteConfirmationMessage,
    ConfirmationDialog,
} from "@web/core/confirmation_dialog/confirmation_dialog";

// -----------------------------------------------------------------------------

patch(ListController.prototype, {
    get deleteConfirmationDialogProps() {
        const root = this.model.root;
        let body = deleteConfirmationMessage;
        if (root.isDomainSelected || root.selection.length > 1) {
            body = _t("Are you sure you want to delete these records?");
        }
        return {
            title: _t("Bye-bye, record!"),
            body,
            confirmLabel: _t("Confirm"),
            confirm: () => this.model.root.deleteRecords(),
            cancel: () => {},
            cancelLabel: _t("No, keep it"),
        };
    }
});
