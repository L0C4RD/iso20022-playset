import base_types
import Trade9
import SupplementaryData1
import ConfirmationRequest1Code
import Period12
import Header23
import QueryTradeStatus1Code
import MessageIdentification1
import Max35NumericText

class ForeignExchangeTradeConfirmationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_TradDtl", "_QryStartNb", "_ReqId", "_Hdr", "_QryTradSts", "_ConfTp", "_SplmtryData", "_QryPrd"]
	@property
	def TradDtl(self):
		return self._TradDtl

	@TradDtl.setter
	def TradDtl(self, value):
		self._TradDtl = value if type(value) != auto else self.make_default("TradDtl")

	@TradDtl.deleter
	def TradDtl(self):
		del self._TradDtl
		self._TradDtl = None

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
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def QryTradSts(self):
		return self._QryTradSts

	@QryTradSts.setter
	def QryTradSts(self, value):
		self._QryTradSts = value if type(value) != auto else self.make_default("QryTradSts")

	@QryTradSts.deleter
	def QryTradSts(self):
		del self._QryTradSts
		self._QryTradSts = None

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
	def QryPrd(self):
		return self._QryPrd

	@QryPrd.setter
	def QryPrd(self, value):
		self._QryPrd = value if type(value) != auto else self.make_default("QryPrd")

	@QryPrd.deleter
	def QryPrd(self):
		del self._QryPrd
		self._QryPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradDtl', type=Trade9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryStartNb', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTradSts', type=QueryTradeStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfTp', type=ConfirmationRequest1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QryPrd', type=Period12, min=1, max=1, mutex_group=None, array=False),
	))

