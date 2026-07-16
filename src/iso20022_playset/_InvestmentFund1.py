# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection30
from . import DecimalNumber
from . import Max35Text
from . import PriceInformation10
from . import SecurityIdentification14
from . import SupplementaryData1

class InvestmentFund1(base_types._BaseFieldType):

	__slots__ = ["_ClssTp", "_FinInstrmId", "_Pric", "_SplmtryData", "_TtlUnitsOutsdng", "_TtlVal", "_TxnlUnits"]
	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if value is not None else base_types.UninitialisedField(self, 'ClssTp', Max35Text, False)

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = base_types.UninitialisedField(self, 'ClssTp', Max35Text, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification14, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification14, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', PriceInformation10, True)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', PriceInformation10, True)

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

	@property
	def TtlUnitsOutsdng(self):
		return self._TtlUnitsOutsdng

	@TtlUnitsOutsdng.setter
	def TtlUnitsOutsdng(self, value):
		self._TtlUnitsOutsdng = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsOutsdng', DecimalNumber, False)

	@TtlUnitsOutsdng.deleter
	def TtlUnitsOutsdng(self):
		del self._TtlUnitsOutsdng
		self._TtlUnitsOutsdng = base_types.UninitialisedField(self, 'TtlUnitsOutsdng', DecimalNumber, False)

	@property
	def TtlVal(self):
		return self._TtlVal

	@TtlVal.setter
	def TtlVal(self, value):
		self._TtlVal = value if value is not None else base_types.UninitialisedField(self, 'TtlVal', AmountAndDirection30, False)

	@TtlVal.deleter
	def TtlVal(self):
		del self._TtlVal
		self._TtlVal = base_types.UninitialisedField(self, 'TtlVal', AmountAndDirection30, False)

	@property
	def TxnlUnits(self):
		return self._TxnlUnits

	@TxnlUnits.setter
	def TxnlUnits(self, value):
		self._TxnlUnits = value if value is not None else base_types.UninitialisedField(self, 'TxnlUnits', DecimalNumber, False)

	@TxnlUnits.deleter
	def TxnlUnits(self):
		del self._TxnlUnits
		self._TxnlUnits = base_types.UninitialisedField(self, 'TxnlUnits', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=PriceInformation10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlUnitsOutsdng', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVal', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxnlUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))