# Bonus round

Following topics are considered 'Bonus' features:

- File cleanup utility that makes use of metadata about space and created/modified time
- File distribution across multiple VMs, where each VM has different space requirements
- Support content search across multiple files, using an algorithm like TF-IDF
- File similarity calculations

--- 
### File cleanup
The file `file_cleanup.py` contains a basic solution to scan a root-folder and its subfolders for possible candidates to be deleted using space and age in days as criteria.   
However, there may be the need to not immediately delete files but identify candidates, notify owners and delete the file after a certain grace period. In this case the files would need to be flagged as 'to be deleted' with a grace expiration date. A simple SQL database would be sufficient for tracking files and their status.

---
### File distribution across VMs
Based on the given requirements there is a need to store the VMs' information like space requirements, name, location, etc. This could be accomplished with a file or simple database table. There could also be additional meta-information stored for each VM so that file distribution can be specified to certain groups of VMs. Before distribution of a file each VM needs to be checked for proper space requirements. There could be a requirement to check first all VMs and only distribute if all are available, or distribute where possible and return a list of VMs that lack requirements.

---
### Support content search
In order to support content search through algorithms like TF-IDF we need information about total count of words and word-frequency for each file. This infomation can be scanned and stored upon saving a file (or run an initial indexing process). Tries are a good data structure for searching words, the individual file-name and word-frequency can be cached for fast lookup (especially frequent search terms). For long term storage of these indicators we can use a SQL database, to support growth of the data volume sharding is a possible solution (shard by terms, frequencies, etc.)

---
### File similarity calculations
This can build on the TF-IDF algorithm above by using frequency of words and their inverse document frequency to find commonalities. Large common sequences between files can be a good indicator for file similarity (the longer the commonality, the greater the match). Similar to above, hash-tables are good for lookup and caching.
