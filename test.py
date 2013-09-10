#!/usr/bin/env python

from logentries import LogentriesHandler
import logging

log = logging.getLogger('logentries')

test = LogentriesHandler("edf701b4-c7a9-4f9d-802d-8c9dc26fca51")

log.addHandler(test)

log.warn("Warning message")

raw_input("test");
