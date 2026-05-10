from . import base_types
from .Quantity54Choice import Quantity54Choice
from .GenericIdentification144 import GenericIdentification144

class BalanceQuantity15Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_Qty"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

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
		base_types.FieldEntry(name='Prtry', type=GenericIdentification144, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity54Choice, min=0, max=1, mutex_group=1, array=False),
	))

