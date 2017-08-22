Change Log
==========

Notable changes are logged here by release. This project uses `Semantic
Versioning <http://semver.org/>`__. The changelog format is inspired by
`keep-a-changelog <https://github.com/olivierlacan/keep-a-changelog>`__.

`Unreleased <https://github.com/smtg-ucl/galore/compare/0.1.0...HEAD>`__
-------------------------------------------------------------------------

-  Gaussian broadening added. In the CLI, this stacks with Lorentzian
   broadening.
-  Text file output
-  Support for PDOS plotting
-  XPS simulation mode; x-axis flipped and PDOS contributions weighted
   by cross-section.
-  Initial documentation

[0.1.0] - 2016-08-11
--------------------

Added
~~~~~

-  Initial prototype from random data
-  Convolution algorithm used to apply Lorentzian broadening
-  command-line interface
-  Plotting to screen and file
-  Test framework
-  setuptools-based distribution