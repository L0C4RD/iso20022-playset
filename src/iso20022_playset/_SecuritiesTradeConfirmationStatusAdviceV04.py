# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AffirmationStatus11Choice
from . import CancellationProcessingStatus10Choice
from . import ConfirmationParties9
from . import Linkages77
from . import MatchingStatus35Choice
from . import Order23
from . import ProcessingStatus98Choice
from . import ReplacementProcessingStatus10Choice
from . import SettlementParties121
from . import SupplementaryData1
from . import TransactiontIdentification4

class SecuritiesTradeConfirmationStatusAdviceV04(base_types._BaseFieldType):

	__slots__ = ["_AffirmSts", "_ConfPties", "_CtrPtyTradgDtls", "_CxlPrcgSts", "_DlvrgSttlmPties", "_Id", "_MtchgSts", "_PrcgSts", "_PtyTradgDtls", "_RcvgSttlmPties", "_Refs", "_RplcmntPrcgSts", "_SplmtryData"]
	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if value is not None else base_types.UninitialisedField(self, 'AffirmSts', AffirmationStatus11Choice, False)

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = base_types.UninitialisedField(self, 'AffirmSts', AffirmationStatus11Choice, False)

	@property
	def ConfPties(self):
		return self._ConfPties

	@ConfPties.setter
	def ConfPties(self, value):
		self._ConfPties = value if value is not None else base_types.UninitialisedField(self, 'ConfPties', ConfirmationParties9, True)

	@ConfPties.deleter
	def ConfPties(self):
		del self._ConfPties
		self._ConfPties = base_types.UninitialisedField(self, 'ConfPties', ConfirmationParties9, True)

	@property
	def CtrPtyTradgDtls(self):
		return self._CtrPtyTradgDtls

	@CtrPtyTradgDtls.setter
	def CtrPtyTradgDtls(self, value):
		self._CtrPtyTradgDtls = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyTradgDtls', Order23, False)

	@CtrPtyTradgDtls.deleter
	def CtrPtyTradgDtls(self):
		del self._CtrPtyTradgDtls
		self._CtrPtyTradgDtls = base_types.UninitialisedField(self, 'CtrPtyTradgDtls', Order23, False)

	@property
	def CxlPrcgSts(self):
		return self._CxlPrcgSts

	@CxlPrcgSts.setter
	def CxlPrcgSts(self, value):
		self._CxlPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'CxlPrcgSts', CancellationProcessingStatus10Choice, False)

	@CxlPrcgSts.deleter
	def CxlPrcgSts(self):
		del self._CxlPrcgSts
		self._CxlPrcgSts = base_types.UninitialisedField(self, 'CxlPrcgSts', CancellationProcessingStatus10Choice, False)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties121, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties121, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', TransactiontIdentification4, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', TransactiontIdentification4, False)

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if value is not None else base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus35Choice, False)

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus35Choice, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus98Choice, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus98Choice, False)

	@property
	def PtyTradgDtls(self):
		return self._PtyTradgDtls

	@PtyTradgDtls.setter
	def PtyTradgDtls(self, value):
		self._PtyTradgDtls = value if value is not None else base_types.UninitialisedField(self, 'PtyTradgDtls', Order23, False)

	@PtyTradgDtls.deleter
	def PtyTradgDtls(self):
		del self._PtyTradgDtls
		self._PtyTradgDtls = base_types.UninitialisedField(self, 'PtyTradgDtls', Order23, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties121, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties121, False)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', Linkages77, True)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', Linkages77, True)

	@property
	def RplcmntPrcgSts(self):
		return self._RplcmntPrcgSts

	@RplcmntPrcgSts.setter
	def RplcmntPrcgSts(self, value):
		self._RplcmntPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'RplcmntPrcgSts', ReplacementProcessingStatus10Choice, False)

	@RplcmntPrcgSts.deleter
	def RplcmntPrcgSts(self):
		del self._RplcmntPrcgSts
		self._RplcmntPrcgSts = base_types.UninitialisedField(self, 'RplcmntPrcgSts', ReplacementProcessingStatus10Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfPties', type=ConfirmationParties9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyTradgDtls', type=Order23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlPrcgSts', type=CancellationProcessingStatus10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties121, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=TransactiontIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus98Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyTradgDtls', type=Order23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties121, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Linkages77, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RplcmntPrcgSts', type=ReplacementProcessingStatus10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))