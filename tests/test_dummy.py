# SPDX-FileCopyrightText: 2021 Daniel Laidig <laidig@control.tu-berlin.de>
#
# SPDX-License-Identifier: MIT

import csgimu


def test_dummy():
    out = csgimu.pythonDummy()
    assert out == 42
