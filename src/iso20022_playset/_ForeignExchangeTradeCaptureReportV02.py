# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReferences2
from . import Header23
from . import Max35Text
from . import MessageIdentification1
from . import Number
from . import SupplementaryData1
from . import Trade7
from . import TradePartyIdentification9
from . import TrueFalseIndicator

class ForeignExchangeTradeCaptureReportV02(base_types._BaseFieldType):

	__slots__ = ["_CtrPtySdId", "_Hdr", "_LastRptReqd", "_QryRjctRsn", "_Ref", "_ReqRjctd", "_ReqRspndr", "_RptId", "_SplmtryData", "_TradDtl", "_TradgSdId", "_TtlNbTrds"]
	@property
	def CtrPtySdId(self):
		return self._CtrPtySdId

	@CtrPtySdId.setter
	def CtrPtySdId(self, value):
		self._CtrPtySdId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySdId', TradePartyIdentification9, False)

	@CtrPtySdId.deleter
	def CtrPtySdId(self):
		del self._CtrPtySdId
		self._CtrPtySdId = base_types.UninitialisedField(self, 'CtrPtySdId', TradePartyIdentification9, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header23, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header23, False)

	@property
	def LastRptReqd(self):
		return self._LastRptReqd

	@LastRptReqd.setter
	def LastRptReqd(self, value):
		self._LastRptReqd = value if value is not None else base_types.UninitialisedField(self, 'LastRptReqd', TrueFalseIndicator, False)

	@LastRptReqd.deleter
	def LastRptReqd(self):
		del self._LastRptReqd
		self._LastRptReqd = base_types.UninitialisedField(self, 'LastRptReqd', TrueFalseIndicator, False)

	@property
	def QryRjctRsn(self):
		return self._QryRjctRsn

	@QryRjctRsn.setter
	def QryRjctRsn(self, value):
		self._QryRjctRsn = value if value is not None else base_types.UninitialisedField(self, 'QryRjctRsn', Max35Text, False)

	@QryRjctRsn.deleter
	def QryRjctRsn(self):
		del self._QryRjctRsn
		self._QryRjctRsn = base_types.UninitialisedField(self, 'QryRjctRsn', Max35Text, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', AdditionalReferences2, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', AdditionalReferences2, False)

	@property
	def ReqRjctd(self):
		return self._ReqRjctd

	@ReqRjctd.setter
	def ReqRjctd(self, value):
		self._ReqRjctd = value if value is not None else base_types.UninitialisedField(self, 'ReqRjctd', TrueFalseIndicator, False)

	@ReqRjctd.deleter
	def ReqRjctd(self):
		del self._ReqRjctd
		self._ReqRjctd = base_types.UninitialisedField(self, 'ReqRjctd', TrueFalseIndicator, False)

	@property
	def ReqRspndr(self):
		return self._ReqRspndr

	@ReqRspndr.setter
	def ReqRspndr(self, value):
		self._ReqRspndr = value if value is not None else base_types.UninitialisedField(self, 'ReqRspndr', TrueFalseIndicator, False)

	@ReqRspndr.deleter
	def ReqRspndr(self):
		del self._ReqRspndr
		self._ReqRspndr = base_types.UninitialisedField(self, 'ReqRspndr', TrueFalseIndicator, False)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', MessageIdentification1, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', MessageIdentification1, False)

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
	def TradDtl(self):
		return self._TradDtl

	@TradDtl.setter
	def TradDtl(self, value):
		self._TradDtl = value if value is not None else base_types.UninitialisedField(self, 'TradDtl', Trade7, False)

	@TradDtl.deleter
	def TradDtl(self):
		del self._TradDtl
		self._TradDtl = base_types.UninitialisedField(self, 'TradDtl', Trade7, False)

	@property
	def TradgSdId(self):
		return self._TradgSdId

	@TradgSdId.setter
	def TradgSdId(self, value):
		self._TradgSdId = value if value is not None else base_types.UninitialisedField(self, 'TradgSdId', TradePartyIdentification9, False)

	@TradgSdId.deleter
	def TradgSdId(self):
		del self._TradgSdId
		self._TradgSdId = base_types.UninitialisedField(self, 'TradgSdId', TradePartyIdentification9, False)

	@property
	def TtlNbTrds(self):
		return self._TtlNbTrds

	@TtlNbTrds.setter
	def TtlNbTrds(self, value):
		self._TtlNbTrds = value if value is not None else base_types.UninitialisedField(self, 'TtlNbTrds', Number, False)

	@TtlNbTrds.deleter
	def TtlNbTrds(self):
		del self._TtlNbTrds
		self._TtlNbTrds = base_types.UninitialisedField(self, 'TtlNbTrds', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtySdId', type=TradePartyIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastRptReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRjctRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=AdditionalReferences2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqRjctd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqRspndr', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDtl', type=Trade7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdId', type=TradePartyIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbTrds', type=Number, min=0, max=1, mutex_group=None, array=False),
	))