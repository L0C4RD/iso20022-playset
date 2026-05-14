# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContentInformationType10 import ContentInformationType10
from ._TRRelatedData2 import TRRelatedData2

class KeyValue3Choice(base_types._BaseFieldType):

	__slots__ = ["_NcrptdKeyVal", "_TRRltdData"]
	@property
	def NcrptdKeyVal(self):
		return self._NcrptdKeyVal

	@NcrptdKeyVal.setter
	def NcrptdKeyVal(self, value):
		self._NcrptdKeyVal = value if type(value) != base_types.auto else self.make_default("NcrptdKeyVal")

	@NcrptdKeyVal.deleter
	def NcrptdKeyVal(self):
		del self._NcrptdKeyVal
		self._NcrptdKeyVal = None

	@property
	def TRRltdData(self):
		return self._TRRltdData

	@TRRltdData.setter
	def TRRltdData(self, value):
		self._TRRltdData = value if type(value) != base_types.auto else self.make_default("TRRltdData")

	@TRRltdData.deleter
	def TRRltdData(self):
		del self._TRRltdData
		self._TRRltdData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NcrptdKeyVal', type=ContentInformationType10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TRRltdData', type=TRRelatedData2, min=0, max=1, mutex_group=1, array=False),
	))