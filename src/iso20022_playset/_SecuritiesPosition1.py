from . import base_types
from .SubBalanceQuantity2Choice import SubBalanceQuantity2Choice
from .Max4AlphaNumericText import Max4AlphaNumericText

class SecuritiesPosition1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Qty"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity2Choice, min=1, max=1, mutex_group=None, array=False),
	))

