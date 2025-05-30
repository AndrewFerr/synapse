#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright 2023 Matrix.org Foundation C.I.C.
# Copyright (C) 2023 New Vector, Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# See the GNU Affero General Public License for more details:
# <https://www.gnu.org/licenses/agpl-3.0.html>.
#
# Originally licensed under the Apache License, Version 2.0:
# <http://www.apache.org/licenses/LICENSE-2.0>.
#
# [This file includes modifications made by New Vector Limited]
#
#

from synapse.config._base import RootConfig
from synapse.config.appservice import AppServiceConfig, ConfigError

from tests.unittest import TestCase


class AppServiceConfigTest(TestCase):
    def test_invalid_app_service_config_files(self) -> None:
        for invalid_value in [
            "foobar",
            1,
            None,
            True,
            False,
            {},
            ["foo", "bar", False],
        ]:
            with self.assertRaises(ConfigError):
                AppServiceConfig(RootConfig()).read_config(
                    {"app_service_config_files": invalid_value}
                )

    def test_valid_app_service_config_files(self) -> None:
        AppServiceConfig(RootConfig()).read_config({"app_service_config_files": []})
        AppServiceConfig(RootConfig()).read_config(
            {"app_service_config_files": ["/not/a/real/path", "/not/a/real/path/2"]}
        )
