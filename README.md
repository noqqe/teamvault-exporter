# teamvault-exporter
Exports all entries from a teamvault instance


What this script does:
* exports all secret entries
* exports only secrets that are available to the current user.
* finds the LATEST revision of the password
* writs a CUSTOM json as output.

What this script does NOT:
* exporting ALL versions (past versions) of a secret
* exporting uploaded files from teamvault
