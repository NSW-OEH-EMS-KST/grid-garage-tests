### grid-garage-3-test

Arcmap test for tool:

### metadata-export_metadata

***

### grid-garage-3-tests

This repository is now branch-based as test artefacts are often somewhat transient.

Use this repository by working on a test scenario fully defined within a unique branch.

Grid-Garage-3 tests under arcmap 10.4.

Each test:
- uses data found in the sample data repo https://github.com/NSW-OEH-EMS-KST/grid-garage-sample-data.git
- may use custom data which will be supplied within the branch
- is in a folder named "tool_category-tool_name"
- is comprised of an mxd (tool_name.mxd) and an fgdb (tool_name.gdb)
- tests a single tool, but may contain multiple tests
