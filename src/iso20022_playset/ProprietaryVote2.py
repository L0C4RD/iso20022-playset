from . import base_types
from .FinancialInstrumentQuantity18Choice import FinancialInstrumentQuantity18Choice
from .GenericIdentification30 import GenericIdentification30

class ProprietaryVote2(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_Cd"]
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
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=GenericIdentification30, min=1, max=1, mutex_group=None, array=False),
	))

