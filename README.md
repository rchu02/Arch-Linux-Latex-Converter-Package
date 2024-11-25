# Arch-Linux-Latex-Converter-Package
## Table of Contents 
  - [Introduction](#introduction)
  - [PKGBUILD](#pkgbuild)
  - [Download](#download)
  - [Sources](#sources)

## Introduction
This is a package for Arch Linux that can convert a user friendly equation to a LaTeX equation. The python files are an extension from my derivative calculator which parses the user's inputted equation using an abstract syntax tree and outputs the input as a LaTeX equation. For more information on how the `python` files work, please visit <a href="https://github.com/rchu02/Derivative-calculator.git" target="_blank">my derivative calculator project</a>. 

All functionalities:
* Can convert simple and user friendly equations ✅
* Supports the use of addition(`+`), subtraction(`-`), multiplication(`*`), division(`/`), and exponentiation(`^`) ✅
* All elementary functions (except logarithms) are supported these include:  
    * Square root. $\sqrt{}$ ✅
    * Trigonometric functions. Like $\tan$ ✅
    * Inverse Trig functions. Like $\arccos$ ✅
    * Hyperbolic Trig functions. Like $\sinh$ ✅
    * Inverse Hyperbolic Trig functions. Like $\text{arccoth}$ ✅
    * This is with the exceptions of logarithms with bases not in $e$ and $10$ ($\ln$ and $\log$ will work but $\log_e$ (log_e), $\log_{10}$ (log_10), $\log_2$ (log_2) will not) ❌
* All constants are supported. The entire Greek alphabet, such as pi &rarr; $\pi$ or omega &rarr; $\omega$ ✅
* Reads implicit multiplication, such as where $xy$ will be read as $x \cdot y$ ✅
* Unary negatives, such as $-(x+y)$ ✅
* White space is ignored ✅
* All function input must be inside of brackets, an example would be for $\sin(x)$, where the $x$ is inside braces, which is not equivalent to $sinx$, where each $s$, $i$, $n$ and $x$ are all variables. This is to avoid confusion between the calculator and user that is inputting the values.
* Does not support LaTeX inputted equations. Do not input a `\` as the AST will not recognize it.

## PKGBUILD
This project utilizies the `PKGBUILD` file which is a Bash shell script package builder in Arch Linux. [^1]

The package name is `latex-converter`, it is still an initialized project, therefore the version is still `1.0`. It utilizes `python` its script and contains 3 `python` files, `ast_to_latex.py`, `eq_parser.py`, `latex.py`. `latex.py` is the main file and is the one being called when you call the package from your command line. I amd skipping the `sha256sums` checksums for all 3 files. [^1]

For the package part:
```
package() {
    install -Dm755 latex.py "$pkgdir/usr/bin/latex-converter"
    install -Dm755 ast_to_latex.py "$pkgdir/usr/lib/latex-converter-package/ast_to_latex.py"
    install -Dm755 eq_parser.py "$pkgdir/usr/lib/latex-converter-package/eq_parser.py"
 }
```
For each line it installs the necessary file and places them in the given directory. `-D` will place the file in `"$pkgdir/usr/...` `-m755` will set the privileges to the default priviliges while making the file executable. `pkgdir` is the variable that is defined by `makepkg` that we will call when we want to create the package. [^1] This specifically becomes the root directory of your built package. [^2]

Lastly, in our `python` files, notice that 
```
import sys
sys.path.append("/usr/lib/latex-converter-package")
```
is added to the `ast_to_latex.py` and `latex.py` file. This is to ensure that the file can search for the necessary dependent files inside of the directory `/usr/lib/latex-converter-package` that contains `ast_to_latex.py` and `eq_parser.py` that we set earlier. The actual executable script of `latex.py` is located in `/usr/bin/`.

## Download
To download this package, do the following steps.

1. Download the necessary package builder in Arch if you haven't done so:
```
sudo pacman -S base-devel
```
[^1]

2. Clone the repository:
```
git clone https://github.com/rchu02/Arch-Linux-Latex-Converter-Package.git
```

3. Make sure you are in the repository,
```
cd Arch-Linux-latex-Converter-Package
```

4. Now run the package builder:
```
makepkg -si
```
* `-s` flag is to build the package and install any dependencies. [^3]
* `-i` flag is to install the package once the package is built successfully. [^3]

5. Now you can call the `latex-converter` package anytime!

For example you can do 
```
latex-converter x^2
```
and it will output 
```
This is your equation in LaTeX: x^{2}
```

## Sources

[^1]: https://wiki.archlinux.org/title/PKGBUILD
Arch Linux - PKGBUILD. (n.d.).

[^2]: https://man.archlinux.org/man/PKGBUILD.5#PACKAGING_FUNCTIONS
Arch Linux - PACKAGING FUNCTION. (n.d.).

[^3]: https://wiki.archlinux.org/title/Makepkg
Arch Linux - Makepkg. (n.d.).