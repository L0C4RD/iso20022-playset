from . import base_types
import CurrencyAndAmount
import UnitOfMeasure3Choice
import Max15NumericText

class UnitPrice18(base_types._BaseFieldType):

	__slots__ = ["_UnitPric", "_Fctr", "_Amt"]
	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def Fctr(self):
		return self._Fctr

	@Fctr.setter
	def Fctr(self, value):
		self._Fctr = value if type(value) != auto else self.make_default("Fctr")

	@Fctr.deleter
	def Fctr(self):
		del self._Fctr
		self._Fctr = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnitPric', type=UnitOfMeasure3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctr', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

