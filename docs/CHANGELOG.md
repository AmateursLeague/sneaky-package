# Changelog
## [Stable-Release]

## v1.0.1 - 19-10-2024

#### Fixes:
- Added support for all file extensions, saving files with the same extension (**`write.py`**).
- Passwords now accept `int` as an argument instead of `str`.

#### Additions:
- **`display.py`** has been implemented with all three features: `show`, `clip`, and `write`.

## v1.0 - 2024-10-13

### Changes
Naming conventions of the features are changed to avoid confusion for contributors.

| v0.9.1        | v1.0           |
|---------------|----------------|
| `models.py`   | **`show.py`**  |
| `graph.py`    | **`clip.py`**  |
| `piechart.py` | **`write.py`** |


### Fixes
- Support almost all the possible extensions that has texts. 
  - `.py`, `.c`, `.cpp`, `.java`, `.js`, `.md`, `.txt`, `.go`...
- Used *simpler and faster built-in libraries* like **`shutil`** & **`glob`** for faster implementation with compact codebase.

### Added
- A new feature that scrapes the content from [**cl1p.net**](https://cl1p.net), and displays the content in console output with indentation.
    > **`scrap.py`**
- Yet another feature that has merged **`show`**, **`clip`**,and **`write`** in one file.
    > **`display.pt`** 

---

## v0.9.1 - 2024-04-08
### Added
- Clipboard feature (src code will copied into os clipboard)
### Fixes
- Bug Fixes for the clipboard feature

---

## [Stable-Release]
## v0.7.1 - 2024-03-29
### Added
- Browser Code
- All subject code

### Fixes
- Integrated functioning code snippets

### Changes
- New package added for testing `graph`.

---

## [Pre-release]
## v0.2 - 2024-02-04
### Added
- Introduces additional source code to PyPI.

### Fixes
- Enhances ease of implementation.

### Changes
- Renamed import from `lib` to `display`.

---

## [Unreleased]

## v0.1 - 2024-02-04
### Added
- Uploaded testing source data.
- Implemented discreet source code display.

### Fixes
- No fixes were required for the initial release.