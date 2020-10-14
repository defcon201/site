[<img align="left" width="128px" height="128px" src="https://avatars2.githubusercontent.com/u/26557946" />](https://defcon201.org/)
## DEFCON201 Website Mk.III

Python script for a dead-simple static site generator, based on [M-Labs' website.](https://git.m-labs.hk/M-Labs/web)
<br/><br/>

This is the repository containing the contents and static page template engine for the DEFCON201 website.

# Requirements:
Python 3. Tested on Ubuntu 18.04 and 20.04, WSL with Ubuntu, and Haiku.

Imports `os`, `re`, `shutil`. Doesn't need any external libraries, nor `pip`.

# Usage:
Clone repo, then just
> `./generate.py`

This script takes no arguments and should be run from the base directory the script is in.

# Deployment:

This requires that you have:

- [SSH keys set up](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh) on your local Git instance
- Push rights to the DC201 git repos

### From an empty repo:
1. Get the code, including the remote `docs` directory in a submodule.

    `git clone --recursive git@github.com:defcon201/site.git && cd site`

2. Make the changes.

3. Generate the pages, and check them in a browser.

    `./generate.py && xdg-open docs/index.html`

4. If it all looks good, then push it to the active site, replacing the commit message with today's date.

    `cd docs`, then `git commit -a -m "DC201 site YYYYMMDD"`, then `git push`.
    Finally, `cd ..`.

5. Commit your changes, with a message indicating what's been revised.

    `git commit -a -m "Update meeting details for October 2020."`

### Updating an existing repo:
1. Pull the latest changes down to the repo. From the root of the repo:

    `git pull`

2. Update the submodule.

    `git submodule update --init --recursive`

3. Start at step 2 under "From an empty repo".

# Directories:
> `docs/` - Output directory

Deleted and created every time the generator is run. Contains static output HTML, to copy to the server.

> `res/` - Resource directory

Static resources. Copied as-is to the output directory.

> `pages/` - Pages directory

Contains `.page` files, which are run through the PageGenerator.

# Architecture:
Currently, everything is pretty monolithic, except for the MeetingDetails. It's all still a bit messy.

### Future plans:
Revision 2 will modularize the code a bit more.

**Generators** generate output files (usually HTML) in the output directory.

Generators can use PageMethods like PageGenerator uses, and DataMethods to retrieve information, to write to the generated file.

Generators hum along at 60Hz and are meant to be mostly left alone until more power is needed, or something fails.

**PageMethods** are functions used for building pages, and are called from .page files by PageGenerator.

**DataMethods** retrieve data and information which generators can use.

# TODOs:
See [the issues.](https://github.com/defcon201/site/issues)
