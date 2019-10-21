import sys
import os
import time

DEFAULT_THRESHOLD = 1024 * 1024 * 1024 * 1024   # Gigabyte
DEFAULT_DAYS_OLD = 365 * 10
DEFAULT_DELETE = False

def file_cleanup(basedir: str, space_threshold: int, maxage_days: int, delete_file: bool):
    if not os.path.exists(basedir) and not os.path.isdir(basedir):
        print('{} does not exist or is not a directory, ending operation'.format(basedir))
        return
    for i in os.listdir(basedir):
        filename = basedir + '/' + i
        if os.path.isdir(filename):
            file_cleanup(filename, space_threshold, maxage_days, delete_file)
        else:
            file_stat = os.stat(filename)
            space = file_stat.st_size
            age_in_days = (time.time() - file_stat.st_mtime) / (60 * 60 * 24)
            if delete_file:
                try:
                    os.remove(filename)
                    print('removed file {}, size: {} bytes, age: {} days'.format(
                        filename, space, age_in_days))
                except Exception as e:
                    print('could not delete file {}, error {}'.format(filename, e))
            else:
                print('to-be removed file {}, size: {} bytes, age: {} days'.format(
                    filename, space, age_in_days))
                

def main():
    root_dir = '.' if len(sys.argv) <= 1 else sys.argv[1]
    if root_dir in ['--help', '-h']:
        print('python file_cleanup.py <root_directory> <space_threshold> <days_old> <delete_files>')
        return
    space_threshold = DEFAULT_THRESHOLD if len(sys.argv) <= 2 else sys.argv[2]
    maxage_days = DEFAULT_DAYS_OLD if len(sys.argv) <= 3 else sys.argv[3]
    delete_file = DEFAULT_DELETE if len(sys.argv) <= 4 else sys.argv[4].lower() == 'true'

    file_cleanup(root_dir, space_threshold, maxage_days, delete_file)


if __name__ == '__main__':
    main()
