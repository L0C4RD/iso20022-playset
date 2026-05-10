from . import base_types
import GenericIdentification56
import FinancialInstrumentQuantity1Choice

class SubBalanceQuantity5Choice(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_Prtry"]
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
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification56, min=0, max=1, mutex_group=1, array=False),
	))

