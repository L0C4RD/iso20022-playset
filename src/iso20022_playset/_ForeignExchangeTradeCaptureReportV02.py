from . import base_types
from ._AdditionalReferences2 import AdditionalReferences2
from ._Header23 import Header23
from ._Max35Text import Max35Text
from ._MessageIdentification1 import MessageIdentification1
from ._Number import Number
from ._SupplementaryData1 import SupplementaryData1
from ._Trade7 import Trade7
from ._TradePartyIdentification9 import TradePartyIdentification9
from ._TrueFalseIndicator import TrueFalseIndicator

class ForeignExchangeTradeCaptureReportV02(base_types._BaseFieldType):

	__slots__ = ["_CtrPtySdId", "_Hdr", "_LastRptReqd", "_QryRjctRsn", "_Ref", "_ReqRjctd", "_ReqRspndr", "_RptId", "_SplmtryData", "_TradDtl", "_TradgSdId", "_TtlNbTrds"]
	@property
	def CtrPtySdId(self):
		return self._CtrPtySdId

	@CtrPtySdId.setter
	def CtrPtySdId(self, value):
		self._CtrPtySdId = value if type(value) != base_types.auto else self.make_default("CtrPtySdId")

	@CtrPtySdId.deleter
	def CtrPtySdId(self):
		del self._CtrPtySdId
		self._CtrPtySdId = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def LastRptReqd(self):
		return self._LastRptReqd

	@LastRptReqd.setter
	def LastRptReqd(self, value):
		self._LastRptReqd = value if type(value) != base_types.auto else self.make_default("LastRptReqd")

	@LastRptReqd.deleter
	def LastRptReqd(self):
		del self._LastRptReqd
		self._LastRptReqd = None

	@property
	def QryRjctRsn(self):
		return self._QryRjctRsn

	@QryRjctRsn.setter
	def QryRjctRsn(self, value):
		self._QryRjctRsn = value if type(value) != base_types.auto else self.make_default("QryRjctRsn")

	@QryRjctRsn.deleter
	def QryRjctRsn(self):
		del self._QryRjctRsn
		self._QryRjctRsn = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def ReqRjctd(self):
		return self._ReqRjctd

	@ReqRjctd.setter
	def ReqRjctd(self, value):
		self._ReqRjctd = value if type(value) != base_types.auto else self.make_default("ReqRjctd")

	@ReqRjctd.deleter
	def ReqRjctd(self):
		del self._ReqRjctd
		self._ReqRjctd = None

	@property
	def ReqRspndr(self):
		return self._ReqRspndr

	@ReqRspndr.setter
	def ReqRspndr(self, value):
		self._ReqRspndr = value if type(value) != base_types.auto else self.make_default("ReqRspndr")

	@ReqRspndr.deleter
	def ReqRspndr(self):
		del self._ReqRspndr
		self._ReqRspndr = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != base_types.auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

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
	def TradDtl(self):
		return self._TradDtl

	@TradDtl.setter
	def TradDtl(self, value):
		self._TradDtl = value if type(value) != base_types.auto else self.make_default("TradDtl")

	@TradDtl.deleter
	def TradDtl(self):
		del self._TradDtl
		self._TradDtl = None

	@property
	def TradgSdId(self):
		return self._TradgSdId

	@TradgSdId.setter
	def TradgSdId(self, value):
		self._TradgSdId = value if type(value) != base_types.auto else self.make_default("TradgSdId")

	@TradgSdId.deleter
	def TradgSdId(self):
		del self._TradgSdId
		self._TradgSdId = None

	@property
	def TtlNbTrds(self):
		return self._TtlNbTrds

	@TtlNbTrds.setter
	def TtlNbTrds(self, value):
		self._TtlNbTrds = value if type(value) != base_types.auto else self.make_default("TtlNbTrds")

	@TtlNbTrds.deleter
	def TtlNbTrds(self):
		del self._TtlNbTrds
		self._TtlNbTrds = None

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

