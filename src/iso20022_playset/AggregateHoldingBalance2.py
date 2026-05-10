from . import base_types
import SupplementaryData1
import FinancialInstrumentAggregateBalance1
import SecurityIdentification19

class AggregateHoldingBalance2(base_types._BaseFieldType):

	__slots__ = ["_BalForFinInstrm", "_SplmtryData", "_FinInstrmId"]
	@property
	def BalForFinInstrm(self):
		return self._BalForFinInstrm

	@BalForFinInstrm.setter
	def BalForFinInstrm(self, value):
		self._BalForFinInstrm = value if type(value) != auto else self.make_default("BalForFinInstrm")

	@BalForFinInstrm.deleter
	def BalForFinInstrm(self):
		del self._BalForFinInstrm
		self._BalForFinInstrm = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalForFinInstrm', type=FinancialInstrumentAggregateBalance1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

