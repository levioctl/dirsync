import os

import printer
import treeprinter
import replicas_from_args
import interactive_dir_sync
import search_supplement_replicas


def sync_from_src_to_dst(src, dst):
    dirsync = interactive_dir_sync.InteractiveDirSync(src, dst)
    dirsync.sync()


def sync(replica_a, replica_b):
    sync_from_src_to_dst(src=replica_a, dst=replica_b)
    sync_from_src_to_dst(src=replica_b, dst=replica_a)


def main():
    replica_a_path, replica_b_path = replicas_from_args.get()
    replica_a_path, replica_b_path = search_supplement_replicas.search(replica_a_path, replica_b_path)
    sync(replica_a_path, replica_b_path)


if __name__ == "__main__":
    if os.getenv('MODE') == 'interactive':
        printer.wrapper(main)
    else:
        main()
