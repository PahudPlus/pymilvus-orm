# Copyright (C) 2019-2020 Zilliz. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

import pandas

from pymilvus_orm.exceptions import DataNotMatch


class Prepare:
    @classmethod
    def prepare_insert_data(cls, data, schema):
        if not isinstance(data, (list, tuple, pandas.DataFrame)):
            raise DataNotMatch(0, "data is not valid")

        fields = schema.fields
        entities = []
        ids = None
        raw_lengths = []
        if isinstance(data, pandas.DataFrame):
            if len(fields) != len(data.columns):
                raise DataNotMatch(0, f"collection has {len(fields)} fields"
                                      f", but go {len(data.columns)} fields")
            for i, field in enumerate(fields):
                entities.append({"name": field.name,
                                 "type": field.dtype,
                                 "values": list(data[field.name])})
                raw_lengths.append(len(data[field.name]))
                if field.is_primary:
                    ids = list(data[field.name])
        else:
            if len(data) != len(fields):
                raise DataNotMatch(0, f"collection has {len(fields)} fields, "
                                      f"but got {len(data)} fields")

            for i, field in enumerate(fields):
                entities.append({
                    "name": field.name,
                    "type": field.dtype,
                    "values": data[i]})
                raw_lengths.append(len(data[i]))
                if field.is_primary:
                    ids = data[i]

        lengths = list(set(raw_lengths))
        if len(lengths) > 1:
            raise DataNotMatch(0, "arrays must all be same length")

        return entities, ids
