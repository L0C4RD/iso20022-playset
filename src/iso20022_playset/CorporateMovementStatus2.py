from . import base_types
import CorporationActionMovementProcessingStatus2
import CorporateActionMovementRejectionStatus2

class CorporateMovementStatus2(base_types._BaseFieldType):

	__slots__ = ["_RjctdSts", "_PrcdSts"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctdSts', type=CorporateActionMovementRejectionStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdSts', type=CorporationActionMovementProcessingStatus2, min=1, max=1, mutex_group=None, array=False),
	))

