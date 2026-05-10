from . import base_types
from .Cleared23Choice import Cleared23Choice
from .ClearingObligationType1Code import ClearingObligationType1Code
from .TrueFalseIndicator import TrueFalseIndicator

class TradeClearing11(base_types._BaseFieldType):

	__slots__ = ["_ClrSts", "_ClrOblgtn", "_IntraGrp"]
	@property
	def ClrSts(self):
		return self._ClrSts

	@ClrSts.setter
	def ClrSts(self, value):
		self._ClrSts = value if type(value) != auto else self.make_default("ClrSts")

	@ClrSts.deleter
	def ClrSts(self):
		del self._ClrSts
		self._ClrSts = None

	@property
	def ClrOblgtn(self):
		return self._ClrOblgtn

	@ClrOblgtn.setter
	def ClrOblgtn(self, value):
		self._ClrOblgtn = value if type(value) != auto else self.make_default("ClrOblgtn")

	@ClrOblgtn.deleter
	def ClrOblgtn(self):
		del self._ClrOblgtn
		self._ClrOblgtn = None

	@property
	def IntraGrp(self):
		return self._IntraGrp

	@IntraGrp.setter
	def IntraGrp(self, value):
		self._IntraGrp = value if type(value) != auto else self.make_default("IntraGrp")

	@IntraGrp.deleter
	def IntraGrp(self):
		del self._IntraGrp
		self._IntraGrp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSts', type=Cleared23Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrOblgtn', type=ClearingObligationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraGrp', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

