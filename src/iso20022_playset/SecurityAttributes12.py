from . import base_types
from .CommonFinancialInstrumentAttributes12 import CommonFinancialInstrumentAttributes12
from .FinancialInstrument97 import FinancialInstrument97
from .SupplementaryData1 import SupplementaryData1

class SecurityAttributes12(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmAttrbts", "_FinInstrmTp", "_SplmtryData"]
	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("FinInstrmAttrbts")

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = None

	@property
	def FinInstrmTp(self):
		return self._FinInstrmTp

	@FinInstrmTp.setter
	def FinInstrmTp(self, value):
		self._FinInstrmTp = value if type(value) != base_types.auto else self.make_default("FinInstrmTp")

	@FinInstrmTp.deleter
	def FinInstrmTp(self):
		del self._FinInstrmTp
		self._FinInstrmTp = None

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
		base_types.FieldEntry(name='FinInstrmAttrbts', type=CommonFinancialInstrumentAttributes12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmTp', type=FinancialInstrument97, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

