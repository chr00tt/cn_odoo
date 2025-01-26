# cn_odoo
Chinese Odoo

主要是修正翻译。

由于需要覆盖翻译，需要在odoo.conf里添加以下设置：
```
overwrite_existing_translations = True
```

另外需要修改 odoo/tools/translate.py 文件的 get_po_paths 函数，添加这段代码：
```
    po_paths += [
        join('cn_' + module_name, dir_, filename + '.po')
        for filename in OrderedSet(po_names)
        for dir_ in ('i18n', 'i18n_extra')
    ]
```

最终的 get_po_paths 函数为：
```
def get_po_paths(module_name: str, lang: str, env: odoo.api.Environment | None = None):
    lang_base = lang.split('_')[0]
    # Load the base as a fallback in case a translation is missing:
    po_names = [lang_base, lang]
    # Exception for Spanish locales: they have two bases, es and es_419:
    if lang_base == 'es' and lang not in ('es_ES', 'es_419'):
        po_names.insert(1, 'es_419')
    po_paths = [
        join(module_name, dir_, filename + '.po')
        for filename in OrderedSet(po_names)
        for dir_ in ('i18n', 'i18n_extra')
    ]
    po_paths += [
        join('cn_' + module_name, dir_, filename + '.po')
        for filename in OrderedSet(po_names)
        for dir_ in ('i18n', 'i18n_extra')
    ]
    for path in po_paths:
        with suppress(FileNotFoundError):
            yield file_path(path, env=env)
```
