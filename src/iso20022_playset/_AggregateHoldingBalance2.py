# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentAggregateBalance1
from . import SecurityIdentification19
from . import SupplementaryData1

class AggregateHoldingBalance2(base_types._BaseFieldType):

	__slots__ = ["_BalForFinInstrm", "_FinInstrmId", "_SplmtryData"]
	@property
	def BalForFinInstrm(self):
		return self._BalForFinInstrm

	@BalForFinInstrm.setter
	def BalForFinInstrm(self, value):
		self._BalForFinInstrm = value if value is not None else base_types.UninitialisedField(self, 'BalForFinInstrm', FinancialInstrumentAggregateBalance1, True)

	@BalForFinInstrm.deleter
	def BalForFinInstrm(self):
		del self._BalForFinInstrm
		self._BalForFinInstrm = base_types.UninitialisedField(self, 'BalForFinInstrm', FinancialInstrumentAggregateBalance1, True)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

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
		base_types.FieldEntry(name='BalForFinInstrm', type=FinancialInstrumentAggregateBalance1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))