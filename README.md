[<img align="left" width="128px" height="128px" src="https://avatars2.githubusercontent.com/u/26557946" />](https://defcon201.org/)
## DEFCON201 Website Mk.III

Python script for a dead-simple static site generator, based on [M-Labs' website.](https://github.com/m-labs/web)
<br/><br/>

This is the repository containing the contents and static page template engine for the DEFCON201 website.

# Requirements:
Python 3. Tested on Ubuntu 18.04.
Imports `os`, `re`, `shutil`. Shouldn't need any wacky libraries, and we won't use `pip`.

# Usage:
Clone repo, then just
> `./generate.py`

This script takes no arguments and should be run from the base directory the script is in.

# Directories:
> `output/` - Output directory

Deleted and created every time the generator is run. Contains static output HTML, to copy to the server.

> `res/` - Resource directory

Static resources. Copied as-is to the output directory.

> `pages/` - Pages directory

Contains `.page` files, which are run through the PageGenerator.

### Future plans:
When rev2 is complete, these will be made available:

> `templates/` - Template directory

HTML fragments to be included into pages by generators.

> `data/`

Data to be used by DataMethods.

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
