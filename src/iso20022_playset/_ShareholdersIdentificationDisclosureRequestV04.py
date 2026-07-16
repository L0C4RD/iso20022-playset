# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import DateFormat46Choice
from . import DecimalNumber
from . import DisclosureRequestType1Code
from . import Max140Text
from . import Max35Text
from . import PartyIdentification129Choice
from . import PartyIdentification214
from . import RequestShareHeldDate1Choice
from . import SecurityIdentification19
from . import SupplementaryData1
from . import YesNoIndicator

class ShareholdersIdentificationDisclosureRequestV04(base_types._BaseFieldType):

	__slots__ = ["_AplblLaw", "_DsclsrReqTp", "_DsclsrRspnDdln", "_DsclsrRspnRcpt", "_FinInstrmId", "_FwdReqInd", "_Issr", "_IssrDsclsrDdln", "_IssrDsclsrReqId", "_PlcOfJursdctn", "_PrvsDsclsrReqId", "_ReqShrHeldDt", "_RspnThrghChainInd", "_ShrhldrRghtsDrctvInd", "_ShrhldrsDsclsrRcrdDt", "_ShrsQtyThrshld", "_SplmtryData"]
	@property
	def AplblLaw(self):
		return self._AplblLaw

	@AplblLaw.setter
	def AplblLaw(self, value):
		self._AplblLaw = value if value is not None else base_types.UninitialisedField(self, 'AplblLaw', Max140Text, False)

	@AplblLaw.deleter
	def AplblLaw(self):
		del self._AplblLaw
		self._AplblLaw = base_types.UninitialisedField(self, 'AplblLaw', Max140Text, False)

	@property
	def DsclsrReqTp(self):
		return self._DsclsrReqTp

	@DsclsrReqTp.setter
	def DsclsrReqTp(self, value):
		self._DsclsrReqTp = value if value is not None else base_types.UninitialisedField(self, 'DsclsrReqTp', DisclosureRequestType1Code, False)

	@DsclsrReqTp.deleter
	def DsclsrReqTp(self):
		del self._DsclsrReqTp
		self._DsclsrReqTp = base_types.UninitialisedField(self, 'DsclsrReqTp', DisclosureRequestType1Code, False)

	@property
	def DsclsrRspnDdln(self):
		return self._DsclsrRspnDdln

	@DsclsrRspnDdln.setter
	def DsclsrRspnDdln(self, value):
		self._DsclsrRspnDdln = value if value is not None else base_types.UninitialisedField(self, 'DsclsrRspnDdln', DateFormat46Choice, False)

	@DsclsrRspnDdln.deleter
	def DsclsrRspnDdln(self):
		del self._DsclsrRspnDdln
		self._DsclsrRspnDdln = base_types.UninitialisedField(self, 'DsclsrRspnDdln', DateFormat46Choice, False)

	@property
	def DsclsrRspnRcpt(self):
		return self._DsclsrRspnRcpt

	@DsclsrRspnRcpt.setter
	def DsclsrRspnRcpt(self, value):
		self._DsclsrRspnRcpt = value if value is not None else base_types.UninitialisedField(self, 'DsclsrRspnRcpt', PartyIdentification214, False)

	@DsclsrRspnRcpt.deleter
	def DsclsrRspnRcpt(self):
		del self._DsclsrRspnRcpt
		self._DsclsrRspnRcpt = base_types.UninitialisedField(self, 'DsclsrRspnRcpt', PartyIdentification214, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def FwdReqInd(self):
		return self._FwdReqInd

	@FwdReqInd.setter
	def FwdReqInd(self, value):
		self._FwdReqInd = value if value is not None else base_types.UninitialisedField(self, 'FwdReqInd', YesNoIndicator, False)

	@FwdReqInd.deleter
	def FwdReqInd(self):
		del self._FwdReqInd
		self._FwdReqInd = base_types.UninitialisedField(self, 'FwdReqInd', YesNoIndicator, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification129Choice, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification129Choice, False)

	@property
	def IssrDsclsrDdln(self):
		return self._IssrDsclsrDdln

	@IssrDsclsrDdln.setter
	def IssrDsclsrDdln(self, value):
		self._IssrDsclsrDdln = value if value is not None else base_types.UninitialisedField(self, 'IssrDsclsrDdln', DateFormat46Choice, False)

	@IssrDsclsrDdln.deleter
	def IssrDsclsrDdln(self):
		del self._IssrDsclsrDdln
		self._IssrDsclsrDdln = base_types.UninitialisedField(self, 'IssrDsclsrDdln', DateFormat46Choice, False)

	@property
	def IssrDsclsrReqId(self):
		return self._IssrDsclsrReqId

	@IssrDsclsrReqId.setter
	def IssrDsclsrReqId(self, value):
		self._IssrDsclsrReqId = value if value is not None else base_types.UninitialisedField(self, 'IssrDsclsrReqId', Max35Text, False)

	@IssrDsclsrReqId.deleter
	def IssrDsclsrReqId(self):
		del self._IssrDsclsrReqId
		self._IssrDsclsrReqId = base_types.UninitialisedField(self, 'IssrDsclsrReqId', Max35Text, False)

	@property
	def PlcOfJursdctn(self):
		return self._PlcOfJursdctn

	@PlcOfJursdctn.setter
	def PlcOfJursdctn(self, value):
		self._PlcOfJursdctn = value if value is not None else base_types.UninitialisedField(self, 'PlcOfJursdctn', CountryCode, False)

	@PlcOfJursdctn.deleter
	def PlcOfJursdctn(self):
		del self._PlcOfJursdctn
		self._PlcOfJursdctn = base_types.UninitialisedField(self, 'PlcOfJursdctn', CountryCode, False)

	@property
	def PrvsDsclsrReqId(self):
		return self._PrvsDsclsrReqId

	@PrvsDsclsrReqId.setter
	def PrvsDsclsrReqId(self, value):
		self._PrvsDsclsrReqId = value if value is not None else base_types.UninitialisedField(self, 'PrvsDsclsrReqId', Max35Text, False)

	@PrvsDsclsrReqId.deleter
	def PrvsDsclsrReqId(self):
		del self._PrvsDsclsrReqId
		self._PrvsDsclsrReqId = base_types.UninitialisedField(self, 'PrvsDsclsrReqId', Max35Text, False)

	@property
	def ReqShrHeldDt(self):
		return self._ReqShrHeldDt

	@ReqShrHeldDt.setter
	def ReqShrHeldDt(self, value):
		self._ReqShrHeldDt = value if value is not None else base_types.UninitialisedField(self, 'ReqShrHeldDt', RequestShareHeldDate1Choice, False)

	@ReqShrHeldDt.deleter
	def ReqShrHeldDt(self):
		del self._ReqShrHeldDt
		self._ReqShrHeldDt = base_types.UninitialisedField(self, 'ReqShrHeldDt', RequestShareHeldDate1Choice, False)

	@property
	def RspnThrghChainInd(self):
		return self._RspnThrghChainInd

	@RspnThrghChainInd.setter
	def RspnThrghChainInd(self, value):
		self._RspnThrghChainInd = value if value is not None else base_types.UninitialisedField(self, 'RspnThrghChainInd', YesNoIndicator, False)

	@RspnThrghChainInd.deleter
	def RspnThrghChainInd(self):
		del self._RspnThrghChainInd
		self._RspnThrghChainInd = base_types.UninitialisedField(self, 'RspnThrghChainInd', YesNoIndicator, False)

	@property
	def ShrhldrRghtsDrctvInd(self):
		return self._ShrhldrRghtsDrctvInd

	@ShrhldrRghtsDrctvInd.setter
	def ShrhldrRghtsDrctvInd(self, value):
		self._ShrhldrRghtsDrctvInd = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrRghtsDrctvInd', YesNoIndicator, False)

	@ShrhldrRghtsDrctvInd.deleter
	def ShrhldrRghtsDrctvInd(self):
		del self._ShrhldrRghtsDrctvInd
		self._ShrhldrRghtsDrctvInd = base_types.UninitialisedField(self, 'ShrhldrRghtsDrctvInd', YesNoIndicator, False)

	@property
	def ShrhldrsDsclsrRcrdDt(self):
		return self._ShrhldrsDsclsrRcrdDt

	@ShrhldrsDsclsrRcrdDt.setter
	def ShrhldrsDsclsrRcrdDt(self, value):
		self._ShrhldrsDsclsrRcrdDt = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrsDsclsrRcrdDt', DateFormat46Choice, False)

	@ShrhldrsDsclsrRcrdDt.deleter
	def ShrhldrsDsclsrRcrdDt(self):
		del self._ShrhldrsDsclsrRcrdDt
		self._ShrhldrsDsclsrRcrdDt = base_types.UninitialisedField(self, 'ShrhldrsDsclsrRcrdDt', DateFormat46Choice, False)

	@property
	def ShrsQtyThrshld(self):
		return self._ShrsQtyThrshld

	@ShrsQtyThrshld.setter
	def ShrsQtyThrshld(self, value):
		self._ShrsQtyThrshld = value if value is not None else base_types.UninitialisedField(self, 'ShrsQtyThrshld', DecimalNumber, False)

	@ShrsQtyThrshld.deleter
	def ShrsQtyThrshld(self):
		del self._ShrsQtyThrshld
		self._ShrsQtyThrshld = base_types.UninitialisedField(self, 'ShrsQtyThrshld', DecimalNumber, False)

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
		base_types.FieldEntry(name='AplblLaw', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsclsrReqTp', type=DisclosureRequestType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsclsrRspnDdln', type=DateFormat46Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsclsrRspnRcpt', type=PartyIdentification214, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdReqInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrDdln', type=DateFormat46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfJursdctn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsDsclsrReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqShrHeldDt', type=RequestShareHeldDate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnThrghChainInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrRghtsDrctvInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrsDsclsrRcrdDt', type=DateFormat46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrsQtyThrshld', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))