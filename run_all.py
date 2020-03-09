# -*- coding: utf-8 -*-
# script will call all crawlers and api
import os
import sys
import six
import inspect
from importlib import import_module
from pkgutil import iter_modules
import logging

logging.getLogger().setLevel(logging.INFO)

def walk_modules(path):
    """Loads a module and all its submodules from the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.
    """

    mods = []
    mod = import_module(path)
    # mods.append(mod)
    if hasattr(mod, '__path__'):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + '.' + subpath
            if ispkg:
                print(fullpath)
                mods += walk_modules(fullpath)
            else:
                submod = import_module(fullpath)
                mods.append(submod)
    return mods

def iter_spider_classes(module):
    """Return an iterator over all spider classes defined in the given module
    that can be instantiated (ie. which have name)
    """
    # this needs to be imported here until get rid of the spider manager
    from crawler import BaseCrawler

    for obj in six.itervalues(vars(module)):
        if inspect.isclass(obj) and \
           issubclass(obj, BaseCrawler) and \
           obj.__module__ == module.__name__:
            return obj
if len(sys.argv) < 2:
    print("Usage: `python run_all.py dev` to run it as development mode - full crawl")
    print("        `python run_all.py prod` to run it as production mode - full crawl")
    print("        `python run_all.py daily` to run it as daily mode - crawl new articles only")
    print("        * in development mode, we will cache http requests")
else:
    os.environ["NEWS_API_CRAWLER_ENV"] = sys.argv[1]
    mods = walk_modules('crawler')
    for submod in mods:
        obj = iter_spider_classes(submod)
        if obj != None:
            crawler = obj()
            crawler.run()