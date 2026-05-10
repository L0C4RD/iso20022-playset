from . import base_types
from .UnitPriceType2Choice import UnitPriceType2Choice
from .PriceValue1 import PriceValue1
from .PriceMethod1Code import PriceMethod1Code

class UnitPrice20(base_types._BaseFieldType):

	__slots__ = ["_PricTp", "_PricMtd", "_Val"]
	@property
	def PricTp(self):
		return self._PricTp

	@PricTp.setter
	def PricTp(self, value):
		self._PricTp = value if type(value) != base_types.auto else self.make_default("PricTp")

	@PricTp.deleter
	def PricTp(self):
		del self._PricTp
		self._PricTp = None

	@property
	def PricMtd(self):
		return self._PricMtd

	@PricMtd.setter
	def PricMtd(self, value):
		self._PricMtd = value if type(value) != base_types.auto else self.make_default("PricMtd")

	@PricMtd.deleter
	def PricMtd(self):
		del self._PricMtd
		self._PricMtd = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricTp', type=UnitPriceType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricMtd', type=PriceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceValue1, min=1, max=1, mutex_group=None, array=False),
	))

