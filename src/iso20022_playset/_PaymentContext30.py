# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditTransferContext1
from . import DirectDebitContext1
from . import PaymentContext29
from . import SaleContext4

class PaymentContext30(base_types._BaseFieldType):

	__slots__ = ["_CdtTrfCntxt", "_DrctDbtCntxt", "_PmtCntxt", "_SaleCntxt"]
	@property
	def CdtTrfCntxt(self):
		return self._CdtTrfCntxt

	@CdtTrfCntxt.setter
	def CdtTrfCntxt(self, value):
		self._CdtTrfCntxt = value if value is not None else base_types.UninitialisedField(self, 'CdtTrfCntxt', CreditTransferContext1, False)

	@CdtTrfCntxt.deleter
	def CdtTrfCntxt(self):
		del self._CdtTrfCntxt
		self._CdtTrfCntxt = base_types.UninitialisedField(self, 'CdtTrfCntxt', CreditTransferContext1, False)

	@property
	def DrctDbtCntxt(self):
		return self._DrctDbtCntxt

	@DrctDbtCntxt.setter
	def DrctDbtCntxt(self, value):
		self._DrctDbtCntxt = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtCntxt', DirectDebitContext1, False)

	@DrctDbtCntxt.deleter
	def DrctDbtCntxt(self):
		del self._DrctDbtCntxt
		self._DrctDbtCntxt = base_types.UninitialisedField(self, 'DrctDbtCntxt', DirectDebitContext1, False)

	@property
	def PmtCntxt(self):
		return self._PmtCntxt

	@PmtCntxt.setter
	def PmtCntxt(self, value):
		self._PmtCntxt = value if value is not None else base_types.UninitialisedField(self, 'PmtCntxt', PaymentContext29, False)

	@PmtCntxt.deleter
	def PmtCntxt(self):
		del self._PmtCntxt
		self._PmtCntxt = base_types.UninitialisedField(self, 'PmtCntxt', PaymentContext29, False)

	@property
	def SaleCntxt(self):
		return self._SaleCntxt

	@SaleCntxt.setter
	def SaleCntxt(self, value):
		self._SaleCntxt = value if value is not None else base_types.UninitialisedField(self, 'SaleCntxt', SaleContext4, False)

	@SaleCntxt.deleter
	def SaleCntxt(self):
		del self._SaleCntxt
		self._SaleCntxt = base_types.UninitialisedField(self, 'SaleCntxt', SaleContext4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtTrfCntxt', type=CreditTransferContext1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctDbtCntxt', type=DirectDebitContext1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCntxt', type=PaymentContext29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleCntxt', type=SaleContext4, min=0, max=1, mutex_group=None, array=False),
	))