import base_types
import TRRelatedData2
import ContentInformationType10

class KeyChoiceValue2(base_types._BaseFieldType):

	__slots__ = ["_TRRltdData", "_NcrptdKeyVal"]
	@property
	def TRRltdData(self):
		return self._TRRltdData

	@TRRltdData.setter
	def TRRltdData(self, value):
		self._TRRltdData = value if type(value) != auto else self.make_default("TRRltdData")

	@TRRltdData.deleter
	def TRRltdData(self):
		del self._TRRltdData
		self._TRRltdData = None

	@property
	def NcrptdKeyVal(self):
		return self._NcrptdKeyVal

	@NcrptdKeyVal.setter
	def NcrptdKeyVal(self, value):
		self._NcrptdKeyVal = value if type(value) != auto else self.make_default("NcrptdKeyVal")

	@NcrptdKeyVal.deleter
	def NcrptdKeyVal(self):
		del self._NcrptdKeyVal
		self._NcrptdKeyVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TRRltdData', type=TRRelatedData2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NcrptdKeyVal', type=ContentInformationType10, min=0, max=1, mutex_group=1, array=False),
	))

