from . import base_types
import Cheque21
import CreditTransfer10
import InvestmentAccount60

class PaymentInstrument26Choice(base_types._BaseFieldType):

	__slots__ = ["_CdtTrfDtls", "_ChqDtls", "_BkrsDrftDtls", "_CshAcctDtls"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque21, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque21, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcctDtls', type=InvestmentAccount60, min=0, max=1, mutex_group=1, array=False),
	))

