# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DirectDebitTransactionInformation35 import DirectDebitTransactionInformation35
from ._GroupHeader125 import GroupHeader125
from ._SupplementaryData1 import SupplementaryData1

class FIToFICustomerDirectDebitV12(base_types._BaseFieldType):

	__slots__ = ["_DrctDbtTxInf", "_GrpHdr", "_SplmtryData"]
	@property
	def DrctDbtTxInf(self):
		return self._DrctDbtTxInf

	@DrctDbtTxInf.setter
	def DrctDbtTxInf(self, value):
		self._DrctDbtTxInf = value if type(value) != base_types.auto else self.make_default("DrctDbtTxInf")

	@DrctDbtTxInf.deleter
	def DrctDbtTxInf(self):
		del self._DrctDbtTxInf
		self._DrctDbtTxInf = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DrctDbtTxInf', type=DirectDebitTransactionInformation35, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader125, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))