from . import base_types
from .CollateralDate2 import CollateralDate2
from .SupplementaryData1 import SupplementaryData1
from .DealTransactionDetails5 import DealTransactionDetails5
from .CollateralParties10 import CollateralParties10
from .Pagination1 import Pagination1
from .CashMovement8 import CashMovement8
from .Linkages58 import Linkages58
from .OtherParties38 import OtherParties38
from .TransactionIdentifications45 import TransactionIdentifications45
from .SecuritiesMovement9 import SecuritiesMovement9
from .CollateralParameters10 import CollateralParameters10

class TripartyCollateralTransactionInstructionV01(base_types._BaseFieldType):

	__slots__ = ["_SctiesMvmnt", "_DealTxDtls", "_DealTxDt", "_CshMvmnt", "_SplmtryData", "_Pgntn", "_TxInstrId", "_GnlParams", "_Lnkgs", "_OthrPties", "_CollPties"]
	@property
	def SctiesMvmnt(self):
		return self._SctiesMvmnt

	@SctiesMvmnt.setter
	def SctiesMvmnt(self, value):
		self._SctiesMvmnt = value if type(value) != base_types.auto else self.make_default("SctiesMvmnt")

	@SctiesMvmnt.deleter
	def SctiesMvmnt(self):
		del self._SctiesMvmnt
		self._SctiesMvmnt = None

	@property
	def DealTxDtls(self):
		return self._DealTxDtls

	@DealTxDtls.setter
	def DealTxDtls(self, value):
		self._DealTxDtls = value if type(value) != base_types.auto else self.make_default("DealTxDtls")

	@DealTxDtls.deleter
	def DealTxDtls(self):
		del self._DealTxDtls
		self._DealTxDtls = None

	@property
	def DealTxDt(self):
		return self._DealTxDt

	@DealTxDt.setter
	def DealTxDt(self, value):
		self._DealTxDt = value if type(value) != base_types.auto else self.make_default("DealTxDt")

	@DealTxDt.deleter
	def DealTxDt(self):
		del self._DealTxDt
		self._DealTxDt = None

	@property
	def CshMvmnt(self):
		return self._CshMvmnt

	@CshMvmnt.setter
	def CshMvmnt(self, value):
		self._CshMvmnt = value if type(value) != base_types.auto else self.make_default("CshMvmnt")

	@CshMvmnt.deleter
	def CshMvmnt(self):
		del self._CshMvmnt
		self._CshMvmnt = None

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
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def TxInstrId(self):
		return self._TxInstrId

	@TxInstrId.setter
	def TxInstrId(self, value):
		self._TxInstrId = value if type(value) != base_types.auto else self.make_default("TxInstrId")

	@TxInstrId.deleter
	def TxInstrId(self):
		del self._TxInstrId
		self._TxInstrId = None

	@property
	def GnlParams(self):
		return self._GnlParams

	@GnlParams.setter
	def GnlParams(self, value):
		self._GnlParams = value if type(value) != base_types.auto else self.make_default("GnlParams")

	@GnlParams.deleter
	def GnlParams(self):
		del self._GnlParams
		self._GnlParams = None

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if type(value) != base_types.auto else self.make_default("Lnkgs")

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = None

	@property
	def OthrPties(self):
		return self._OthrPties

	@OthrPties.setter
	def OthrPties(self, value):
		self._OthrPties = value if type(value) != base_types.auto else self.make_default("OthrPties")

	@OthrPties.deleter
	def OthrPties(self):
		del self._OthrPties
		self._OthrPties = None

	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if type(value) != base_types.auto else self.make_default("CollPties")

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesMvmnt', type=SecuritiesMovement9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DealTxDtls', type=DealTransactionDetails5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTxDt', type=CollateralDate2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CashMovement8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInstrId', type=TransactionIdentifications45, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlParams', type=CollateralParameters10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages58, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrPties', type=OtherParties38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPties', type=CollateralParties10, min=1, max=1, mutex_group=None, array=False),
	))

