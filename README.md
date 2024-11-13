# cn_odoo
Chinese Odoo (中国 Odoo)
=======================

* 主要是修正中文翻译。

由于需要覆盖翻译，需要在odoo.conf里添加以下设置：
```
overwrite_existing_translations = True
```

另外需要修改 odoo/tools/translate.py 文件的 CodeTranslations 类的 _get_po_paths 函数为：
```
    @staticmethod
    def _get_po_paths(mod, lang):
        lang_base = lang.split('_')[0]
        po_paths = [get_resource_path(mod, 'i18n', lang_base + '.po'),
                    get_resource_path(mod, 'i18n', lang + '.po'),
                    get_resource_path(mod, 'i18n_extra', lang_base + '.po'),
                    get_resource_path(mod, 'i18n_extra', lang + '.po'),
                    get_resource_path('cn_'+mod, 'i18n', lang_base + '.po'),
                    get_resource_path('cn_'+mod, 'i18n', lang + '.po'),
                    get_resource_path('cn_'+mod, 'i18n_extra', lang_base + '.po'),
                    get_resource_path('cn_'+mod, 'i18n_extra', lang + '.po'),
                    ]
        return [path for path in po_paths if path]
```
