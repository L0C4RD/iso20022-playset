from . import base_types
from .CorporateActionAmendmentRejectionStatus1 import CorporateActionAmendmentRejectionStatus1
from .CorporateActionAmendmentProcessingStatus1 import CorporateActionAmendmentProcessingStatus1

class ElectionAmendmentStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_PrcdSts", "_RjctdSts"]
	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if type(value) != auto else self.make_default("PrcdSts")

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = None

	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if type(value) != auto else self.make_default("RjctdSts")

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcdSts', type=CorporateActionAmendmentProcessingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdSts', type=CorporateActionAmendmentRejectionStatus1, min=0, max=1, mutex_group=1, array=False),
	))

