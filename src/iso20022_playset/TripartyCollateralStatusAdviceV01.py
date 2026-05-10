import base_types
import SupplementaryData1
import AllocationStatus1Choice
import CollateralParties8
import CollateralParameters13
import SecuritiesMovement8
import TransactionIdentifications46
import DealTransactionDetails7
import Pagination1
import SettlementStatus27Choice
import CollateralStatus3Choice
import CollateralDate2
import CashMovement7

class TripartyCollateralStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_TxInstrId", "_SplmtryData", "_CollSts", "_CollPties", "_SctiesMvmnt", "_AllcnSts", "_SttlmSts", "_CshMvmnt", "_DealTxDt", "_Pgntn", "_GnlParams", "_DealTxDtls"]
	@property
	def TxInstrId(self):
		return self._TxInstrId

	@TxInstrId.setter
	def TxInstrId(self, value):
		self._TxInstrId = value if type(value) != auto else self.make_default("TxInstrId")

	@TxInstrId.deleter
	def TxInstrId(self):
		del self._TxInstrId
		self._TxInstrId = None

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
	def CollSts(self):
		return self._CollSts

	@CollSts.setter
	def CollSts(self, value):
		self._CollSts = value if type(value) != auto else self.make_default("CollSts")

	@CollSts.deleter
	def CollSts(self):
		del self._CollSts
		self._CollSts = None

	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if type(value) != auto else self.make_default("CollPties")

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = None

	@property
	def SctiesMvmnt(self):
		return self._SctiesMvmnt

	@SctiesMvmnt.setter
	def SctiesMvmnt(self, value):
		self._SctiesMvmnt = value if type(value) != auto else self.make_default("SctiesMvmnt")

	@SctiesMvmnt.deleter
	def SctiesMvmnt(self):
		del self._SctiesMvmnt
		self._SctiesMvmnt = None

	@property
	def AllcnSts(self):
		return self._AllcnSts

	@AllcnSts.setter
	def AllcnSts(self, value):
		self._AllcnSts = value if type(value) != auto else self.make_default("AllcnSts")

	@AllcnSts.deleter
	def AllcnSts(self):
		del self._AllcnSts
		self._AllcnSts = None

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if type(value) != auto else self.make_default("SttlmSts")

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = None

	@property
	def CshMvmnt(self):
		return self._CshMvmnt

	@CshMvmnt.setter
	def CshMvmnt(self, value):
		self._CshMvmnt = value if type(value) != auto else self.make_default("CshMvmnt")

	@CshMvmnt.deleter
	def CshMvmnt(self):
		del self._CshMvmnt
		self._CshMvmnt = None

	@property
	def DealTxDt(self):
		return self._DealTxDt

	@DealTxDt.setter
	def DealTxDt(self, value):
		self._DealTxDt = value if type(value) != auto else self.make_default("DealTxDt")

	@DealTxDt.deleter
	def DealTxDt(self):
		del self._DealTxDt
		self._DealTxDt = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def GnlParams(self):
		return self._GnlParams

	@GnlParams.setter
	def GnlParams(self, value):
		self._GnlParams = value if type(value) != auto else self.make_default("GnlParams")

	@GnlParams.deleter
	def GnlParams(self):
		del self._GnlParams
		self._GnlParams = None

	@property
	def DealTxDtls(self):
		return self._DealTxDtls

	@DealTxDtls.setter
	def DealTxDtls(self, value):
		self._DealTxDtls = value if type(value) != auto else self.make_default("DealTxDtls")

	@DealTxDtls.deleter
	def DealTxDtls(self):
		del self._DealTxDtls
		self._DealTxDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxInstrId', type=TransactionIdentifications46, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CollSts', type=CollateralStatus3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPties', type=CollateralParties8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmnt', type=SecuritiesMovement8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllcnSts', type=AllocationStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CashMovement7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DealTxDt', type=CollateralDate2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlParams', type=CollateralParameters13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTxDtls', type=DealTransactionDetails7, min=1, max=1, mutex_group=None, array=False),
	))

