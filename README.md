# OneLogin-Event-Log-Exporter

Overview

Utilizing OneLogin's OpenAPI SDK, this is a wrapper script to pull event logs as a csv so that it can be ingested into a SIEM that doesn't support OneLogin or have direct integration.

Reference: https://github.com/onelogin/onelogin-python-sdk

Instructions:

1. `git clone` and extract .py scripts to a directory
2. Add your secrets (ideally stored in a secrets manager or password vault and shouldn't be hardcoded into the script) - maybe fork and enhance? Many thanks in advanced.
3. Modify the file path for the log output
4. Set a file watcher or configure your SIEM agent to collect from the file path.

Usage:

`./onelogin-get-events.py`
