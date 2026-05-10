from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._CreditTransferTransaction70 import CreditTransferTransaction70
from ._GroupHeader131 import GroupHeader131

class FIToFICustomerCreditTransferV13(base_types._BaseFieldType):

	__slots__ = ["_CdtTrfTxInf", "_SplmtryData", "_GrpHdr"]
	@property
	def CdtTrfTxInf(self):
		return self._CdtTrfTxInf

	@CdtTrfTxInf.setter
	def CdtTrfTxInf(self, value):
		self._CdtTrfTxInf = value if type(value) != base_types.auto else self.make_default("CdtTrfTxInf")

	@CdtTrfTxInf.deleter
	def CdtTrfTxInf(self):
		del self._CdtTrfTxInf
		self._CdtTrfTxInf = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtTrfTxInf', type=CreditTransferTransaction70, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader131, min=1, max=1, mutex_group=None, array=False),
	))

