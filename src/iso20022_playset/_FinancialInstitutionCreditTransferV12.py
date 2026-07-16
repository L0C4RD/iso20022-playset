# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditTransferTransaction67
from . import GroupHeader131
from . import SupplementaryData1

class FinancialInstitutionCreditTransferV12(base_types._BaseFieldType):

	__slots__ = ["_CdtTrfTxInf", "_GrpHdr", "_SplmtryData"]
	@property
	def CdtTrfTxInf(self):
		return self._CdtTrfTxInf

	@CdtTrfTxInf.setter
	def CdtTrfTxInf(self, value):
		self._CdtTrfTxInf = value if value is not None else base_types.UninitialisedField(self, 'CdtTrfTxInf', CreditTransferTransaction67, True)

	@CdtTrfTxInf.deleter
	def CdtTrfTxInf(self):
		del self._CdtTrfTxInf
		self._CdtTrfTxInf = base_types.UninitialisedField(self, 'CdtTrfTxInf', CreditTransferTransaction67, True)

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader131, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader131, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtTrfTxInf', type=CreditTransferTransaction67, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader131, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))