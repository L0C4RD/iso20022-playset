from . import base_types
from ._Max15NumericText import Max15NumericText
from ._DecimalNumber import DecimalNumber
from ._UnitOfMeasure3Choice import UnitOfMeasure3Choice

class Quantity9(base_types._BaseFieldType):

	__slots__ = ["_UnitOfMeasr", "_Val", "_Fctr"]
	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

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

	@property
	def Fctr(self):
		return self._Fctr

	@Fctr.setter
	def Fctr(self, value):
		self._Fctr = value if type(value) != base_types.auto else self.make_default("Fctr")

	@Fctr.deleter
	def Fctr(self):
		del self._Fctr
		self._Fctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctr', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))

