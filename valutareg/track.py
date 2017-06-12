import random
import os


class QueryParamSource:
    def __init__(self, indices, params):
        self._indices = indices
        self._params = params
        cwd = os.path.dirname(__file__)
        with open(os.path.join(cwd, "lastnames.txt"), "r") as ins:
            self.terms = [line.strip() for line in ins.readlines()]
        with open(os.path.join(cwd, "currencycodes.txt"), "r") as ins:
            self.currency = [line.strip() for line in ins.readlines()]

    def partition(self, partition_index, total_partitions):
        return self

    def size(self):
        return 1


class ForeignLastnameQueryParamSource(QueryParamSource):
    def params(self):
        result = {
            "body": {
                "query": {
                    "match": {
                        "utletternavn": "%s" % random.choice(self.terms)
                    }
                }
            },
            "index": None,
            "type": None,
            "use_request_cache": self._params.get("use_request_cache", False)
        }
        return result


class CurrencyCodeQueryParamSource(QueryParamSource):
    def params(self):
        result = {
            "body": {
                "query": {
                    "bool": {
                        "filter": {
                            "term": {
                                "valutakode": "%s" % random.choice(self.currency)
                            }
                        }
                    }
                }
            },
            "index": None,
            "type": None,
            "use_request_cache": self._params.get("use_request_cache", False)
        }
        return result

class CurrencyCode10QueryParamSource(QueryParamSource):
    def params(self):
        result = {
            "body": {
                "size": 10,
                "query": {
                    "bool": {
                        "filter": {
                            "term": {
                                "valutakode": "%s" % random.choice(self.currency)
                            }
                        }
                    }
                }
            },
            "index": None,
            "type": None,
            "use_request_cache": self._params.get("use_request_cache", False)
        }
        return result

class CurrencyCode10kQueryParamSource(QueryParamSource):
    def params(self):
        result = {
            "body": {
                "size": 10000,
                "query": {
                    "bool": {
                        "filter": {
                            "term": {
                                "valutakode": "%s" % random.choice(self.currency)
                            }
                        }
                    }
                }
            },
            "index": None,
            "type": None,
            "use_request_cache": self._params.get("use_request_cache", False)
        }
        return result

def register(registry):
    registry.register_param_source("currency-code-query-source", CurrencyCodeQueryParamSource)
    registry.register_param_source("currency-code-10-query-source", CurrencyCode10QueryParamSource)
    registry.register_param_source("currency-code-10k-query-source", CurrencyCode10kQueryParamSource)
    registry.register_param_source("foreign-last-query-source", ForeignLastnameQueryParamSource)