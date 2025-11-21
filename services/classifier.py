from typing import List, Dict
from models.FileItem import FileItem
"""
classifier takes the list of good files, then creates a new list of files with added
tags for which bucket it should go into.

if fileitem.extension in bucket, add the bucket to the file tag. return new list of tagged fileitems.


"""

class Classifier:
    def __init__(self, buckets:Dict):
        self.ext_to_buckets:Dict[str,str] = invert_bucket_dict(buckets['buckets'])

    def classify(self, file_list:List[FileItem]) -> tuple[list[FileItem], list[FileItem]]:
        classified_list = []
        unclassified_list = []

        for file in file_list:
            extension = file.extension.lower().lstrip(".")
            
            bucket = self.ext_to_buckets.get(extension)
            if bucket is None:
                unclassified_list.append(file)
            else:
                classified_list.append(file.with_tag(bucket))

        return classified_list,unclassified_list
    

def invert_bucket_dict(buckets: Dict[str,list]) -> dict[str,str]:
    inverted: Dict[str,str] = {}

    for bucket_name, extensions in buckets.items():
        for extension in extensions:
            inverted[extension.lower()] = bucket_name

    return inverted