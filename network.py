#!/usr/bin/env python

import pkg_resources as pkg
print [p.name for p in pkg.iter_entry_points("ironic.hardware.interfaces.network") if not p.name.startswith("fake")]
