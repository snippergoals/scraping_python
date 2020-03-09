# # -*- coding: utf-8 -*-
# # script will call all crawlers and api
# import os
# import sys
# import six
# import inspect
# from importlib import import_module
# from pkgutil import iter_modules
# import threading

# def walk_modules(path):
#     """Loads a module and all its submodules from the given module path and
#     returns them. If *any* module throws an exception while importing, that
#     exception is thrown back.
#     """
#     mods = []
#     mod = import_module(path)
#     # mods.append(mod)
#     if hasattr(mod, '__path__'):
#         for _, subpath, ispkg in iter_modules(mod.__path__):
#             fullpath = path + '.' + subpath
#             if ispkg:
#                 print(fullpath)
#                 mods += walk_modules(fullpath)
#             else:
#                 submod = import_module(fullpath)
#                 mods.append(submod)
#     return mods

# def iter_spider_classes(module):
#     """Return an iterator over all spider classes defined in the given module
#     that can be instantiated (ie. which have name)
#     """
#     # this needs to be imported here until get rid of the spider manager
#     from crawler import BaseCrawler

#     for obj in six.itervalues(vars(module)):
#         if inspect.isclass(obj) and \
#            issubclass(obj, BaseCrawler) and \
#            obj.__module__ == module.__name__:
#             return obj

# # Define a function for the thread
# class CrawlThread(threading.Thread):
#     def __init__(self, cls):
#         threading.Thread.__init__(self)
#         self.cls = cls
#     def run(self):
#         crawler = self.cls()
#         crawler.quick_test()

# mods = walk_modules('crawler')
# for submod in mods[:4]:
#     cls = iter_spider_classes(submod)
#     if cls is not None:
#         # start new thread for new crawler
#         thread = CrawlThread(cls)
#         thread.start()
#         thread.join()