#!/usr/bin/env python

import pkg_resources as pkg
print [p.name for p in pkg.iter_entry_points("ironic.hardware.interfaces.deploy") if not p.name.startswith("fake")]
