valutareg-rally
---------------

This repository contains the track specifications for the Elasticsearch
benchmarking tool [Rally](https://github.com/elastic/rally) for use with
Valutaregisteret.

Versioning Scheme
-----------------

From time to time, setting and mapping formats change in Elasticsearch. As we want to be able to support multiple versions of Elasticsearch, we also need to version track specifications. Therefore, this repository contains multiple branches. The following examples should give you an idea how the versioning scheme works:

* master: tracks on this branch are compatible with the latest development version of Elasticsearch
* 5.0.0-alpha2: compatible with the released version 5.0.0-alpha2.
* 2: compatible with all Elasticsearch releases with the major release number 2 (e.g. 2.1, 2.2, 2.2.1)
* 1.7: compatible with all Elasticsearch releases with the major release number 1 and minor release number 7 (e.g. 1.7.0, 1.7.1, 1.7.2)

As you can see, branches can match exact release numbers but Rally is also lenient in case settings mapping formats did not change for a few releases. Rally will try to match in the following order:

1. major.minor.patch-extension_label (e.g. 5.0.0-alpha5)
2. major.minor.patch (e.g. 2.3.1)
3. major.minor (e.g. 2.3)
4. major (e.g. 2)

Apart from that, the master branch is always considered to be compatible with the Elasticsearch master branch.

To specify the version to check against, add `--distribution-version` when running Rally. It it is not specified, Rally assumes that you want to benchmark against the Elasticsearch master version. 

Example: If you want to benchmark Elasticsearch 5.0.0, run the following command:

```
esrally --distribution-version=5.0.0
```
