from . import base_types
import Number
import YesNoIndicator
import MessageIdentification1
import Max35NumericText
import ISODateTime
import ConfirmationRequest1Code
import TradeConfirmationStatus1Code

class Confirmation1(base_types._BaseFieldType):

	__slots__ = ["_LastRptReqd", "_ConfSts", "_QryStartNb", "_ReqId", "_LastPgInd", "_ConfTm", "_TradPtyConfTm", "_MsgNbOfCurPg", "_ListOrdrNb", "_InitgPtyConfTm", "_TtlNbOfRpts", "_QryPgNb", "_ConfTp", "_PgNb"]
	@property
	def LastRptReqd(self):
		return self._LastRptReqd

	@LastRptReqd.setter
	def LastRptReqd(self, value):
		self._LastRptReqd = value if type(value) != auto else self.make_default("LastRptReqd")

	@LastRptReqd.deleter
	def LastRptReqd(self):
		del self._LastRptReqd
		self._LastRptReqd = None

	@property
	def ConfSts(self):
		return self._ConfSts

	@ConfSts.setter
	def ConfSts(self, value):
		self._ConfSts = value if type(value) != auto else self.make_default("ConfSts")

	@ConfSts.deleter
	def ConfSts(self):
		del self._ConfSts
		self._ConfSts = None

	@property
	def QryStartNb(self):
		return self._QryStartNb

	@QryStartNb.setter
	def QryStartNb(self, value):
		self._QryStartNb = value if type(value) != auto else self.make_default("QryStartNb")

	@QryStartNb.deleter
	def QryStartNb(self):
		del self._QryStartNb
		self._QryStartNb = None

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if type(value) != auto else self.make_default("ReqId")

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = None

	@property
	def LastPgInd(self):
		return self._LastPgInd

	@LastPgInd.setter
	def LastPgInd(self, value):
		self._LastPgInd = value if type(value) != auto else self.make_default("LastPgInd")

	@LastPgInd.deleter
	def LastPgInd(self):
		del self._LastPgInd
		self._LastPgInd = None

	@property
	def ConfTm(self):
		return self._ConfTm

	@ConfTm.setter
	def ConfTm(self, value):
		self._ConfTm = value if type(value) != auto else self.make_default("ConfTm")

	@ConfTm.deleter
	def ConfTm(self):
		del self._ConfTm
		self._ConfTm = None

	@property
	def TradPtyConfTm(self):
		return self._TradPtyConfTm

	@TradPtyConfTm.setter
	def TradPtyConfTm(self, value):
		self._TradPtyConfTm = value if type(value) != auto else self.make_default("TradPtyConfTm")

	@TradPtyConfTm.deleter
	def TradPtyConfTm(self):
		del self._TradPtyConfTm
		self._TradPtyConfTm = None

	@property
	def MsgNbOfCurPg(self):
		return self._MsgNbOfCurPg

	@MsgNbOfCurPg.setter
	def MsgNbOfCurPg(self, value):
		self._MsgNbOfCurPg = value if type(value) != auto else self.make_default("MsgNbOfCurPg")

	@MsgNbOfCurPg.deleter
	def MsgNbOfCurPg(self):
		del self._MsgNbOfCurPg
		self._MsgNbOfCurPg = None

	@property
	def ListOrdrNb(self):
		return self._ListOrdrNb

	@ListOrdrNb.setter
	def ListOrdrNb(self, value):
		self._ListOrdrNb = value if type(value) != auto else self.make_default("ListOrdrNb")

	@ListOrdrNb.deleter
	def ListOrdrNb(self):
		del self._ListOrdrNb
		self._ListOrdrNb = None

	@property
	def InitgPtyConfTm(self):
		return self._InitgPtyConfTm

	@InitgPtyConfTm.setter
	def InitgPtyConfTm(self, value):
		self._InitgPtyConfTm = value if type(value) != auto else self.make_default("InitgPtyConfTm")

	@InitgPtyConfTm.deleter
	def InitgPtyConfTm(self):
		del self._InitgPtyConfTm
		self._InitgPtyConfTm = None

	@property
	def TtlNbOfRpts(self):
		return self._TtlNbOfRpts

	@TtlNbOfRpts.setter
	def TtlNbOfRpts(self, value):
		self._TtlNbOfRpts = value if type(value) != auto else self.make_default("TtlNbOfRpts")

	@TtlNbOfRpts.deleter
	def TtlNbOfRpts(self):
		del self._TtlNbOfRpts
		self._TtlNbOfRpts = None

	@property
	def QryPgNb(self):
		return self._QryPgNb

	@QryPgNb.setter
	def QryPgNb(self, value):
		self._QryPgNb = value if type(value) != auto else self.make_default("QryPgNb")

	@QryPgNb.deleter
	def QryPgNb(self):
		del self._QryPgNb
		self._QryPgNb = None

	@property
	def ConfTp(self):
		return self._ConfTp

	@ConfTp.setter
	def ConfTp(self, value):
		self._ConfTp = value if type(value) != auto else self.make_default("ConfTp")

	@ConfTp.deleter
	def ConfTp(self):
		del self._ConfTp
		self._ConfTp = None

	@property
	def PgNb(self):
		return self._PgNb

	@PgNb.setter
	def PgNb(self, value):
		self._PgNb = value if type(value) != auto else self.make_default("PgNb")

	@PgNb.deleter
	def PgNb(self):
		del self._PgNb
		self._PgNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastRptReqd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfSts', type=TradeConfirmationStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryStartNb', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastPgInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPtyConfTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNbOfCurPg', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListOrdrNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPtyConfTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRpts', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryPgNb', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfTp', type=ConfirmationRequest1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PgNb', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
	))

