# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReportingTransactionType3Choice import ReportingTransactionType3Choice
from ._SupplementaryData1 import SupplementaryData1

class FinancialInstrumentReportingTransactionReportV03(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_Tx"]
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
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tx', type=ReportingTransactionType3Choice, min=1, max=None, mutex_group=None, array=True),
	))