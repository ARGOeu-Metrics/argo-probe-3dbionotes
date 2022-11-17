from distutils.core import setup

NAME = "argo-probe-3dbionotes"


def get_ver():
    try:
        for line in open(NAME + '.spec'):
            if "Version:" in line:
                return line.split()[1]

    except IOError:
        raise SystemExit(1)


setup(
    name=NAME,
    version=get_ver(),
    author="SRCE",
    author_email="kzailac@srce.hr",
    description="ARGO probe that checks if 3DBionotes web application is "
                "working as expected",
    url="https://github.com/ARGOeu-Metrics/argo-probe-3dbionotes",
    data_files=[('/usr/libexec/argo/probes/3dbionotes', ['src/check_app.py'])]
)
