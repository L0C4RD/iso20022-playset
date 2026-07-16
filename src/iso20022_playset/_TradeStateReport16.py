# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractModification3
from . import CounterpartyData88
from . import Max140Text
from . import ReconciliationFlag2
from . import SupplementaryData1
from . import TransactionCollateralData18Choice
from . import TransactionLoanData31Choice

class TradeStateReport16(base_types._BaseFieldType):

	__slots__ = ["_CollData", "_CtrPtySpcfcData", "_CtrctMod", "_LnData", "_RcncltnFlg", "_SplmtryData", "_TechRcrdId"]
	@property
	def CollData(self):
		return self._CollData

	@CollData.setter
	def CollData(self, value):
		self._CollData = value if value is not None else base_types.UninitialisedField(self, 'CollData', TransactionCollateralData18Choice, False)

	@CollData.deleter
	def CollData(self):
		del self._CollData
		self._CollData = base_types.UninitialisedField(self, 'CollData', TransactionCollateralData18Choice, False)

	@property
	def CtrPtySpcfcData(self):
		return self._CtrPtySpcfcData

	@CtrPtySpcfcData.setter
	def CtrPtySpcfcData(self, value):
		self._CtrPtySpcfcData = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySpcfcData', CounterpartyData88, False)

	@CtrPtySpcfcData.deleter
	def CtrPtySpcfcData(self):
		del self._CtrPtySpcfcData
		self._CtrPtySpcfcData = base_types.UninitialisedField(self, 'CtrPtySpcfcData', CounterpartyData88, False)

	@property
	def CtrctMod(self):
		return self._CtrctMod

	@CtrctMod.setter
	def CtrctMod(self, value):
		self._CtrctMod = value if value is not None else base_types.UninitialisedField(self, 'CtrctMod', ContractModification3, False)

	@CtrctMod.deleter
	def CtrctMod(self):
		del self._CtrctMod
		self._CtrctMod = base_types.UninitialisedField(self, 'CtrctMod', ContractModification3, False)

	@property
	def LnData(self):
		return self._LnData

	@LnData.setter
	def LnData(self, value):
		self._LnData = value if value is not None else base_types.UninitialisedField(self, 'LnData', TransactionLoanData31Choice, False)

	@LnData.deleter
	def LnData(self):
		del self._LnData
		self._LnData = base_types.UninitialisedField(self, 'LnData', TransactionLoanData31Choice, False)

	@property
	def RcncltnFlg(self):
		return self._RcncltnFlg

	@RcncltnFlg.setter
	def RcncltnFlg(self, value):
		self._RcncltnFlg = value if value is not None else base_types.UninitialisedField(self, 'RcncltnFlg', ReconciliationFlag2, False)

	@RcncltnFlg.deleter
	def RcncltnFlg(self):
		del self._RcncltnFlg
		self._RcncltnFlg = base_types.UninitialisedField(self, 'RcncltnFlg', ReconciliationFlag2, False)

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
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollData', type=TransactionCollateralData18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySpcfcData', type=CounterpartyData88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctMod', type=ContractModification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnData', type=TransactionLoanData31Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFlg', type=ReconciliationFlag2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))