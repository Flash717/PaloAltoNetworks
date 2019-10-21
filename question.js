/**
 * Problem Set: Out-er Space
 * As developers, we often interact with I/O resources. This is reflected in the
 * software that we write and consume (i.e. PDF readers, web browsers, IDEs,
 * video players, photo editors). These pieces of software often interact with
 * files and directories - creating, updating, modifying and deleting them.
 * Over time, these software applications get slower. One of the reasons why is
 * that the end user does not clean up the files created by these apps. As a
 * result, the computer that the apps run on do not have sufficient disk space
 * to operate effectively.
 * The goal of this exercise is to design algorithms that help end users
 * detect the space consumed by files in a fictitious root directory.
 */

const assert = require("assert");


/**
 * NOTE: Represents a root directory with sub-directories and files.
 * Sub-directory -> where value in kv pair is a dictionary (i.e. root["a"])
 * File -> where value in kv pair is a string (i.e. root["a"]["a.txt"])
 */
const root = {
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
};


/**
 * Return filetype of given filename.
 * @param {String} fname
 */
function filetype(fname) {
    let split = fname.split(".");
    return fname.split(".")[split.length-1];
}


/**
 * Q1: Get total space for all files in basedir.
 * @param {Object} basedir
 */
function space_used(basedir) {
    throw new Error("todo");
}


/**
 * Q2: Get total space for each filetype in basedir.
 * @param {Object} basedir
 */
function space_used_by_filetype(basedir) {
    throw new Error("todo");
}


/*
 * Q3: Get largest space for each filetype in basedir.
 * @param {Object} basedir
 */
function largest_space_used_by_filetype(basedir) {
    throw new Error("todo");
}


/*
 * Q4: Get filenames in basedir whose space exceed threshold.
 * @param {Object} basedir
 * @param {Integer} threshold
 */
function files_greater_than(basedir, threshold) {
    throw new Error("todo");
}


/*
 * Q5: Delete files in basedir whose space exceeds threshold.
 * @param {Object} basedir
 * @param {Integer} threshold
 */
function delete_files_greater_than(basedir, threshold) {
    throw new Error("todo");
}


// TEST SUITE
function main() {
    console.log("run tests...");

    // test solution for Q1
    const total_space = space_used(root);
    assert(typeof(total_space) === "number");
    assert(total_space > 0);
    assert(total_space === 364);

    // test solution for Q2
    const space_ftype = space_used_by_filetype(root);
    assert(typeof(space_ftype) === "object");
    Object.values(space_ftype).forEach((v) => {
        assert(typeof(v) === "number");
    });
    assert.deepEqual(space_ftype, {"txt": 121, "json": 95, "xml": 148});

    // test solution for Q3
    const largest_ftype = largest_space_used_by_filetype(root);
    assert(typeof(space_ftype) === "object");
    Object.values(largest_ftype).forEach((v) => {
        assert(typeof(v) === "object");
    });
    assert.deepEqual(largest_ftype, {
        "txt": {"name": "a/c.txt", "space": 43},
        "json": {"name": "c/d/o3.json", "space": 36},
        "xml": {"name": "c/o5.xml", "space": 51},
    });

    // test solution for Q4
    let space_exceeds = files_greater_than(root, 0);
    assert(space_exceeds instanceof Array);
    for (let v in space_exceeds) {
        assert(typeof(v) === "string");
    }
    assert(space_exceeds.length === 12);
    assert.deepEqual(space_exceeds, [
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
    ]);
    space_exceeds = files_greater_than(root, Math.pow(2,32) - 1);
    assert.deepEqual(space_exceeds, []);

    // test solution for Q5
    let saved_space = delete_files_greater_than(root, Math.pow(2,32) - 1);
    let updated_space = space_used(root);
    assert(saved_space == 0);
    assert(updated_space == (total_space - saved_space));
    saved_space = delete_files_greater_than(root, 0);
    updated_space = space_used(root);
    assert(saved_space == total_space);
    assert(updated_space == (total_space - saved_space));

    console.log("tests finished.");
}


main();
