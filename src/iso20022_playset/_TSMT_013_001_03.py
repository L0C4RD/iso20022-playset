# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataSetMatchReportV03

class TSMT_013_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.013.001.03"
		_docname = "tsmt.013.001.03"

		__slots__ = ["_DataSetMtchRpt"]
		@property
		def DataSetMtchRpt(self):
			return self._DataSetMtchRpt

		@DataSetMtchRpt.setter
		def DataSetMtchRpt(self, value):
			self._DataSetMtchRpt = value if value is not None else base_types.UninitialisedField(self, 'DataSetMtchRpt', DataSetMatchReportV03, False)

		@DataSetMtchRpt.deleter
		def DataSetMtchRpt(self):
			del self._DataSetMtchRpt
			self._DataSetMtchRpt = base_types.UninitialisedField(self, 'DataSetMtchRpt', DataSetMatchReportV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DataSetMtchRpt', type=DataSetMatchReportV03, min=1, max=1, mutex_group=None, array=False),
		))