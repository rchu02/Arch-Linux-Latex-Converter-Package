pkgname=latex-converter
pkgver=1.0
pkgrel=1
pkgdesc="A package that will take any user friendly input of an equation and convert to a LaTeX appropriate equation"
arch=('any')
license=('MIT')
depends=('python')
source=('ast_to_latex.py' 'eq_parser.py' 'latex.py')
sha256sums=('SKIP' 'SKIP' 'SKIP')

package() {
    install -Dm755 latex.py "$pkgdir/usr/bin/latex-converter"
    install -Dm755 ast_to_latex.py "$pkgdir/usr/lib/latex-converter-package/ast_to_latex.py"
    install -Dm755 eq_parser.py "$pkgdir/usr/bin/latex-converter-package/eq_parser.py"
   
    ln -s /usr/lib/mypackage/latex-converter "$pkgdir/usr/bin/latex-converter"
 }
