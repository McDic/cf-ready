#!/bin/bash
# Main entry of `cf-ready`.

# https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

function die() {
    if [[ "$1" ]]; then
        echo "CF-Ready failed: $1"
    else
        echo "CF-Ready failed with unknown reason."
    fi
    exit 1;
}

if ! command -v python &>/dev/null ; then
    die "Couldn't find Python in your machine."
fi

# Pass all arguments to main python file
python "$SCRIPT_DIR/main.py" "$@"
