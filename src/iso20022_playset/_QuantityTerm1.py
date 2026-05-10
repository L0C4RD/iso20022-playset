from . import base_types
from ._Max3Number import Max3Number
from ._LongFraction19DecimalNumber import LongFraction19DecimalNumber
from ._Frequency19Code import Frequency19Code
from ._UnitOfMeasure8Choice import UnitOfMeasure8Choice

class QuantityTerm1(base_types._BaseFieldType):

	__slots__ = ["_TmUnit", "_UnitOfMeasr", "_Val", "_Qty"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def TmUnit(self):
		return self._TmUnit

	@TmUnit.setter
	def TmUnit(self, value):
		self._TmUnit = value if type(value) != base_types.auto else self.make_default("TmUnit")

	@TmUnit.deleter
	def TmUnit(self):
		del self._TmUnit
		self._TmUnit = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmUnit', type=Frequency19Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
	))

