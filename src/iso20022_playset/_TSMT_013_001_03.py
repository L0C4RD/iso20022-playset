# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DataSetMatchReportV03 import DataSetMatchReportV03

class TSMT_013_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DataSetMtchRpt"]
		@property
		def DataSetMtchRpt(self):
			return self._DataSetMtchRpt

		@DataSetMtchRpt.setter
		def DataSetMtchRpt(self, value):
			self._DataSetMtchRpt = value if type(value) != base_types.auto else self.make_default("DataSetMtchRpt")

		@DataSetMtchRpt.deleter
		def DataSetMtchRpt(self):
			del self._DataSetMtchRpt
			self._DataSetMtchRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DataSetMtchRpt', type=DataSetMatchReportV03, min=1, max=1, mutex_group=None, array=False),
		))