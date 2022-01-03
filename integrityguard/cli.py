import sys
import click
from integrityguard.helpers.loadconfig import load_config
from integrityguard.helpers.showpaths import show_paths
from integrityguard.helpers.copyconfig import copy_config
from integrityguard.hashreport import hash_report
from integrityguard.monitor import monitor

# Load configuration
config = load_config()

# Get root path to scan
path = config['monitor']['target_path']

# Get hash type
hash_type = config['hash']['hash_type'].lower()

@click.command()
@click.option('--task', default="monitor", help='Tasks available: monitor, generate_hashes')
@click.option('--target', default=path, help='Target path to monitor')
@click.option('--config', default="", help='Full path to .conf file')
@click.option('--hash', default="", help='Hash algorithm type (MD5, SHA1, SHA224, SHA256, SHA384, and SHA512).')
@click.option('--destination', default="", help='Used for copy_config task. Full destination path of the .conf file.')

def main(task,target,config,hash,destination):

    """Console script for IntegrityGuard."""

    if task == "generate_hashes":
        hash_report(config)

    elif task == "monitor":
        monitor(config)

    elif task == "copy_config":
        # Handle possible errors
        if destination == "":
            print("Error: --destination is required when using copy_config task.")
            exit()

        if destination.endswith('.conf') == False:
            print("Error: --destination must be a full path including the file name. (e.g. <any-name>.conf)")
            exit()

        # Copy config file
        copy_config(destination)

    elif task == "show_paths":
        show_paths(config)

    return 0

if __name__ == "__main__":
    sys.exit(main())
