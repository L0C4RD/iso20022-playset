# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashMovement8
from . import CollateralDate2
from . import CollateralParameters10
from . import CollateralParties10
from . import DealTransactionDetails5
from . import Linkages58
from . import OtherParties38
from . import Pagination1
from . import SecuritiesMovement9
from . import SupplementaryData1
from . import TransactionIdentifications45

class TripartyCollateralTransactionInstructionV01(base_types._BaseFieldType):

	__slots__ = ["_CollPties", "_CshMvmnt", "_DealTxDt", "_DealTxDtls", "_GnlParams", "_Lnkgs", "_OthrPties", "_Pgntn", "_SctiesMvmnt", "_SplmtryData", "_TxInstrId"]
	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if value is not None else base_types.UninitialisedField(self, 'CollPties', CollateralParties10, False)

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = base_types.UninitialisedField(self, 'CollPties', CollateralParties10, False)

	@property
	def CshMvmnt(self):
		return self._CshMvmnt

	@CshMvmnt.setter
	def CshMvmnt(self, value):
		self._CshMvmnt = value if value is not None else base_types.UninitialisedField(self, 'CshMvmnt', CashMovement8, True)

	@CshMvmnt.deleter
	def CshMvmnt(self):
		del self._CshMvmnt
		self._CshMvmnt = base_types.UninitialisedField(self, 'CshMvmnt', CashMovement8, True)

	@property
	def DealTxDt(self):
		return self._DealTxDt

	@DealTxDt.setter
	def DealTxDt(self, value):
		self._DealTxDt = value if value is not None else base_types.UninitialisedField(self, 'DealTxDt', CollateralDate2, False)

	@DealTxDt.deleter
	def DealTxDt(self):
		del self._DealTxDt
		self._DealTxDt = base_types.UninitialisedField(self, 'DealTxDt', CollateralDate2, False)

	@property
	def DealTxDtls(self):
		return self._DealTxDtls

	@DealTxDtls.setter
	def DealTxDtls(self, value):
		self._DealTxDtls = value if value is not None else base_types.UninitialisedField(self, 'DealTxDtls', DealTransactionDetails5, False)

	@DealTxDtls.deleter
	def DealTxDtls(self):
		del self._DealTxDtls
		self._DealTxDtls = base_types.UninitialisedField(self, 'DealTxDtls', DealTransactionDetails5, False)

	@property
	def GnlParams(self):
		return self._GnlParams

	@GnlParams.setter
	def GnlParams(self, value):
		self._GnlParams = value if value is not None else base_types.UninitialisedField(self, 'GnlParams', CollateralParameters10, False)

	@GnlParams.deleter
	def GnlParams(self):
		del self._GnlParams
		self._GnlParams = base_types.UninitialisedField(self, 'GnlParams', CollateralParameters10, False)

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if value is not None else base_types.UninitialisedField(self, 'Lnkgs', Linkages58, True)

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = base_types.UninitialisedField(self, 'Lnkgs', Linkages58, True)

	@property
	def OthrPties(self):
		return self._OthrPties

	@OthrPties.setter
	def OthrPties(self, value):
		self._OthrPties = value if value is not None else base_types.UninitialisedField(self, 'OthrPties', OtherParties38, False)

	@OthrPties.deleter
	def OthrPties(self):
		del self._OthrPties
		self._OthrPties = base_types.UninitialisedField(self, 'OthrPties', OtherParties38, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def SctiesMvmnt(self):
		return self._SctiesMvmnt

	@SctiesMvmnt.setter
	def SctiesMvmnt(self, value):
		self._SctiesMvmnt = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmnt', SecuritiesMovement9, True)

	@SctiesMvmnt.deleter
	def SctiesMvmnt(self):
		del self._SctiesMvmnt
		self._SctiesMvmnt = base_types.UninitialisedField(self, 'SctiesMvmnt', SecuritiesMovement9, True)

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
	def TxInstrId(self):
		return self._TxInstrId

	@TxInstrId.setter
	def TxInstrId(self, value):
		self._TxInstrId = value if value is not None else base_types.UninitialisedField(self, 'TxInstrId', TransactionIdentifications45, False)

	@TxInstrId.deleter
	def TxInstrId(self):
		del self._TxInstrId
		self._TxInstrId = base_types.UninitialisedField(self, 'TxInstrId', TransactionIdentifications45, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPties', type=CollateralParties10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CashMovement8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DealTxDt', type=CollateralDate2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTxDtls', type=DealTransactionDetails5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlParams', type=CollateralParameters10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages58, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrPties', type=OtherParties38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmnt', type=SecuritiesMovement9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInstrId', type=TransactionIdentifications45, min=1, max=1, mutex_group=None, array=False),
	))