from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .CounterpartyData88 import CounterpartyData88
from .TransactionCollateralData18Choice import TransactionCollateralData18Choice
from .ModificationLevel1Code import ModificationLevel1Code
from .TransactionLoanData31Choice import TransactionLoanData31Choice
from .Max140Text import Max140Text

class TradeTransactionCorrection13(base_types._BaseFieldType):

	__slots__ = ["_LnData", "_CollData", "_SplmtryData", "_CtrPtySpcfcData", "_LvlTp", "_TechRcrdId"]
	@property
	def LnData(self):
		return self._LnData

	@LnData.setter
	def LnData(self, value):
		self._LnData = value if type(value) != base_types.auto else self.make_default("LnData")

	@LnData.deleter
	def LnData(self):
		del self._LnData
		self._LnData = None

	@property
	def CollData(self):
		return self._CollData

	@CollData.setter
	def CollData(self, value):
		self._CollData = value if type(value) != base_types.auto else self.make_default("CollData")

	@CollData.deleter
	def CollData(self):
		del self._CollData
		self._CollData = None

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
	def CtrPtySpcfcData(self):
		return self._CtrPtySpcfcData

	@CtrPtySpcfcData.setter
	def CtrPtySpcfcData(self, value):
		self._CtrPtySpcfcData = value if type(value) != base_types.auto else self.make_default("CtrPtySpcfcData")

	@CtrPtySpcfcData.deleter
	def CtrPtySpcfcData(self):
		del self._CtrPtySpcfcData
		self._CtrPtySpcfcData = None

	@property
	def LvlTp(self):
		return self._LvlTp

	@LvlTp.setter
	def LvlTp(self, value):
		self._LvlTp = value if type(value) != base_types.auto else self.make_default("LvlTp")

	@LvlTp.deleter
	def LvlTp(self):
		del self._LvlTp
		self._LvlTp = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LnData', type=TransactionLoanData31Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollData', type=TransactionCollateralData18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtySpcfcData', type=CounterpartyData88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LvlTp', type=ModificationLevel1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

