# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DirectDebitTransactionInformation31
from . import GroupHeader125
from . import SupplementaryData1

class FIToFICustomerDirectDebitV11(base_types._BaseFieldType):

	__slots__ = ["_DrctDbtTxInf", "_GrpHdr", "_SplmtryData"]
	@property
	def DrctDbtTxInf(self):
		return self._DrctDbtTxInf

	@DrctDbtTxInf.setter
	def DrctDbtTxInf(self, value):
		self._DrctDbtTxInf = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtTxInf', DirectDebitTransactionInformation31, True)

	@DrctDbtTxInf.deleter
	def DrctDbtTxInf(self):
		del self._DrctDbtTxInf
		self._DrctDbtTxInf = base_types.UninitialisedField(self, 'DrctDbtTxInf', DirectDebitTransactionInformation31, True)

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader125, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader125, False)

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
		base_types.FieldEntry(name='DrctDbtTxInf', type=DirectDebitTransactionInformation31, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader125, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))