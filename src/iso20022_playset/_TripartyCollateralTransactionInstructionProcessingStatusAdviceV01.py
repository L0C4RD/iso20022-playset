# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatus30Choice
from . import CashMovement7
from . import CollateralDate2
from . import CollateralParameters12
from . import CollateralParties8
from . import DealTransactionDetails7
from . import MatchingStatus33Choice
from . import Max35Text
from . import Pagination1
from . import ProcessingStatus82Choice
from . import SecuritiesMovement8
from . import SupplementaryData1
from . import TransactionIdentifications46

class TripartyCollateralTransactionInstructionProcessingStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_CollPties", "_CshMvmnt", "_CxlPrcgSts", "_CxlReqRef", "_DealTxDt", "_DealTxDtls", "_GnlParams", "_InstrPrcgSts", "_MtchgSts", "_Pgntn", "_SctiesMvmnt", "_SplmtryData", "_TxInstrId"]
	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if value is not None else base_types.UninitialisedField(self, 'CollPties', CollateralParties8, False)

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = base_types.UninitialisedField(self, 'CollPties', CollateralParties8, False)

	@property
	def CshMvmnt(self):
		return self._CshMvmnt

	@CshMvmnt.setter
	def CshMvmnt(self, value):
		self._CshMvmnt = value if value is not None else base_types.UninitialisedField(self, 'CshMvmnt', CashMovement7, True)

	@CshMvmnt.deleter
	def CshMvmnt(self):
		del self._CshMvmnt
		self._CshMvmnt = base_types.UninitialisedField(self, 'CshMvmnt', CashMovement7, True)

	@property
	def CxlPrcgSts(self):
		return self._CxlPrcgSts

	@CxlPrcgSts.setter
	def CxlPrcgSts(self, value):
		self._CxlPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'CxlPrcgSts', CancellationStatus30Choice, False)

	@CxlPrcgSts.deleter
	def CxlPrcgSts(self):
		del self._CxlPrcgSts
		self._CxlPrcgSts = base_types.UninitialisedField(self, 'CxlPrcgSts', CancellationStatus30Choice, False)

	@property
	def CxlReqRef(self):
		return self._CxlReqRef

	@CxlReqRef.setter
	def CxlReqRef(self, value):
		self._CxlReqRef = value if value is not None else base_types.UninitialisedField(self, 'CxlReqRef', Max35Text, False)

	@CxlReqRef.deleter
	def CxlReqRef(self):
		del self._CxlReqRef
		self._CxlReqRef = base_types.UninitialisedField(self, 'CxlReqRef', Max35Text, False)

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
		self._DealTxDtls = value if value is not None else base_types.UninitialisedField(self, 'DealTxDtls', DealTransactionDetails7, False)

	@DealTxDtls.deleter
	def DealTxDtls(self):
		del self._DealTxDtls
		self._DealTxDtls = base_types.UninitialisedField(self, 'DealTxDtls', DealTransactionDetails7, False)

	@property
	def GnlParams(self):
		return self._GnlParams

	@GnlParams.setter
	def GnlParams(self, value):
		self._GnlParams = value if value is not None else base_types.UninitialisedField(self, 'GnlParams', CollateralParameters12, False)

	@GnlParams.deleter
	def GnlParams(self):
		del self._GnlParams
		self._GnlParams = base_types.UninitialisedField(self, 'GnlParams', CollateralParameters12, False)

	@property
	def InstrPrcgSts(self):
		return self._InstrPrcgSts

	@InstrPrcgSts.setter
	def InstrPrcgSts(self, value):
		self._InstrPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgSts', ProcessingStatus82Choice, False)

	@InstrPrcgSts.deleter
	def InstrPrcgSts(self):
		del self._InstrPrcgSts
		self._InstrPrcgSts = base_types.UninitialisedField(self, 'InstrPrcgSts', ProcessingStatus82Choice, False)

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if value is not None else base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus33Choice, False)

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus33Choice, False)

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
		self._SctiesMvmnt = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmnt', SecuritiesMovement8, True)

	@SctiesMvmnt.deleter
	def SctiesMvmnt(self):
		del self._SctiesMvmnt
		self._SctiesMvmnt = base_types.UninitialisedField(self, 'SctiesMvmnt', SecuritiesMovement8, True)

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
		self._TxInstrId = value if value is not None else base_types.UninitialisedField(self, 'TxInstrId', TransactionIdentifications46, False)

	@TxInstrId.deleter
	def TxInstrId(self):
		del self._TxInstrId
		self._TxInstrId = base_types.UninitialisedField(self, 'TxInstrId', TransactionIdentifications46, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPties', type=CollateralParties8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CashMovement7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CxlPrcgSts', type=CancellationStatus30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlReqRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTxDt', type=CollateralDate2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTxDtls', type=DealTransactionDetails7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlParams', type=CollateralParameters12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=ProcessingStatus82Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmnt', type=SecuritiesMovement8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInstrId', type=TransactionIdentifications46, min=1, max=1, mutex_group=None, array=False),
	))