# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsData4
from . import SettlementFailsReportHeader2
from . import SupplementaryData1

class SettlementFailsAnnualReportV01(base_types._BaseFieldType):

	__slots__ = ["_AnlAggt", "_RptHdr", "_SplmtryData"]
	@property
	def AnlAggt(self):
		return self._AnlAggt

	@AnlAggt.setter
	def AnlAggt(self, value):
		self._AnlAggt = value if value is not None else base_types.UninitialisedField(self, 'AnlAggt', SettlementFailsData4, False)

	@AnlAggt.deleter
	def AnlAggt(self):
		del self._AnlAggt
		self._AnlAggt = base_types.UninitialisedField(self, 'AnlAggt', SettlementFailsData4, False)

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if value is not None else base_types.UninitialisedField(self, 'RptHdr', SettlementFailsReportHeader2, False)

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = base_types.UninitialisedField(self, 'RptHdr', SettlementFailsReportHeader2, False)

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
		base_types.FieldEntry(name='AnlAggt', type=SettlementFailsData4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptHdr', type=SettlementFailsReportHeader2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))