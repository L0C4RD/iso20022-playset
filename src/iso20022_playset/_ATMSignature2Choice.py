from . import base_types
from .TRRelatedData2 import TRRelatedData2
from .ContentInformationType14 import ContentInformationType14

class ATMSignature2Choice(base_types._BaseFieldType):

	__slots__ = ["_TRRltdData", "_DgtlSgntr"]
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

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TRRltdData', type=TRRelatedData2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=ContentInformationType14, min=0, max=1, mutex_group=1, array=False),
	))

