from . import base_types
import YesNoIndicator
import ImpliedCurrencyAndAmount

class AmountRangeBoundary1(base_types._BaseFieldType):

	__slots__ = ["_BdryAmt", "_Incl"]
	@property
	def BdryAmt(self):
		return self._BdryAmt

	@BdryAmt.setter
	def BdryAmt(self, value):
		self._BdryAmt = value if type(value) != auto else self.make_default("BdryAmt")

	@BdryAmt.deleter
	def BdryAmt(self):
		del self._BdryAmt
		self._BdryAmt = None

	@property
	def Incl(self):
		return self._Incl

	@Incl.setter
	def Incl(self, value):
		self._Incl = value if type(value) != auto else self.make_default("Incl")

	@Incl.deleter
	def Incl(self):
		del self._Incl
		self._Incl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BdryAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

