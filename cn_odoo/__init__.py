# -*- coding: utf-8 -*-

from os.path import join
from contextlib import suppress
from collections.abc import Iterator
from odoo.tools.misc import file_path

from odoo.tools import translate

def cn_odoo_get_po_paths(module_name: str, lang: str) -> Iterator[str]:
    po_paths = [
        join(module_name, dir_, filename + '.po')
        for filename in translate.get_base_langs(lang)
        for dir_ in ('i18n', 'i18n_extra')
    ]
    po_paths += [
        join('cn_' + module_name, dir_, filename + '.po')
        for filename in translate.get_base_langs(lang)
        for dir_ in ('i18n', 'i18n_extra')
    ]
    for path in po_paths:
        with suppress(FileNotFoundError):
            yield file_path(path)

translate.get_po_paths = cn_odoo_get_po_paths
