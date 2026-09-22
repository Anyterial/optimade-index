#!/usr/bin/env python

import json
import pathlib
import unittest

from optimade.models import IndexInfoResponse, LinksResponse


TOP_DIR = pathlib.Path(__file__).parent.parent


class ProvidersValidator(unittest.TestCase):
    def test_info(self):
        """Validate each index info response."""
        paths = sorted((TOP_DIR / "src" / "info").glob("v*/info.json"))
        self.assertTrue(paths)
        for path in paths:
            with path.open() as handle:
                IndexInfoResponse(**json.load(handle))

    def test_providers(self):
        """Validate each links response and its index topology."""
        paths = sorted((TOP_DIR / "src" / "links").glob("v*/providers.json"))
        self.assertTrue(paths)
        for path in paths:
            with path.open() as handle:
                response = LinksResponse(**json.load(handle))
            link_types = [entry.attributes.link_type.value for entry in response.data]
            self.assertEqual(link_types.count("root"), 1)
            self.assertIn("child", link_types)


if __name__ == "__main__":
    unittest.main()
