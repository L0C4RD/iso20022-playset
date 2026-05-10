from . import base_types
import TransactiontIdentification4
import Linkages77
import ReplacementProcessingStatus10Choice
import MatchingStatus35Choice
import CancellationProcessingStatus10Choice
import SupplementaryData1
import Order23
import ConfirmationParties9
import SettlementParties121
import ProcessingStatus98Choice
import AffirmationStatus11Choice

class SecuritiesTradeConfirmationStatusAdviceV04(base_types._BaseFieldType):

	__slots__ = ["_Id", "_DlvrgSttlmPties", "_AffirmSts", "_CxlPrcgSts", "_SplmtryData", "_CtrPtyTradgDtls", "_RcvgSttlmPties", "_RplcmntPrcgSts", "_PrcgSts", "_PtyTradgDtls", "_MtchgSts", "_Refs", "_ConfPties"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if type(value) != auto else self.make_default("AffirmSts")

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = None

	@property
	def CxlPrcgSts(self):
		return self._CxlPrcgSts

	@CxlPrcgSts.setter
	def CxlPrcgSts(self, value):
		self._CxlPrcgSts = value if type(value) != auto else self.make_default("CxlPrcgSts")

	@CxlPrcgSts.deleter
	def CxlPrcgSts(self):
		del self._CxlPrcgSts
		self._CxlPrcgSts = None

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
	def CtrPtyTradgDtls(self):
		return self._CtrPtyTradgDtls

	@CtrPtyTradgDtls.setter
	def CtrPtyTradgDtls(self, value):
		self._CtrPtyTradgDtls = value if type(value) != auto else self.make_default("CtrPtyTradgDtls")

	@CtrPtyTradgDtls.deleter
	def CtrPtyTradgDtls(self):
		del self._CtrPtyTradgDtls
		self._CtrPtyTradgDtls = None

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def RplcmntPrcgSts(self):
		return self._RplcmntPrcgSts

	@RplcmntPrcgSts.setter
	def RplcmntPrcgSts(self, value):
		self._RplcmntPrcgSts = value if type(value) != auto else self.make_default("RplcmntPrcgSts")

	@RplcmntPrcgSts.deleter
	def RplcmntPrcgSts(self):
		del self._RplcmntPrcgSts
		self._RplcmntPrcgSts = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def PtyTradgDtls(self):
		return self._PtyTradgDtls

	@PtyTradgDtls.setter
	def PtyTradgDtls(self, value):
		self._PtyTradgDtls = value if type(value) != auto else self.make_default("PtyTradgDtls")

	@PtyTradgDtls.deleter
	def PtyTradgDtls(self):
		del self._PtyTradgDtls
		self._PtyTradgDtls = None

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def ConfPties(self):
		return self._ConfPties

	@ConfPties.setter
	def ConfPties(self, value):
		self._ConfPties = value if type(value) != auto else self.make_default("ConfPties")

	@ConfPties.deleter
	def ConfPties(self):
		del self._ConfPties
		self._ConfPties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=TransactiontIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties121, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlPrcgSts', type=CancellationProcessingStatus10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyTradgDtls', type=Order23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties121, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RplcmntPrcgSts', type=ReplacementProcessingStatus10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus98Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyTradgDtls', type=Order23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Linkages77, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfPties', type=ConfirmationParties9, min=0, max=None, mutex_group=None, array=True),
	))

