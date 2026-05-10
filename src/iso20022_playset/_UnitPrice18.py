from . import base_types
from ._Max15NumericText import Max15NumericText
from ._UnitOfMeasure3Choice import UnitOfMeasure3Choice
from ._CurrencyAndAmount import CurrencyAndAmount

class UnitPrice18(base_types._BaseFieldType):

	__slots__ = ["_UnitPric", "_Fctr", "_Amt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

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

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctr', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=UnitOfMeasure3Choice, min=1, max=1, mutex_group=None, array=False),
	))

