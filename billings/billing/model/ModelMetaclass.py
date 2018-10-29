# -*- coding: utf-8 -*-
import logging
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls,name,bases,attrs)

        tablename = attrs.get('__table__', None) or name
        logging.info('found model: %s (table:%s)' % (name, tablename))

        mappings = dict()
        fields = []
        primarryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info(' found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    if primarryKey:
                        raise RuntimeError('Duplicate primary key for field: %s' % k)
                        primarryKey = k
                else:
                    fields.append(k)
        if not primarryKey:
            raise RuntimeError('Primary ket not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_field = list(map(lambda f: '`%s`' %f, fields))

        attrs['__mappings__'] = mappings # keep the relationship betweeb attribute and column
        attrs['__table__'] = tablename
        attrs['__primary_key__'] = primarryKey
        attrs['__fields__'] = fields
