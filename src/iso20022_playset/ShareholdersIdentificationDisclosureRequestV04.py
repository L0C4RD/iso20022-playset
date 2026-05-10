from . import base_types
from .DecimalNumber import DecimalNumber
from .Max140Text import Max140Text
from .SupplementaryData1 import SupplementaryData1
from .SecurityIdentification19 import SecurityIdentification19
from .PartyIdentification129Choice import PartyIdentification129Choice
from .DateFormat46Choice import DateFormat46Choice
from .RequestShareHeldDate1Choice import RequestShareHeldDate1Choice
from .Max35Text import Max35Text
from .PartyIdentification214 import PartyIdentification214
from .DisclosureRequestType1Code import DisclosureRequestType1Code
from .YesNoIndicator import YesNoIndicator
from .CountryCode import CountryCode

class ShareholdersIdentificationDisclosureRequestV04(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_IssrDsclsrDdln", "_ShrsQtyThrshld", "_DsclsrReqTp", "_AplblLaw", "_RspnThrghChainInd", "_DsclsrRspnDdln", "_PrvsDsclsrReqId", "_DsclsrRspnRcpt", "_SplmtryData", "_PlcOfJursdctn", "_IssrDsclsrReqId", "_FwdReqInd", "_ShrhldrRghtsDrctvInd", "_FinInstrmId", "_ShrhldrsDsclsrRcrdDt", "_ReqShrHeldDt"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def IssrDsclsrDdln(self):
		return self._IssrDsclsrDdln

	@IssrDsclsrDdln.setter
	def IssrDsclsrDdln(self, value):
		self._IssrDsclsrDdln = value if type(value) != base_types.auto else self.make_default("IssrDsclsrDdln")

	@IssrDsclsrDdln.deleter
	def IssrDsclsrDdln(self):
		del self._IssrDsclsrDdln
		self._IssrDsclsrDdln = None

	@property
	def ShrsQtyThrshld(self):
		return self._ShrsQtyThrshld

	@ShrsQtyThrshld.setter
	def ShrsQtyThrshld(self, value):
		self._ShrsQtyThrshld = value if type(value) != base_types.auto else self.make_default("ShrsQtyThrshld")

	@ShrsQtyThrshld.deleter
	def ShrsQtyThrshld(self):
		del self._ShrsQtyThrshld
		self._ShrsQtyThrshld = None

	@property
	def DsclsrReqTp(self):
		return self._DsclsrReqTp

	@DsclsrReqTp.setter
	def DsclsrReqTp(self, value):
		self._DsclsrReqTp = value if type(value) != base_types.auto else self.make_default("DsclsrReqTp")

	@DsclsrReqTp.deleter
	def DsclsrReqTp(self):
		del self._DsclsrReqTp
		self._DsclsrReqTp = None

	@property
	def AplblLaw(self):
		return self._AplblLaw

	@AplblLaw.setter
	def AplblLaw(self, value):
		self._AplblLaw = value if type(value) != base_types.auto else self.make_default("AplblLaw")

	@AplblLaw.deleter
	def AplblLaw(self):
		del self._AplblLaw
		self._AplblLaw = None

	@property
	def RspnThrghChainInd(self):
		return self._RspnThrghChainInd

	@RspnThrghChainInd.setter
	def RspnThrghChainInd(self, value):
		self._RspnThrghChainInd = value if type(value) != base_types.auto else self.make_default("RspnThrghChainInd")

	@RspnThrghChainInd.deleter
	def RspnThrghChainInd(self):
		del self._RspnThrghChainInd
		self._RspnThrghChainInd = None

	@property
	def DsclsrRspnDdln(self):
		return self._DsclsrRspnDdln

	@DsclsrRspnDdln.setter
	def DsclsrRspnDdln(self, value):
		self._DsclsrRspnDdln = value if type(value) != base_types.auto else self.make_default("DsclsrRspnDdln")

	@DsclsrRspnDdln.deleter
	def DsclsrRspnDdln(self):
		del self._DsclsrRspnDdln
		self._DsclsrRspnDdln = None

	@property
	def PrvsDsclsrReqId(self):
		return self._PrvsDsclsrReqId

	@PrvsDsclsrReqId.setter
	def PrvsDsclsrReqId(self, value):
		self._PrvsDsclsrReqId = value if type(value) != base_types.auto else self.make_default("PrvsDsclsrReqId")

	@PrvsDsclsrReqId.deleter
	def PrvsDsclsrReqId(self):
		del self._PrvsDsclsrReqId
		self._PrvsDsclsrReqId = None

	@property
	def DsclsrRspnRcpt(self):
		return self._DsclsrRspnRcpt

	@DsclsrRspnRcpt.setter
	def DsclsrRspnRcpt(self, value):
		self._DsclsrRspnRcpt = value if type(value) != base_types.auto else self.make_default("DsclsrRspnRcpt")

	@DsclsrRspnRcpt.deleter
	def DsclsrRspnRcpt(self):
		del self._DsclsrRspnRcpt
		self._DsclsrRspnRcpt = None

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
	def PlcOfJursdctn(self):
		return self._PlcOfJursdctn

	@PlcOfJursdctn.setter
	def PlcOfJursdctn(self, value):
		self._PlcOfJursdctn = value if type(value) != base_types.auto else self.make_default("PlcOfJursdctn")

	@PlcOfJursdctn.deleter
	def PlcOfJursdctn(self):
		del self._PlcOfJursdctn
		self._PlcOfJursdctn = None

	@property
	def IssrDsclsrReqId(self):
		return self._IssrDsclsrReqId

	@IssrDsclsrReqId.setter
	def IssrDsclsrReqId(self, value):
		self._IssrDsclsrReqId = value if type(value) != base_types.auto else self.make_default("IssrDsclsrReqId")

	@IssrDsclsrReqId.deleter
	def IssrDsclsrReqId(self):
		del self._IssrDsclsrReqId
		self._IssrDsclsrReqId = None

	@property
	def FwdReqInd(self):
		return self._FwdReqInd

	@FwdReqInd.setter
	def FwdReqInd(self, value):
		self._FwdReqInd = value if type(value) != base_types.auto else self.make_default("FwdReqInd")

	@FwdReqInd.deleter
	def FwdReqInd(self):
		del self._FwdReqInd
		self._FwdReqInd = None

	@property
	def ShrhldrRghtsDrctvInd(self):
		return self._ShrhldrRghtsDrctvInd

	@ShrhldrRghtsDrctvInd.setter
	def ShrhldrRghtsDrctvInd(self, value):
		self._ShrhldrRghtsDrctvInd = value if type(value) != base_types.auto else self.make_default("ShrhldrRghtsDrctvInd")

	@ShrhldrRghtsDrctvInd.deleter
	def ShrhldrRghtsDrctvInd(self):
		del self._ShrhldrRghtsDrctvInd
		self._ShrhldrRghtsDrctvInd = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def ShrhldrsDsclsrRcrdDt(self):
		return self._ShrhldrsDsclsrRcrdDt

	@ShrhldrsDsclsrRcrdDt.setter
	def ShrhldrsDsclsrRcrdDt(self, value):
		self._ShrhldrsDsclsrRcrdDt = value if type(value) != base_types.auto else self.make_default("ShrhldrsDsclsrRcrdDt")

	@ShrhldrsDsclsrRcrdDt.deleter
	def ShrhldrsDsclsrRcrdDt(self):
		del self._ShrhldrsDsclsrRcrdDt
		self._ShrhldrsDsclsrRcrdDt = None

	@property
	def ReqShrHeldDt(self):
		return self._ReqShrHeldDt

	@ReqShrHeldDt.setter
	def ReqShrHeldDt(self, value):
		self._ReqShrHeldDt = value if type(value) != base_types.auto else self.make_default("ReqShrHeldDt")

	@ReqShrHeldDt.deleter
	def ReqShrHeldDt(self):
		del self._ReqShrHeldDt
		self._ReqShrHeldDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrDdln', type=DateFormat46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrsQtyThrshld', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsclsrReqTp', type=DisclosureRequestType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblLaw', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnThrghChainInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsclsrRspnDdln', type=DateFormat46Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsDsclsrReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsclsrRspnRcpt', type=PartyIdentification214, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlcOfJursdctn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdReqInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrRghtsDrctvInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrsDsclsrRcrdDt', type=DateFormat46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqShrHeldDt', type=RequestShareHeldDate1Choice, min=0, max=1, mutex_group=None, array=False),
	))

