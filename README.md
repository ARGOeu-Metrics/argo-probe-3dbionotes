# argo-probe-3dbionotes

Package contains a custom ARGO probe which checks if 3DBionotes-WS service is working as expected.

## Synopsis

Probe takes three mandatory arguments: hostname, timeout and path to CA bundle location. 

```
# /usr/libexec/argo/probes/3dbionotes/check_app.py -h
usage: ARGO probe that tests the functionality of 3dBionotes web application
       [-h] -H HOSTNAME -t TIMEOUT --ca-bundle CA_BUNDLE

optional arguments:
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname HOSTNAME
                        hostname
  -t TIMEOUT, --timeout TIMEOUT
                        timeout in seconds
  --ca-bundle CA_BUNDLE
                        location of CA bundle
```

HOSTNAME is the name of the host (without schema or path - the full URL which is being tested is built by the probe itself).

TIMEOUT is the time in seconds after which the request is raising the timeout exception and the execution is terminated.

CA_BUNDLE is the path to the CA bundle location, which is used for authentication.

Example of the probe execution:

```
# /usr/libexec/argo/probes/3dbionotes/check_app.py -H 3dbionotes.cnb.csic.es -t 30 --ca-bundle /etc/pki/tls/certs/ca-bundle.crt
OK - Data fetched successfully
```
