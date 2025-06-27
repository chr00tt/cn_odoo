# cn_odoo
Chinese Odoo (中国 Odoo)
=======================

主要内容是修正中文翻译。

由于需要覆盖翻译，需要在odoo.conf里添加以下设置：
```
overwrite_existing_translations = True
```

另外需要修改 odoo/tools/translate.py 文件的 get_po_paths_env 函数：
```
@@ -1642,6 +1642,7 @@ def get_po_paths_env(module_name: str, lang: str, env: odoo.api.Environment | No
         po_names.insert(1, 'es_419')
     po_paths = (
         join(module_name, dir_, filename + '.po')
+        for module_name in (module_name, 'cn_' + module_name)
         for filename in po_names
         for dir_ in ('i18n', 'i18n_extra')
     )
```
