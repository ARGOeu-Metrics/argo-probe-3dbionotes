PKGNAME=argo-probe-3dbionotes
SPECFILE=${PKGNAME}.spec

PKGVERSION=$(shell grep -s '^Version:' $(SPECFILE) | sed -e 's/Version: *//')

srpm: dist
	rpmbuild -ts --define='dist .el7' ${PKGNAME}-${PKGVERSION}.tar.gz

rpm: dist
	rpmbuild -ta ${PKGNAME}-${PKGVERSION}.tar.gz

dist:
	rm -rf dist
	python3 setup.py sdist
	mv dist/${PKGNAME}-${PKGVERSION}.tar.gz .
	rm -rf dist

sources: dist

clean:
	rm -rf ${PKGNAME}-${PKGVERSION}.tar.gz
	rm -f MANIFEST
	rm -rf dist
	rm -rf **/*.pyc
	rm -rf **/*.pyo
