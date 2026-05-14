# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CashMovement5 import CashMovement5
from ._CollateralDate2 import CollateralDate2
from ._CollateralParameters11 import CollateralParameters11
from ._CollateralParties8 import CollateralParties8
from ._DealTransactionDetails6 import DealTransactionDetails6
from ._Pagination1 import Pagination1
from ._SecuritiesMovement7 import SecuritiesMovement7
from ._SupplementaryData1 import SupplementaryData1
from ._TransactionIdentifications44 import TransactionIdentifications44

class TripartyCollateralAllegementNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_CollPties", "_CshMvmnt", "_DealTxDt", "_DealTxDtls", "_GnlParams", "_Pgntn", "_SctiesMvmnt", "_SplmtryData", "_TxInstrId"]
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
	def TxInstrId(self):
		return self._TxInstrId

	@TxInstrId.setter
	def TxInstrId(self, value):
		self._TxInstrId = value if type(value) != base_types.auto else self.make_default("TxInstrId")

	@TxInstrId.deleter
	def TxInstrId(self):
		del self._TxInstrId
		self._TxInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPties', type=CollateralParties8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CashMovement5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DealTxDt', type=CollateralDate2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTxDtls', type=DealTransactionDetails6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlParams', type=CollateralParameters11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmnt', type=SecuritiesMovement7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInstrId', type=TransactionIdentifications44, min=1, max=1, mutex_group=None, array=False),
	))