import base_types
import Cheque9
import InvestmentAccount60
import CreditTransfer8

class PaymentInstrument21Choice(base_types._BaseFieldType):

	__slots__ = ["_BkrsDrftDtls", "_CshAcctDtls", "_ChqDtls", "_CdtTrfDtls"]
	@property
	def BkrsDrftDtls(self):
		return self._BkrsDrftDtls

	@BkrsDrftDtls.setter
	def BkrsDrftDtls(self, value):
		self._BkrsDrftDtls = value if type(value) != auto else self.make_default("BkrsDrftDtls")

	@BkrsDrftDtls.deleter
	def BkrsDrftDtls(self):
		del self._BkrsDrftDtls
		self._BkrsDrftDtls = None

	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if type(value) != auto else self.make_default("CshAcctDtls")

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = None

	@property
	def ChqDtls(self):
		return self._ChqDtls

	@ChqDtls.setter
	def ChqDtls(self, value):
		self._ChqDtls = value if type(value) != auto else self.make_default("ChqDtls")

	@ChqDtls.deleter
	def ChqDtls(self):
		del self._ChqDtls
		self._ChqDtls = None

	@property
	def CdtTrfDtls(self):
		return self._CdtTrfDtls

	@CdtTrfDtls.setter
	def CdtTrfDtls(self, value):
		self._CdtTrfDtls = value if type(value) != auto else self.make_default("CdtTrfDtls")

	@CdtTrfDtls.deleter
	def CdtTrfDtls(self):
		del self._CdtTrfDtls
		self._CdtTrfDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcctDtls', type=InvestmentAccount60, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer8, min=0, max=1, mutex_group=1, array=False),
	))

