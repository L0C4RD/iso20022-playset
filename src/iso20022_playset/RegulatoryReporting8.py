from . import base_types
from .Max10Text import Max10Text
from .PartyIdentification242Choice import PartyIdentification242Choice
from .SecurityIdentification19 import SecurityIdentification19
from .Max210Text import Max210Text
from .ISOTime import ISOTime
from .ProductIdentifier3Choice import ProductIdentifier3Choice
from .TradingSideTransactionReporting3 import TradingSideTransactionReporting3
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .CorporateSectorIdentifier1Code import CorporateSectorIdentifier1Code
from .ISODateTime import ISODateTime
from .AllocationIndicator1Code import AllocationIndicator1Code
from .FXCommissionOrFee1 import FXCommissionOrFee1
from .Max35Text import Max35Text
from .Exact42Text import Exact42Text
from .CollateralisationIndicator1Code import CollateralisationIndicator1Code
from .YesNoIndicator import YesNoIndicator
from .ClearingBrokerIdentification1 import ClearingBrokerIdentification1
from .CounterpartySideTransactionReporting3 import CounterpartySideTransactionReporting3

class RegulatoryReporting8(base_types._BaseFieldType):

	__slots__ = ["_AddtlRptgInf", "_ExctnVn", "_ConfDtAndTmstmp", "_AllcnInd", "_FinNtrOfTheCtrPtyInd", "_NonStdFlg", "_ComrclOrTrsrFincgInd", "_ClrXcptnPty", "_CollstnInd", "_PrtflCmprssnInd", "_FinInstrmId", "_ClrBrkrId", "_CorpSctrInd", "_TradgSdTxRptg", "_ComssnsAndFees", "_TradWthNonEEACtrPtyInd", "_LkSwpId", "_CollPrtflInd", "_ClrTmstmp", "_CollPrtflCd", "_ClrThrshldInd", "_ClrdPdctId", "_NtrgrpTradInd", "_ClrBrkr", "_ExctnTmstmp", "_PdctIdr", "_CtrPtySdTxRptg", "_CntrlCtrPtyClrHs"]
	@property
	def AddtlRptgInf(self):
		return self._AddtlRptgInf

	@AddtlRptgInf.setter
	def AddtlRptgInf(self, value):
		self._AddtlRptgInf = value if type(value) != base_types.auto else self.make_default("AddtlRptgInf")

	@AddtlRptgInf.deleter
	def AddtlRptgInf(self):
		del self._AddtlRptgInf
		self._AddtlRptgInf = None

	@property
	def ExctnVn(self):
		return self._ExctnVn

	@ExctnVn.setter
	def ExctnVn(self, value):
		self._ExctnVn = value if type(value) != base_types.auto else self.make_default("ExctnVn")

	@ExctnVn.deleter
	def ExctnVn(self):
		del self._ExctnVn
		self._ExctnVn = None

	@property
	def ConfDtAndTmstmp(self):
		return self._ConfDtAndTmstmp

	@ConfDtAndTmstmp.setter
	def ConfDtAndTmstmp(self, value):
		self._ConfDtAndTmstmp = value if type(value) != base_types.auto else self.make_default("ConfDtAndTmstmp")

	@ConfDtAndTmstmp.deleter
	def ConfDtAndTmstmp(self):
		del self._ConfDtAndTmstmp
		self._ConfDtAndTmstmp = None

	@property
	def AllcnInd(self):
		return self._AllcnInd

	@AllcnInd.setter
	def AllcnInd(self, value):
		self._AllcnInd = value if type(value) != base_types.auto else self.make_default("AllcnInd")

	@AllcnInd.deleter
	def AllcnInd(self):
		del self._AllcnInd
		self._AllcnInd = None

	@property
	def FinNtrOfTheCtrPtyInd(self):
		return self._FinNtrOfTheCtrPtyInd

	@FinNtrOfTheCtrPtyInd.setter
	def FinNtrOfTheCtrPtyInd(self, value):
		self._FinNtrOfTheCtrPtyInd = value if type(value) != base_types.auto else self.make_default("FinNtrOfTheCtrPtyInd")

	@FinNtrOfTheCtrPtyInd.deleter
	def FinNtrOfTheCtrPtyInd(self):
		del self._FinNtrOfTheCtrPtyInd
		self._FinNtrOfTheCtrPtyInd = None

	@property
	def NonStdFlg(self):
		return self._NonStdFlg

	@NonStdFlg.setter
	def NonStdFlg(self, value):
		self._NonStdFlg = value if type(value) != base_types.auto else self.make_default("NonStdFlg")

	@NonStdFlg.deleter
	def NonStdFlg(self):
		del self._NonStdFlg
		self._NonStdFlg = None

	@property
	def ComrclOrTrsrFincgInd(self):
		return self._ComrclOrTrsrFincgInd

	@ComrclOrTrsrFincgInd.setter
	def ComrclOrTrsrFincgInd(self, value):
		self._ComrclOrTrsrFincgInd = value if type(value) != base_types.auto else self.make_default("ComrclOrTrsrFincgInd")

	@ComrclOrTrsrFincgInd.deleter
	def ComrclOrTrsrFincgInd(self):
		del self._ComrclOrTrsrFincgInd
		self._ComrclOrTrsrFincgInd = None

	@property
	def ClrXcptnPty(self):
		return self._ClrXcptnPty

	@ClrXcptnPty.setter
	def ClrXcptnPty(self, value):
		self._ClrXcptnPty = value if type(value) != base_types.auto else self.make_default("ClrXcptnPty")

	@ClrXcptnPty.deleter
	def ClrXcptnPty(self):
		del self._ClrXcptnPty
		self._ClrXcptnPty = None

	@property
	def CollstnInd(self):
		return self._CollstnInd

	@CollstnInd.setter
	def CollstnInd(self, value):
		self._CollstnInd = value if type(value) != base_types.auto else self.make_default("CollstnInd")

	@CollstnInd.deleter
	def CollstnInd(self):
		del self._CollstnInd
		self._CollstnInd = None

	@property
	def PrtflCmprssnInd(self):
		return self._PrtflCmprssnInd

	@PrtflCmprssnInd.setter
	def PrtflCmprssnInd(self, value):
		self._PrtflCmprssnInd = value if type(value) != base_types.auto else self.make_default("PrtflCmprssnInd")

	@PrtflCmprssnInd.deleter
	def PrtflCmprssnInd(self):
		del self._PrtflCmprssnInd
		self._PrtflCmprssnInd = None

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
	def ClrBrkrId(self):
		return self._ClrBrkrId

	@ClrBrkrId.setter
	def ClrBrkrId(self, value):
		self._ClrBrkrId = value if type(value) != base_types.auto else self.make_default("ClrBrkrId")

	@ClrBrkrId.deleter
	def ClrBrkrId(self):
		del self._ClrBrkrId
		self._ClrBrkrId = None

	@property
	def CorpSctrInd(self):
		return self._CorpSctrInd

	@CorpSctrInd.setter
	def CorpSctrInd(self, value):
		self._CorpSctrInd = value if type(value) != base_types.auto else self.make_default("CorpSctrInd")

	@CorpSctrInd.deleter
	def CorpSctrInd(self):
		del self._CorpSctrInd
		self._CorpSctrInd = None

	@property
	def TradgSdTxRptg(self):
		return self._TradgSdTxRptg

	@TradgSdTxRptg.setter
	def TradgSdTxRptg(self, value):
		self._TradgSdTxRptg = value if type(value) != base_types.auto else self.make_default("TradgSdTxRptg")

	@TradgSdTxRptg.deleter
	def TradgSdTxRptg(self):
		del self._TradgSdTxRptg
		self._TradgSdTxRptg = None

	@property
	def ComssnsAndFees(self):
		return self._ComssnsAndFees

	@ComssnsAndFees.setter
	def ComssnsAndFees(self, value):
		self._ComssnsAndFees = value if type(value) != base_types.auto else self.make_default("ComssnsAndFees")

	@ComssnsAndFees.deleter
	def ComssnsAndFees(self):
		del self._ComssnsAndFees
		self._ComssnsAndFees = None

	@property
	def TradWthNonEEACtrPtyInd(self):
		return self._TradWthNonEEACtrPtyInd

	@TradWthNonEEACtrPtyInd.setter
	def TradWthNonEEACtrPtyInd(self, value):
		self._TradWthNonEEACtrPtyInd = value if type(value) != base_types.auto else self.make_default("TradWthNonEEACtrPtyInd")

	@TradWthNonEEACtrPtyInd.deleter
	def TradWthNonEEACtrPtyInd(self):
		del self._TradWthNonEEACtrPtyInd
		self._TradWthNonEEACtrPtyInd = None

	@property
	def LkSwpId(self):
		return self._LkSwpId

	@LkSwpId.setter
	def LkSwpId(self, value):
		self._LkSwpId = value if type(value) != base_types.auto else self.make_default("LkSwpId")

	@LkSwpId.deleter
	def LkSwpId(self):
		del self._LkSwpId
		self._LkSwpId = None

	@property
	def CollPrtflInd(self):
		return self._CollPrtflInd

	@CollPrtflInd.setter
	def CollPrtflInd(self, value):
		self._CollPrtflInd = value if type(value) != base_types.auto else self.make_default("CollPrtflInd")

	@CollPrtflInd.deleter
	def CollPrtflInd(self):
		del self._CollPrtflInd
		self._CollPrtflInd = None

	@property
	def ClrTmstmp(self):
		return self._ClrTmstmp

	@ClrTmstmp.setter
	def ClrTmstmp(self, value):
		self._ClrTmstmp = value if type(value) != base_types.auto else self.make_default("ClrTmstmp")

	@ClrTmstmp.deleter
	def ClrTmstmp(self):
		del self._ClrTmstmp
		self._ClrTmstmp = None

	@property
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if type(value) != base_types.auto else self.make_default("CollPrtflCd")

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = None

	@property
	def ClrThrshldInd(self):
		return self._ClrThrshldInd

	@ClrThrshldInd.setter
	def ClrThrshldInd(self, value):
		self._ClrThrshldInd = value if type(value) != base_types.auto else self.make_default("ClrThrshldInd")

	@ClrThrshldInd.deleter
	def ClrThrshldInd(self):
		del self._ClrThrshldInd
		self._ClrThrshldInd = None

	@property
	def ClrdPdctId(self):
		return self._ClrdPdctId

	@ClrdPdctId.setter
	def ClrdPdctId(self, value):
		self._ClrdPdctId = value if type(value) != base_types.auto else self.make_default("ClrdPdctId")

	@ClrdPdctId.deleter
	def ClrdPdctId(self):
		del self._ClrdPdctId
		self._ClrdPdctId = None

	@property
	def NtrgrpTradInd(self):
		return self._NtrgrpTradInd

	@NtrgrpTradInd.setter
	def NtrgrpTradInd(self, value):
		self._NtrgrpTradInd = value if type(value) != base_types.auto else self.make_default("NtrgrpTradInd")

	@NtrgrpTradInd.deleter
	def NtrgrpTradInd(self):
		del self._NtrgrpTradInd
		self._NtrgrpTradInd = None

	@property
	def ClrBrkr(self):
		return self._ClrBrkr

	@ClrBrkr.setter
	def ClrBrkr(self, value):
		self._ClrBrkr = value if type(value) != base_types.auto else self.make_default("ClrBrkr")

	@ClrBrkr.deleter
	def ClrBrkr(self):
		del self._ClrBrkr
		self._ClrBrkr = None

	@property
	def ExctnTmstmp(self):
		return self._ExctnTmstmp

	@ExctnTmstmp.setter
	def ExctnTmstmp(self, value):
		self._ExctnTmstmp = value if type(value) != base_types.auto else self.make_default("ExctnTmstmp")

	@ExctnTmstmp.deleter
	def ExctnTmstmp(self):
		del self._ExctnTmstmp
		self._ExctnTmstmp = None

	@property
	def PdctIdr(self):
		return self._PdctIdr

	@PdctIdr.setter
	def PdctIdr(self, value):
		self._PdctIdr = value if type(value) != base_types.auto else self.make_default("PdctIdr")

	@PdctIdr.deleter
	def PdctIdr(self):
		del self._PdctIdr
		self._PdctIdr = None

	@property
	def CtrPtySdTxRptg(self):
		return self._CtrPtySdTxRptg

	@CtrPtySdTxRptg.setter
	def CtrPtySdTxRptg(self, value):
		self._CtrPtySdTxRptg = value if type(value) != base_types.auto else self.make_default("CtrPtySdTxRptg")

	@CtrPtySdTxRptg.deleter
	def CtrPtySdTxRptg(self):
		del self._CtrPtySdTxRptg
		self._CtrPtySdTxRptg = None

	@property
	def CntrlCtrPtyClrHs(self):
		return self._CntrlCtrPtyClrHs

	@CntrlCtrPtyClrHs.setter
	def CntrlCtrPtyClrHs(self, value):
		self._CntrlCtrPtyClrHs = value if type(value) != base_types.auto else self.make_default("CntrlCtrPtyClrHs")

	@CntrlCtrPtyClrHs.deleter
	def CntrlCtrPtyClrHs(self):
		del self._CntrlCtrPtyClrHs
		self._CntrlCtrPtyClrHs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRptgInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnVn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfDtAndTmstmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllcnInd', type=AllocationIndicator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinNtrOfTheCtrPtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdFlg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComrclOrTrsrFincgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrXcptnPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollstnInd', type=CollateralisationIndicator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflCmprssnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrBrkrId', type=ClearingBrokerIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpSctrInd', type=CorporateSectorIdentifier1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdTxRptg', type=TradingSideTransactionReporting3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComssnsAndFees', type=FXCommissionOrFee1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradWthNonEEACtrPtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSwpId', type=Exact42Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrTmstmp', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflCd', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrThrshldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrdPdctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtrgrpTradInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrBrkr', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTmstmp', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctIdr', type=ProductIdentifier3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdTxRptg', type=CounterpartySideTransactionReporting3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CntrlCtrPtyClrHs', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
	))

