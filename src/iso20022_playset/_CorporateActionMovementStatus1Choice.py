from . import base_types
from ._CorporateActionMovementProcessingStatus1 import CorporateActionMovementProcessingStatus1
from ._CorporateActionMovementFailedStatus1 import CorporateActionMovementFailedStatus1
from ._CorporateActionMovementRejectionStatus1 import CorporateActionMovementRejectionStatus1

class CorporateActionMovementStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_RjctdSts", "_PrcdSts", "_FaildSts"]
	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if type(value) != base_types.auto else self.make_default("RjctdSts")

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = None

	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if type(value) != base_types.auto else self.make_default("PrcdSts")

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = None

	@property
	def FaildSts(self):
		return self._FaildSts

	@FaildSts.setter
	def FaildSts(self, value):
		self._FaildSts = value if type(value) != base_types.auto else self.make_default("FaildSts")

	@FaildSts.deleter
	def FaildSts(self):
		del self._FaildSts
		self._FaildSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctdSts', type=CorporateActionMovementRejectionStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcdSts', type=CorporateActionMovementProcessingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FaildSts', type=CorporateActionMovementFailedStatus1, min=0, max=1, mutex_group=1, array=False),
	))

