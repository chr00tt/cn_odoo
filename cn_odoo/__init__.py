# -*- coding: utf-8 -*-

from contextlib import suppress
from os.path import join

import odoo
from odoo.tools.misc import file_path

from odoo.tools import translate

def cn_odoo_get_po_paths_env(module_name: str, lang: str, env: odoo.api.Environment | None = None):
    lang_base = lang.split('_', 1)[0]
    # Load the base as a fallback in case a translation is missing:
    po_names = [lang_base, lang]
    # Exception for Spanish locales: they have two bases, es and es_419:
    if lang_base == 'es' and lang not in ('es_ES', 'es_419'):
        po_names.insert(1, 'es_419')
    po_paths = (
        join(module_name, dir_, filename + '.po')
        # 同时考虑 <模块名> 和 cn_<模块名>:
        for module_name in (module_name, 'cn_' + module_name)
        for filename in po_names
        for dir_ in ('i18n', 'i18n_extra')
    )
    for path in po_paths:
        with suppress(FileNotFoundError):
            yield file_path(path, env=env)

translate.get_po_paths_env = cn_odoo_get_po_paths_env
