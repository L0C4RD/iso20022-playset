from . import base_types
from ._Warrant4 import Warrant4
from ._Debt5 import Debt5
from ._Derivative4 import Derivative4
from ._Equity3 import Equity3

class FinancialInstrument97(base_types._BaseFieldType):

	__slots__ = ["_Deriv", "_Warrt", "_Debt", "_Eqty"]
	@property
	def Debt(self):
		return self._Debt

	@Debt.setter
	def Debt(self, value):
		self._Debt = value if type(value) != base_types.auto else self.make_default("Debt")

	@Debt.deleter
	def Debt(self):
		del self._Debt
		self._Debt = None

	@property
	def Deriv(self):
		return self._Deriv

	@Deriv.setter
	def Deriv(self, value):
		self._Deriv = value if type(value) != base_types.auto else self.make_default("Deriv")

	@Deriv.deleter
	def Deriv(self):
		del self._Deriv
		self._Deriv = None

	@property
	def Eqty(self):
		return self._Eqty

	@Eqty.setter
	def Eqty(self, value):
		self._Eqty = value if type(value) != base_types.auto else self.make_default("Eqty")

	@Eqty.deleter
	def Eqty(self):
		del self._Eqty
		self._Eqty = None

	@property
	def Warrt(self):
		return self._Warrt

	@Warrt.setter
	def Warrt(self, value):
		self._Warrt = value if type(value) != base_types.auto else self.make_default("Warrt")

	@Warrt.deleter
	def Warrt(self):
		del self._Warrt
		self._Warrt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Debt', type=Debt5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Deriv', type=Derivative4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqty', type=Equity3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Warrt', type=Warrant4, min=0, max=1, mutex_group=None, array=False),
	))

