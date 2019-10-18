# Copyright DataStax, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa

from cassandra.cqlengine import columns 
from cassandra.cqlengine.models import Model

class ModelTest(unittest.TestCase):

    def test_subclasses(self):
        class A(Model):
            field1 = columns.DateTime(primary_key=True)
            field2 = columns.Text(primary_key=True)
            field3 = columns.Integer()

        class B(A):
            field1 = columns.DateTime(primary_key=True, partition_key=False)
            field2 = columns.DateTime(primary_key=True, partition_key=True)
        self.assertEqual(A._defined_columns['field1'].partition_key, True)
        self.assertEqual(A._defined_columns['field2'].partition_key, False)

        self.assertEqual(B._defined_columns['field1'].partition_key, False)
        self.assertEqual(B._defined_columns['field2'].partition_key, True)
