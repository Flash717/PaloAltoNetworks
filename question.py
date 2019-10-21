"""
Problem Set: Out-er Space
As developers, we often interact with I/O resources. This is reflected in the
software that we write and consume (i.e. PDF readers, web browsers, IDEs,
video players, photo editors). These pieces of software often interact with
files and directories - creating, updating, modifying and deleting them.
Over time, these software applications get slower. One of the reasons why is
that the end user does not clean up the files created by these apps. As a
result, the computer that the apps run on do not have sufficient disk space
to operate effectively.
The goal of this exercise is to design algorithms that help end users
detect the space consumed by files in a fictitious root directory.
"""
from typing import List, Dict


# NOTE: Represents a root directory with sub-directories and files.
# Sub-directory -> where value in kv pair is a dictionary (i.e. root["a"])
# File -> where value in kv pair is a string (i.e. root["a"]["a.txt"])
root = {
    "a": {
        "a.txt": "hot jazz",
        "b.txt": "hot links",
        "c.txt": "hot dogs are cute and fluffy, unlike humans",
    },
    "b": {
        "a.txt": "foo jazz",
        "d.txt": "right is the right way",
        "g.txt": "help is right around the corner",
    },
    "c": {
        "d": {
            "o1.json": '{"name": "johndoe", "age": 5}',
            "o2.json": '{"name": "marydoe", "age": 30}',
            "o3.json": '{"name": "earth", "age": 1000000000}',
        },
        "e": {
            "o3.xml": "<person><name>bobdoe</name><age>55</age></person>",
            "o4.xml": "<person><name>robdoe</name><age>2</age></person>",
        },
        "o5.xml": "<tree><name>mars</name><age>1000000000</age></tree>",
    },
}


def filetype(fname: str) -> str:
    """Return filetype of given filename."""
    return fname.split(".")[-1]


def space_used(basedir: Dict) -> int:
    """Q1: Get total space for all files in basedir."""
    raise NotImplementedError("todo")


def space_used_by_filetype(basedir: Dict) -> Dict[str, int]:
    """Q2: Get total space for each filetype in basedir."""
    raise NotImplementedError("todo")


def largest_space_used_by_filetype(basedir: Dict) -> Dict[str, Dict]:
    """Q3: Get largest space for each filetype in basedir."""
    raise NotImplementedError("todo")


def files_greater_than(basedir: Dict, threshold: int) -> List[str]:
    """Q4: Get filenames in basedir whose space exceeds threshold."""
    raise NotImplementedError("todo")


def delete_files_greater_than(basedir: Dict, threshold: int) -> int:
    """Q5: Delete files in basedir whose space exceeds threshold."""
    raise NotImplementedError("todo")


# TEST SUITE
def main():
    print("running tests...")

    # test solution for Q1
    total_space = space_used(root)
    assert isinstance(total_space, int), type(total_space)
    assert total_space > 0, total_space
    assert total_space == 364, total_space

    # test solution for Q2
    space_ftype = space_used_by_filetype(root)
    assert isinstance(space_ftype, dict), type(space_ftype)
    assert all(isinstance(v, int) for v in space_ftype.values())
    assert space_ftype == {"txt": 121, "json": 95, "xml": 148}, space_ftype
    assert total_space == sum(v for v in space_ftype.values())

    # test solution for Q3
    largest_ftype = largest_space_used_by_filetype(root)
    assert isinstance(largest_ftype, dict), type(largest_ftype)
    assert all(isinstance(v, dict) for v in largest_ftype.values())
    assert largest_ftype == {
        "txt": {"name": "a/c.txt", "space": 43},
        "json": {"name": "c/d/o3.json", "space": 36},
        "xml": {"name": "c/o5.xml", "space": 51},
    }, largest_ftype

    # test solution for Q4
    space_exceeds = files_greater_than(root, 0)
    assert isinstance(space_exceeds, list), type(space_exceeds)
    assert all(isinstance(v, str) for v in space_exceeds)
    assert len(space_exceeds) == 12, len(space_exceeds)
    assert space_exceeds == [
        "a/a.txt",
        "a/b.txt",
        "a/c.txt",
        "b/a.txt",
        "b/d.txt",
        "b/g.txt",
        "c/d/o1.json",
        "c/d/o2.json",
        "c/d/o3.json",
        "c/e/o3.xml",
        "c/e/o4.xml",
        "c/o5.xml",
    ], space_exceeds
    space_exceeds = files_greater_than(root, 2 ** 32 - 1)
    assert space_exceeds == [], space_exceeds

    # test solution for Q5
    saved_space = delete_files_greater_than(root, 2 ** 32 - 1)
    updated_space = space_used(root)
    assert saved_space == 0, saved_space
    assert updated_space == total_space - saved_space
    saved_space = delete_files_greater_than(root, 0)
    updated_space = space_used(root)
    assert saved_space == total_space, saved_space
    assert updated_space == total_space - saved_space

    print("tests finished.")


main()
