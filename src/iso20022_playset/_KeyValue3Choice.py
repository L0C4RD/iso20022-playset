# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType10
from . import TRRelatedData2

class KeyValue3Choice(base_types._BaseFieldType):

	__slots__ = ["_NcrptdKeyVal", "_TRRltdData"]
	@property
	def NcrptdKeyVal(self):
		return self._NcrptdKeyVal

	@NcrptdKeyVal.setter
	def NcrptdKeyVal(self, value):
		self._NcrptdKeyVal = value if value is not None else base_types.UninitialisedField(self, 'NcrptdKeyVal', ContentInformationType10, False)

	@NcrptdKeyVal.deleter
	def NcrptdKeyVal(self):
		del self._NcrptdKeyVal
		self._NcrptdKeyVal = base_types.UninitialisedField(self, 'NcrptdKeyVal', ContentInformationType10, False)

	@property
	def TRRltdData(self):
		return self._TRRltdData

	@TRRltdData.setter
	def TRRltdData(self, value):
		self._TRRltdData = value if value is not None else base_types.UninitialisedField(self, 'TRRltdData', TRRelatedData2, False)

	@TRRltdData.deleter
	def TRRltdData(self):
		del self._TRRltdData
		self._TRRltdData = base_types.UninitialisedField(self, 'TRRltdData', TRRelatedData2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NcrptdKeyVal', type=ContentInformationType10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TRRltdData', type=TRRelatedData2, min=0, max=1, mutex_group=1, array=False),
	))