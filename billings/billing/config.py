# -*- coding: utf-8 -*-
from heapq import merge
from billing import config_default, config_override


configs =config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass