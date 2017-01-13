# -*- coding: utf-8 -*-
formatter = "%r %r %r %s"

print formatter % (1, 2, 3, 4)
# use %s instead to print Chinese, or it'll be weird symbols
print formatter % ("one", "two", "真的", "四")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
