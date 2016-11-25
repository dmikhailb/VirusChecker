# VirusChecker

The MVP version of a virus checker that uses ClamAV to check uploaded files.

CURL command to send files:
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file_to_scan=@testfile" <URI>/scanner/api/v1.0/file-scanner
