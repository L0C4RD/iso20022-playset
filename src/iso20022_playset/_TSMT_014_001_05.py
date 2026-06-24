# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DataSetSubmissionV05 import DataSetSubmissionV05

class TSMT_014_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_DataSetSubmissn"]
		@property
		def DataSetSubmissn(self):
			return self._DataSetSubmissn

		@DataSetSubmissn.setter
		def DataSetSubmissn(self, value):
			self._DataSetSubmissn = value if type(value) != base_types.auto else self.make_default("DataSetSubmissn")

		@DataSetSubmissn.deleter
		def DataSetSubmissn(self):
			del self._DataSetSubmissn
			self._DataSetSubmissn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DataSetSubmissn', type=DataSetSubmissionV05, min=1, max=1, mutex_group=None, array=False),
		))