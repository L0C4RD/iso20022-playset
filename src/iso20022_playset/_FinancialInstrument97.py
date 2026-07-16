# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Debt5
from . import Derivative4
from . import Equity3
from . import Warrant4

class FinancialInstrument97(base_types._BaseFieldType):

	__slots__ = ["_Debt", "_Deriv", "_Eqty", "_Warrt"]
	@property
	def Debt(self):
		return self._Debt

	@Debt.setter
	def Debt(self, value):
		self._Debt = value if value is not None else base_types.UninitialisedField(self, 'Debt', Debt5, False)

	@Debt.deleter
	def Debt(self):
		del self._Debt
		self._Debt = base_types.UninitialisedField(self, 'Debt', Debt5, False)

	@property
	def Deriv(self):
		return self._Deriv

	@Deriv.setter
	def Deriv(self, value):
		self._Deriv = value if value is not None else base_types.UninitialisedField(self, 'Deriv', Derivative4, False)

	@Deriv.deleter
	def Deriv(self):
		del self._Deriv
		self._Deriv = base_types.UninitialisedField(self, 'Deriv', Derivative4, False)

	@property
	def Eqty(self):
		return self._Eqty

	@Eqty.setter
	def Eqty(self, value):
		self._Eqty = value if value is not None else base_types.UninitialisedField(self, 'Eqty', Equity3, False)

	@Eqty.deleter
	def Eqty(self):
		del self._Eqty
		self._Eqty = base_types.UninitialisedField(self, 'Eqty', Equity3, False)

	@property
	def Warrt(self):
		return self._Warrt

	@Warrt.setter
	def Warrt(self, value):
		self._Warrt = value if value is not None else base_types.UninitialisedField(self, 'Warrt', Warrant4, False)

	@Warrt.deleter
	def Warrt(self):
		del self._Warrt
		self._Warrt = base_types.UninitialisedField(self, 'Warrt', Warrant4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Debt', type=Debt5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Deriv', type=Derivative4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqty', type=Equity3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Warrt', type=Warrant4, min=0, max=1, mutex_group=None, array=False),
	))