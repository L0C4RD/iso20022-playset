from . import base_types
import ActiveCurrencyAndAmount

class BalanceTransferFundingLimit1(base_types._BaseFieldType):

	__slots__ = ["_CcyAmt"]
	@property
	def CcyAmt(self):
		return self._CcyAmt

	@CcyAmt.setter
	def CcyAmt(self, value):
		self._CcyAmt = value if type(value) != auto else self.make_default("CcyAmt")

	@CcyAmt.deleter
	def CcyAmt(self):
		del self._CcyAmt
		self._CcyAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

