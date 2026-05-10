from . import base_types
from .GenericIdentification6 import GenericIdentification6
from .FinancialInstrumentQuantityChoice import FinancialInstrumentQuantityChoice

class BalanceQuantity1Choice(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_QtyAsDSS"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def QtyAsDSS(self):
		return self._QtyAsDSS

	@QtyAsDSS.setter
	def QtyAsDSS(self, value):
		self._QtyAsDSS = value if type(value) != auto else self.make_default("QtyAsDSS")

	@QtyAsDSS.deleter
	def QtyAsDSS(self):
		del self._QtyAsDSS
		self._QtyAsDSS = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantityChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyAsDSS', type=GenericIdentification6, min=0, max=1, mutex_group=1, array=False),
	))

