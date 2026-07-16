# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AllocationIndicator1Code
from . import ClearingBrokerIdentification1
from . import CollateralisationIndicator1Code
from . import CorporateSectorIdentifier1Code
from . import CounterpartySideTransactionReporting3
from . import DateAndDateTime2Choice
from . import Exact42Text
from . import FXCommissionOrFee1
from . import ISODateTime
from . import ISOTime
from . import Max10Text
from . import Max210Text
from . import Max35Text
from . import PartyIdentification242Choice
from . import ProductIdentifier3Choice
from . import SecurityIdentification19
from . import TradingSideTransactionReporting3
from . import YesNoIndicator

class RegulatoryReporting8(base_types._BaseFieldType):

	__slots__ = ["_AddtlRptgInf", "_AllcnInd", "_ClrBrkr", "_ClrBrkrId", "_ClrThrshldInd", "_ClrTmstmp", "_ClrXcptnPty", "_ClrdPdctId", "_CntrlCtrPtyClrHs", "_CollPrtflCd", "_CollPrtflInd", "_CollstnInd", "_ComrclOrTrsrFincgInd", "_ComssnsAndFees", "_ConfDtAndTmstmp", "_CorpSctrInd", "_CtrPtySdTxRptg", "_ExctnTmstmp", "_ExctnVn", "_FinInstrmId", "_FinNtrOfTheCtrPtyInd", "_LkSwpId", "_NonStdFlg", "_NtrgrpTradInd", "_PdctIdr", "_PrtflCmprssnInd", "_TradWthNonEEACtrPtyInd", "_TradgSdTxRptg"]
	@property
	def AddtlRptgInf(self):
		return self._AddtlRptgInf

	@AddtlRptgInf.setter
	def AddtlRptgInf(self, value):
		self._AddtlRptgInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRptgInf', Max210Text, False)

	@AddtlRptgInf.deleter
	def AddtlRptgInf(self):
		del self._AddtlRptgInf
		self._AddtlRptgInf = base_types.UninitialisedField(self, 'AddtlRptgInf', Max210Text, False)

	@property
	def AllcnInd(self):
		return self._AllcnInd

	@AllcnInd.setter
	def AllcnInd(self, value):
		self._AllcnInd = value if value is not None else base_types.UninitialisedField(self, 'AllcnInd', AllocationIndicator1Code, False)

	@AllcnInd.deleter
	def AllcnInd(self):
		del self._AllcnInd
		self._AllcnInd = base_types.UninitialisedField(self, 'AllcnInd', AllocationIndicator1Code, False)

	@property
	def ClrBrkr(self):
		return self._ClrBrkr

	@ClrBrkr.setter
	def ClrBrkr(self, value):
		self._ClrBrkr = value if value is not None else base_types.UninitialisedField(self, 'ClrBrkr', PartyIdentification242Choice, False)

	@ClrBrkr.deleter
	def ClrBrkr(self):
		del self._ClrBrkr
		self._ClrBrkr = base_types.UninitialisedField(self, 'ClrBrkr', PartyIdentification242Choice, False)

	@property
	def ClrBrkrId(self):
		return self._ClrBrkrId

	@ClrBrkrId.setter
	def ClrBrkrId(self, value):
		self._ClrBrkrId = value if value is not None else base_types.UninitialisedField(self, 'ClrBrkrId', ClearingBrokerIdentification1, False)

	@ClrBrkrId.deleter
	def ClrBrkrId(self):
		del self._ClrBrkrId
		self._ClrBrkrId = base_types.UninitialisedField(self, 'ClrBrkrId', ClearingBrokerIdentification1, False)

	@property
	def ClrThrshldInd(self):
		return self._ClrThrshldInd

	@ClrThrshldInd.setter
	def ClrThrshldInd(self, value):
		self._ClrThrshldInd = value if value is not None else base_types.UninitialisedField(self, 'ClrThrshldInd', YesNoIndicator, False)

	@ClrThrshldInd.deleter
	def ClrThrshldInd(self):
		del self._ClrThrshldInd
		self._ClrThrshldInd = base_types.UninitialisedField(self, 'ClrThrshldInd', YesNoIndicator, False)

	@property
	def ClrTmstmp(self):
		return self._ClrTmstmp

	@ClrTmstmp.setter
	def ClrTmstmp(self, value):
		self._ClrTmstmp = value if value is not None else base_types.UninitialisedField(self, 'ClrTmstmp', ISOTime, False)

	@ClrTmstmp.deleter
	def ClrTmstmp(self):
		del self._ClrTmstmp
		self._ClrTmstmp = base_types.UninitialisedField(self, 'ClrTmstmp', ISOTime, False)

	@property
	def ClrXcptnPty(self):
		return self._ClrXcptnPty

	@ClrXcptnPty.setter
	def ClrXcptnPty(self, value):
		self._ClrXcptnPty = value if value is not None else base_types.UninitialisedField(self, 'ClrXcptnPty', PartyIdentification242Choice, False)

	@ClrXcptnPty.deleter
	def ClrXcptnPty(self):
		del self._ClrXcptnPty
		self._ClrXcptnPty = base_types.UninitialisedField(self, 'ClrXcptnPty', PartyIdentification242Choice, False)

	@property
	def ClrdPdctId(self):
		return self._ClrdPdctId

	@ClrdPdctId.setter
	def ClrdPdctId(self, value):
		self._ClrdPdctId = value if value is not None else base_types.UninitialisedField(self, 'ClrdPdctId', Max35Text, False)

	@ClrdPdctId.deleter
	def ClrdPdctId(self):
		del self._ClrdPdctId
		self._ClrdPdctId = base_types.UninitialisedField(self, 'ClrdPdctId', Max35Text, False)

	@property
	def CntrlCtrPtyClrHs(self):
		return self._CntrlCtrPtyClrHs

	@CntrlCtrPtyClrHs.setter
	def CntrlCtrPtyClrHs(self, value):
		self._CntrlCtrPtyClrHs = value if value is not None else base_types.UninitialisedField(self, 'CntrlCtrPtyClrHs', PartyIdentification242Choice, False)

	@CntrlCtrPtyClrHs.deleter
	def CntrlCtrPtyClrHs(self):
		del self._CntrlCtrPtyClrHs
		self._CntrlCtrPtyClrHs = base_types.UninitialisedField(self, 'CntrlCtrPtyClrHs', PartyIdentification242Choice, False)

	@property
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if value is not None else base_types.UninitialisedField(self, 'CollPrtflCd', Max10Text, False)

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = base_types.UninitialisedField(self, 'CollPrtflCd', Max10Text, False)

	@property
	def CollPrtflInd(self):
		return self._CollPrtflInd

	@CollPrtflInd.setter
	def CollPrtflInd(self, value):
		self._CollPrtflInd = value if value is not None else base_types.UninitialisedField(self, 'CollPrtflInd', YesNoIndicator, False)

	@CollPrtflInd.deleter
	def CollPrtflInd(self):
		del self._CollPrtflInd
		self._CollPrtflInd = base_types.UninitialisedField(self, 'CollPrtflInd', YesNoIndicator, False)

	@property
	def CollstnInd(self):
		return self._CollstnInd

	@CollstnInd.setter
	def CollstnInd(self, value):
		self._CollstnInd = value if value is not None else base_types.UninitialisedField(self, 'CollstnInd', CollateralisationIndicator1Code, False)

	@CollstnInd.deleter
	def CollstnInd(self):
		del self._CollstnInd
		self._CollstnInd = base_types.UninitialisedField(self, 'CollstnInd', CollateralisationIndicator1Code, False)

	@property
	def ComrclOrTrsrFincgInd(self):
		return self._ComrclOrTrsrFincgInd

	@ComrclOrTrsrFincgInd.setter
	def ComrclOrTrsrFincgInd(self, value):
		self._ComrclOrTrsrFincgInd = value if value is not None else base_types.UninitialisedField(self, 'ComrclOrTrsrFincgInd', YesNoIndicator, False)

	@ComrclOrTrsrFincgInd.deleter
	def ComrclOrTrsrFincgInd(self):
		del self._ComrclOrTrsrFincgInd
		self._ComrclOrTrsrFincgInd = base_types.UninitialisedField(self, 'ComrclOrTrsrFincgInd', YesNoIndicator, False)

	@property
	def ComssnsAndFees(self):
		return self._ComssnsAndFees

	@ComssnsAndFees.setter
	def ComssnsAndFees(self, value):
		self._ComssnsAndFees = value if value is not None else base_types.UninitialisedField(self, 'ComssnsAndFees', FXCommissionOrFee1, True)

	@ComssnsAndFees.deleter
	def ComssnsAndFees(self):
		del self._ComssnsAndFees
		self._ComssnsAndFees = base_types.UninitialisedField(self, 'ComssnsAndFees', FXCommissionOrFee1, True)

	@property
	def ConfDtAndTmstmp(self):
		return self._ConfDtAndTmstmp

	@ConfDtAndTmstmp.setter
	def ConfDtAndTmstmp(self, value):
		self._ConfDtAndTmstmp = value if value is not None else base_types.UninitialisedField(self, 'ConfDtAndTmstmp', ISODateTime, False)

	@ConfDtAndTmstmp.deleter
	def ConfDtAndTmstmp(self):
		del self._ConfDtAndTmstmp
		self._ConfDtAndTmstmp = base_types.UninitialisedField(self, 'ConfDtAndTmstmp', ISODateTime, False)

	@property
	def CorpSctrInd(self):
		return self._CorpSctrInd

	@CorpSctrInd.setter
	def CorpSctrInd(self, value):
		self._CorpSctrInd = value if value is not None else base_types.UninitialisedField(self, 'CorpSctrInd', CorporateSectorIdentifier1Code, False)

	@CorpSctrInd.deleter
	def CorpSctrInd(self):
		del self._CorpSctrInd
		self._CorpSctrInd = base_types.UninitialisedField(self, 'CorpSctrInd', CorporateSectorIdentifier1Code, False)

	@property
	def CtrPtySdTxRptg(self):
		return self._CtrPtySdTxRptg

	@CtrPtySdTxRptg.setter
	def CtrPtySdTxRptg(self, value):
		self._CtrPtySdTxRptg = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySdTxRptg', CounterpartySideTransactionReporting3, True)

	@CtrPtySdTxRptg.deleter
	def CtrPtySdTxRptg(self):
		del self._CtrPtySdTxRptg
		self._CtrPtySdTxRptg = base_types.UninitialisedField(self, 'CtrPtySdTxRptg', CounterpartySideTransactionReporting3, True)

	@property
	def ExctnTmstmp(self):
		return self._ExctnTmstmp

	@ExctnTmstmp.setter
	def ExctnTmstmp(self, value):
		self._ExctnTmstmp = value if value is not None else base_types.UninitialisedField(self, 'ExctnTmstmp', DateAndDateTime2Choice, False)

	@ExctnTmstmp.deleter
	def ExctnTmstmp(self):
		del self._ExctnTmstmp
		self._ExctnTmstmp = base_types.UninitialisedField(self, 'ExctnTmstmp', DateAndDateTime2Choice, False)

	@property
	def ExctnVn(self):
		return self._ExctnVn

	@ExctnVn.setter
	def ExctnVn(self, value):
		self._ExctnVn = value if value is not None else base_types.UninitialisedField(self, 'ExctnVn', Max35Text, False)

	@ExctnVn.deleter
	def ExctnVn(self):
		del self._ExctnVn
		self._ExctnVn = base_types.UninitialisedField(self, 'ExctnVn', Max35Text, False)

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
	def FinNtrOfTheCtrPtyInd(self):
		return self._FinNtrOfTheCtrPtyInd

	@FinNtrOfTheCtrPtyInd.setter
	def FinNtrOfTheCtrPtyInd(self, value):
		self._FinNtrOfTheCtrPtyInd = value if value is not None else base_types.UninitialisedField(self, 'FinNtrOfTheCtrPtyInd', YesNoIndicator, False)

	@FinNtrOfTheCtrPtyInd.deleter
	def FinNtrOfTheCtrPtyInd(self):
		del self._FinNtrOfTheCtrPtyInd
		self._FinNtrOfTheCtrPtyInd = base_types.UninitialisedField(self, 'FinNtrOfTheCtrPtyInd', YesNoIndicator, False)

	@property
	def LkSwpId(self):
		return self._LkSwpId

	@LkSwpId.setter
	def LkSwpId(self, value):
		self._LkSwpId = value if value is not None else base_types.UninitialisedField(self, 'LkSwpId', Exact42Text, False)

	@LkSwpId.deleter
	def LkSwpId(self):
		del self._LkSwpId
		self._LkSwpId = base_types.UninitialisedField(self, 'LkSwpId', Exact42Text, False)

	@property
	def NonStdFlg(self):
		return self._NonStdFlg

	@NonStdFlg.setter
	def NonStdFlg(self, value):
		self._NonStdFlg = value if value is not None else base_types.UninitialisedField(self, 'NonStdFlg', YesNoIndicator, False)

	@NonStdFlg.deleter
	def NonStdFlg(self):
		del self._NonStdFlg
		self._NonStdFlg = base_types.UninitialisedField(self, 'NonStdFlg', YesNoIndicator, False)

	@property
	def NtrgrpTradInd(self):
		return self._NtrgrpTradInd

	@NtrgrpTradInd.setter
	def NtrgrpTradInd(self, value):
		self._NtrgrpTradInd = value if value is not None else base_types.UninitialisedField(self, 'NtrgrpTradInd', YesNoIndicator, False)

	@NtrgrpTradInd.deleter
	def NtrgrpTradInd(self):
		del self._NtrgrpTradInd
		self._NtrgrpTradInd = base_types.UninitialisedField(self, 'NtrgrpTradInd', YesNoIndicator, False)

	@property
	def PdctIdr(self):
		return self._PdctIdr

	@PdctIdr.setter
	def PdctIdr(self, value):
		self._PdctIdr = value if value is not None else base_types.UninitialisedField(self, 'PdctIdr', ProductIdentifier3Choice, False)

	@PdctIdr.deleter
	def PdctIdr(self):
		del self._PdctIdr
		self._PdctIdr = base_types.UninitialisedField(self, 'PdctIdr', ProductIdentifier3Choice, False)

	@property
	def PrtflCmprssnInd(self):
		return self._PrtflCmprssnInd

	@PrtflCmprssnInd.setter
	def PrtflCmprssnInd(self, value):
		self._PrtflCmprssnInd = value if value is not None else base_types.UninitialisedField(self, 'PrtflCmprssnInd', YesNoIndicator, False)

	@PrtflCmprssnInd.deleter
	def PrtflCmprssnInd(self):
		del self._PrtflCmprssnInd
		self._PrtflCmprssnInd = base_types.UninitialisedField(self, 'PrtflCmprssnInd', YesNoIndicator, False)

	@property
	def TradWthNonEEACtrPtyInd(self):
		return self._TradWthNonEEACtrPtyInd

	@TradWthNonEEACtrPtyInd.setter
	def TradWthNonEEACtrPtyInd(self, value):
		self._TradWthNonEEACtrPtyInd = value if value is not None else base_types.UninitialisedField(self, 'TradWthNonEEACtrPtyInd', YesNoIndicator, False)

	@TradWthNonEEACtrPtyInd.deleter
	def TradWthNonEEACtrPtyInd(self):
		del self._TradWthNonEEACtrPtyInd
		self._TradWthNonEEACtrPtyInd = base_types.UninitialisedField(self, 'TradWthNonEEACtrPtyInd', YesNoIndicator, False)

	@property
	def TradgSdTxRptg(self):
		return self._TradgSdTxRptg

	@TradgSdTxRptg.setter
	def TradgSdTxRptg(self, value):
		self._TradgSdTxRptg = value if value is not None else base_types.UninitialisedField(self, 'TradgSdTxRptg', TradingSideTransactionReporting3, True)

	@TradgSdTxRptg.deleter
	def TradgSdTxRptg(self):
		del self._TradgSdTxRptg
		self._TradgSdTxRptg = base_types.UninitialisedField(self, 'TradgSdTxRptg', TradingSideTransactionReporting3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRptgInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllcnInd', type=AllocationIndicator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrBrkr', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrBrkrId', type=ClearingBrokerIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrThrshldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrTmstmp', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrXcptnPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrdPdctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrlCtrPtyClrHs', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflCd', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollstnInd', type=CollateralisationIndicator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComrclOrTrsrFincgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnsAndFees', type=FXCommissionOrFee1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfDtAndTmstmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpSctrInd', type=CorporateSectorIdentifier1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdTxRptg', type=CounterpartySideTransactionReporting3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ExctnTmstmp', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnVn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinNtrOfTheCtrPtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSwpId', type=Exact42Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdFlg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtrgrpTradInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctIdr', type=ProductIdentifier3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflCmprssnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradWthNonEEACtrPtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdTxRptg', type=TradingSideTransactionReporting3, min=0, max=None, mutex_group=None, array=True),
	))