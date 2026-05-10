from . import base_types
from .PaymentContext29 import PaymentContext29
from .SaleContext4 import SaleContext4
from .DirectDebitContext1 import DirectDebitContext1
from .CreditTransferContext1 import CreditTransferContext1

class PaymentContext30(base_types._BaseFieldType):

	__slots__ = ["_PmtCntxt", "_SaleCntxt", "_DrctDbtCntxt", "_CdtTrfCntxt"]
	@property
	def PmtCntxt(self):
		return self._PmtCntxt

	@PmtCntxt.setter
	def PmtCntxt(self, value):
		self._PmtCntxt = value if type(value) != base_types.auto else self.make_default("PmtCntxt")

	@PmtCntxt.deleter
	def PmtCntxt(self):
		del self._PmtCntxt
		self._PmtCntxt = None

	@property
	def SaleCntxt(self):
		return self._SaleCntxt

	@SaleCntxt.setter
	def SaleCntxt(self, value):
		self._SaleCntxt = value if type(value) != base_types.auto else self.make_default("SaleCntxt")

	@SaleCntxt.deleter
	def SaleCntxt(self):
		del self._SaleCntxt
		self._SaleCntxt = None

	@property
	def DrctDbtCntxt(self):
		return self._DrctDbtCntxt

	@DrctDbtCntxt.setter
	def DrctDbtCntxt(self, value):
		self._DrctDbtCntxt = value if type(value) != base_types.auto else self.make_default("DrctDbtCntxt")

	@DrctDbtCntxt.deleter
	def DrctDbtCntxt(self):
		del self._DrctDbtCntxt
		self._DrctDbtCntxt = None

	@property
	def CdtTrfCntxt(self):
		return self._CdtTrfCntxt

	@CdtTrfCntxt.setter
	def CdtTrfCntxt(self, value):
		self._CdtTrfCntxt = value if type(value) != base_types.auto else self.make_default("CdtTrfCntxt")

	@CdtTrfCntxt.deleter
	def CdtTrfCntxt(self):
		del self._CdtTrfCntxt
		self._CdtTrfCntxt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtCntxt', type=PaymentContext29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleCntxt', type=SaleContext4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctDbtCntxt', type=DirectDebitContext1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtTrfCntxt', type=CreditTransferContext1, min=0, max=1, mutex_group=None, array=False),
	))

