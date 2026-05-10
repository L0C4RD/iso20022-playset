from . import base_types
from ._AmountAndDirection30 import AmountAndDirection30
from ._PriceInformation10 import PriceInformation10
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1
from ._DecimalNumber import DecimalNumber
from ._SecurityIdentification14 import SecurityIdentification14

class InvestmentFund1(base_types._BaseFieldType):

	__slots__ = ["_ClssTp", "_Pric", "_FinInstrmId", "_TxnlUnits", "_TtlVal", "_SplmtryData", "_TtlUnitsOutsdng"]
	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if type(value) != base_types.auto else self.make_default("ClssTp")

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != base_types.auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def TxnlUnits(self):
		return self._TxnlUnits

	@TxnlUnits.setter
	def TxnlUnits(self, value):
		self._TxnlUnits = value if type(value) != base_types.auto else self.make_default("TxnlUnits")

	@TxnlUnits.deleter
	def TxnlUnits(self):
		del self._TxnlUnits
		self._TxnlUnits = None

	@property
	def TtlVal(self):
		return self._TtlVal

	@TtlVal.setter
	def TtlVal(self, value):
		self._TtlVal = value if type(value) != base_types.auto else self.make_default("TtlVal")

	@TtlVal.deleter
	def TtlVal(self):
		del self._TtlVal
		self._TtlVal = None

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
	def TtlUnitsOutsdng(self):
		return self._TtlUnitsOutsdng

	@TtlUnitsOutsdng.setter
	def TtlUnitsOutsdng(self, value):
		self._TtlUnitsOutsdng = value if type(value) != base_types.auto else self.make_default("TtlUnitsOutsdng")

	@TtlUnitsOutsdng.deleter
	def TtlUnitsOutsdng(self):
		del self._TtlUnitsOutsdng
		self._TtlUnitsOutsdng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=PriceInformation10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxnlUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVal', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlUnitsOutsdng', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

