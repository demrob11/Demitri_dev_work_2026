# Qualifying Nested Modules in Python

In Python, modules are often organized into **packages** (directories with an `__init__.py` file). When working with nested packages, you need to **qualify the path** to the module or function you want to use.

---

## 1. Importing a Full Path

```python
import package.subpackage.module

package.subpackage.module.function()
```

- Imports the entire module using its full qualified path.
- You must call functions with the complete reference.

✅ Useful for clarity in large projects.

---

## 2. Importing a Nested Module Directly

```python
from package.subpackage import module

module.function()
```

- Pulls the **module** into your namespace.
- Lets you drop one layer of qualification.

✅ Cleaner than always writing the full path.

**Example with Astropy:**

```python
from astropy.io import fits

# Now you can directly use the 'fits' module
hdul = fits.open("image.fits")
print(hdul.info())
```

Here, `astropy` is the top-level package, `io` is a subpackage for input/output, and `fits` is the module used for interacting with FITS files. By importing `fits` directly, you can access all of its functionality (`open`, `writeto`, `getheader`, etc.) without repeating the full qualified path each time.

---

## 3. Importing Specific Functions from a Nested Module

```python
from package.subpackage.module import function

function()
```

- Imports a **specific function or object** directly.
- You can call it without referencing the parent modules.

✅ Most concise, but sometimes less explicit.

**Example with Astropy:**

```python
from astropy.io.fits import open

# Directly call the open function
hdul = open("image.fits")
print(hdul[0].header)
```

Here, instead of importing the whole `fits` module, only the `open` function is imported. This reduces namespace clutter but can be less explicit about where the function originates.

---

## 4. Aliasing Nested Imports

```python
import package.subpackage.module as mod

mod.function()
```

- Aliases a long path to something shorter.
- Improves readability in deeply nested structures.

✅ Especially useful in scientific libraries (e.g., `import astropy.coordinates as coord`).

---

## Expanded Example with `astropy`

```python
# Full path import
import astropy.io.fits
hdul = astropy.io.fits.open('image.fits')

# Direct module import
from astropy.io import fits
hdul = fits.open('image.fits')

# Importing specific function
from astropy.io.fits import open
hdul = open('image.fits')

# Aliasing
import astropy.io.fits as afits
hdul = afits.open('image.fits')
```

This progression shows four different ways of accessing the same capability from the `astropy.io.fits` module, ranging from fully explicit to highly concise. The choice depends on project scale, clarity needs, and personal or team style guidelines.

---

## Best Practices

- Use **qualified imports** when clarity is important.
- Use **direct imports** for frequently used modules or functions.
- Use **aliasing** to simplify long paths, especially in scientific workflows.
- Be cautious with overly concise imports if they obscure where functions come from.

Think of it like navigating folders:

- `import package.subpackage.module` → Opening the whole folder.
- `from package.subpackage import module` → Picking a subfolder.
- `from package.subpackage.module import function` → Grabbing a single file from inside.
- `as` → Creating a shortcut to that file or folder.

