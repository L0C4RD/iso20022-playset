from . import base_types
import Max140Text
import TransactionLoanData26Choice
import SupplementaryData1
import CounterpartyData88
import TransactionCollateralData18Choice

class TradeTransactionCollateralUpdate8(base_types._BaseFieldType):

	__slots__ = ["_CtrPtySpcfcData", "_CollData", "_TechRcrdId", "_SplmtryData", "_LnData"]
	@property
	def CtrPtySpcfcData(self):
		return self._CtrPtySpcfcData

	@CtrPtySpcfcData.setter
	def CtrPtySpcfcData(self, value):
		self._CtrPtySpcfcData = value if type(value) != auto else self.make_default("CtrPtySpcfcData")

	@CtrPtySpcfcData.deleter
	def CtrPtySpcfcData(self):
		del self._CtrPtySpcfcData
		self._CtrPtySpcfcData = None

	@property
	def CollData(self):
		return self._CollData

	@CollData.setter
	def CollData(self, value):
		self._CollData = value if type(value) != auto else self.make_default("CollData")

	@CollData.deleter
	def CollData(self):
		del self._CollData
		self._CollData = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

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
	def LnData(self):
		return self._LnData

	@LnData.setter
	def LnData(self, value):
		self._LnData = value if type(value) != auto else self.make_default("LnData")

	@LnData.deleter
	def LnData(self):
		del self._LnData
		self._LnData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtySpcfcData', type=CounterpartyData88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollData', type=TransactionCollateralData18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LnData', type=TransactionLoanData26Choice, min=0, max=1, mutex_group=None, array=False),
	))

