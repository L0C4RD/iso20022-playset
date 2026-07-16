# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection59
from . import DateAndDateTime2Choice
from . import Exact3NumericText
from . import InterestComputationMethodFormat5Choice
from . import LegalFramework4Choice
from . import Rate2
from . import RateName2
from . import RateOrName2Choice
from . import RateType67Choice
from . import RestrictedFINXMax140Text
from . import RestrictedFINXMax16Text
from . import RestrictedFINXMax52Text
from . import RevaluationIndicator4Choice
from . import TerminationDate7Choice
from . import YesNoIndicator

class SecuritiesFinancingTransactionDetails48(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_ChrgsRate", "_ClsgLegId", "_ComssnClctnDt", "_DealAmt", "_EarlstCallBckDt", "_FrftAmt", "_IntrstCmptnMtd", "_IntrstPmt", "_LclBrkrComssn", "_LglFrmwk", "_MtrtyDtMod", "_PricgRate", "_PrmAmt", "_RateChngDt", "_RateTp", "_RpRate", "_Rvaltn", "_ScndLegNrrtv", "_SctiesFincgTradId", "_SctiesHrcut", "_Sprd", "_StockLnMrgn", "_TermntnAmtPerPcOfColl", "_TermntnDt", "_TermntnTxAmt", "_TtlNbOfCollInstrs", "_TxCallDely", "_VarblRateSpprt"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection59, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection59, False)

	@property
	def ChrgsRate(self):
		return self._ChrgsRate

	@ChrgsRate.setter
	def ChrgsRate(self, value):
		self._ChrgsRate = value if value is not None else base_types.UninitialisedField(self, 'ChrgsRate', Rate2, False)

	@ChrgsRate.deleter
	def ChrgsRate(self):
		del self._ChrgsRate
		self._ChrgsRate = base_types.UninitialisedField(self, 'ChrgsRate', Rate2, False)

	@property
	def ClsgLegId(self):
		return self._ClsgLegId

	@ClsgLegId.setter
	def ClsgLegId(self, value):
		self._ClsgLegId = value if value is not None else base_types.UninitialisedField(self, 'ClsgLegId', RestrictedFINXMax16Text, False)

	@ClsgLegId.deleter
	def ClsgLegId(self):
		del self._ClsgLegId
		self._ClsgLegId = base_types.UninitialisedField(self, 'ClsgLegId', RestrictedFINXMax16Text, False)

	@property
	def ComssnClctnDt(self):
		return self._ComssnClctnDt

	@ComssnClctnDt.setter
	def ComssnClctnDt(self, value):
		self._ComssnClctnDt = value if value is not None else base_types.UninitialisedField(self, 'ComssnClctnDt', DateAndDateTime2Choice, False)

	@ComssnClctnDt.deleter
	def ComssnClctnDt(self):
		del self._ComssnClctnDt
		self._ComssnClctnDt = base_types.UninitialisedField(self, 'ComssnClctnDt', DateAndDateTime2Choice, False)

	@property
	def DealAmt(self):
		return self._DealAmt

	@DealAmt.setter
	def DealAmt(self, value):
		self._DealAmt = value if value is not None else base_types.UninitialisedField(self, 'DealAmt', AmountAndDirection59, False)

	@DealAmt.deleter
	def DealAmt(self):
		del self._DealAmt
		self._DealAmt = base_types.UninitialisedField(self, 'DealAmt', AmountAndDirection59, False)

	@property
	def EarlstCallBckDt(self):
		return self._EarlstCallBckDt

	@EarlstCallBckDt.setter
	def EarlstCallBckDt(self, value):
		self._EarlstCallBckDt = value if value is not None else base_types.UninitialisedField(self, 'EarlstCallBckDt', DateAndDateTime2Choice, False)

	@EarlstCallBckDt.deleter
	def EarlstCallBckDt(self):
		del self._EarlstCallBckDt
		self._EarlstCallBckDt = base_types.UninitialisedField(self, 'EarlstCallBckDt', DateAndDateTime2Choice, False)

	@property
	def FrftAmt(self):
		return self._FrftAmt

	@FrftAmt.setter
	def FrftAmt(self, value):
		self._FrftAmt = value if value is not None else base_types.UninitialisedField(self, 'FrftAmt', AmountAndDirection59, False)

	@FrftAmt.deleter
	def FrftAmt(self):
		del self._FrftAmt
		self._FrftAmt = base_types.UninitialisedField(self, 'FrftAmt', AmountAndDirection59, False)

	@property
	def IntrstCmptnMtd(self):
		return self._IntrstCmptnMtd

	@IntrstCmptnMtd.setter
	def IntrstCmptnMtd(self, value):
		self._IntrstCmptnMtd = value if value is not None else base_types.UninitialisedField(self, 'IntrstCmptnMtd', InterestComputationMethodFormat5Choice, False)

	@IntrstCmptnMtd.deleter
	def IntrstCmptnMtd(self):
		del self._IntrstCmptnMtd
		self._IntrstCmptnMtd = base_types.UninitialisedField(self, 'IntrstCmptnMtd', InterestComputationMethodFormat5Choice, False)

	@property
	def IntrstPmt(self):
		return self._IntrstPmt

	@IntrstPmt.setter
	def IntrstPmt(self, value):
		self._IntrstPmt = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmt', YesNoIndicator, False)

	@IntrstPmt.deleter
	def IntrstPmt(self):
		del self._IntrstPmt
		self._IntrstPmt = base_types.UninitialisedField(self, 'IntrstPmt', YesNoIndicator, False)

	@property
	def LclBrkrComssn(self):
		return self._LclBrkrComssn

	@LclBrkrComssn.setter
	def LclBrkrComssn(self, value):
		self._LclBrkrComssn = value if value is not None else base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection59, False)

	@LclBrkrComssn.deleter
	def LclBrkrComssn(self):
		del self._LclBrkrComssn
		self._LclBrkrComssn = base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection59, False)

	@property
	def LglFrmwk(self):
		return self._LglFrmwk

	@LglFrmwk.setter
	def LglFrmwk(self, value):
		self._LglFrmwk = value if value is not None else base_types.UninitialisedField(self, 'LglFrmwk', LegalFramework4Choice, False)

	@LglFrmwk.deleter
	def LglFrmwk(self):
		del self._LglFrmwk
		self._LglFrmwk = base_types.UninitialisedField(self, 'LglFrmwk', LegalFramework4Choice, False)

	@property
	def MtrtyDtMod(self):
		return self._MtrtyDtMod

	@MtrtyDtMod.setter
	def MtrtyDtMod(self, value):
		self._MtrtyDtMod = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDtMod', YesNoIndicator, False)

	@MtrtyDtMod.deleter
	def MtrtyDtMod(self):
		del self._MtrtyDtMod
		self._MtrtyDtMod = base_types.UninitialisedField(self, 'MtrtyDtMod', YesNoIndicator, False)

	@property
	def PricgRate(self):
		return self._PricgRate

	@PricgRate.setter
	def PricgRate(self, value):
		self._PricgRate = value if value is not None else base_types.UninitialisedField(self, 'PricgRate', RateOrName2Choice, False)

	@PricgRate.deleter
	def PricgRate(self):
		del self._PricgRate
		self._PricgRate = base_types.UninitialisedField(self, 'PricgRate', RateOrName2Choice, False)

	@property
	def PrmAmt(self):
		return self._PrmAmt

	@PrmAmt.setter
	def PrmAmt(self, value):
		self._PrmAmt = value if value is not None else base_types.UninitialisedField(self, 'PrmAmt', AmountAndDirection59, False)

	@PrmAmt.deleter
	def PrmAmt(self):
		del self._PrmAmt
		self._PrmAmt = base_types.UninitialisedField(self, 'PrmAmt', AmountAndDirection59, False)

	@property
	def RateChngDt(self):
		return self._RateChngDt

	@RateChngDt.setter
	def RateChngDt(self, value):
		self._RateChngDt = value if value is not None else base_types.UninitialisedField(self, 'RateChngDt', DateAndDateTime2Choice, False)

	@RateChngDt.deleter
	def RateChngDt(self):
		del self._RateChngDt
		self._RateChngDt = base_types.UninitialisedField(self, 'RateChngDt', DateAndDateTime2Choice, False)

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if value is not None else base_types.UninitialisedField(self, 'RateTp', RateType67Choice, False)

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = base_types.UninitialisedField(self, 'RateTp', RateType67Choice, False)

	@property
	def RpRate(self):
		return self._RpRate

	@RpRate.setter
	def RpRate(self, value):
		self._RpRate = value if value is not None else base_types.UninitialisedField(self, 'RpRate', Rate2, False)

	@RpRate.deleter
	def RpRate(self):
		del self._RpRate
		self._RpRate = base_types.UninitialisedField(self, 'RpRate', Rate2, False)

	@property
	def Rvaltn(self):
		return self._Rvaltn

	@Rvaltn.setter
	def Rvaltn(self, value):
		self._Rvaltn = value if value is not None else base_types.UninitialisedField(self, 'Rvaltn', RevaluationIndicator4Choice, False)

	@Rvaltn.deleter
	def Rvaltn(self):
		del self._Rvaltn
		self._Rvaltn = base_types.UninitialisedField(self, 'Rvaltn', RevaluationIndicator4Choice, False)

	@property
	def ScndLegNrrtv(self):
		return self._ScndLegNrrtv

	@ScndLegNrrtv.setter
	def ScndLegNrrtv(self, value):
		self._ScndLegNrrtv = value if value is not None else base_types.UninitialisedField(self, 'ScndLegNrrtv', RestrictedFINXMax140Text, False)

	@ScndLegNrrtv.deleter
	def ScndLegNrrtv(self):
		del self._ScndLegNrrtv
		self._ScndLegNrrtv = base_types.UninitialisedField(self, 'ScndLegNrrtv', RestrictedFINXMax140Text, False)

	@property
	def SctiesFincgTradId(self):
		return self._SctiesFincgTradId

	@SctiesFincgTradId.setter
	def SctiesFincgTradId(self, value):
		self._SctiesFincgTradId = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgTradId', RestrictedFINXMax52Text, False)

	@SctiesFincgTradId.deleter
	def SctiesFincgTradId(self):
		del self._SctiesFincgTradId
		self._SctiesFincgTradId = base_types.UninitialisedField(self, 'SctiesFincgTradId', RestrictedFINXMax52Text, False)

	@property
	def SctiesHrcut(self):
		return self._SctiesHrcut

	@SctiesHrcut.setter
	def SctiesHrcut(self, value):
		self._SctiesHrcut = value if value is not None else base_types.UninitialisedField(self, 'SctiesHrcut', Rate2, False)

	@SctiesHrcut.deleter
	def SctiesHrcut(self):
		del self._SctiesHrcut
		self._SctiesHrcut = base_types.UninitialisedField(self, 'SctiesHrcut', Rate2, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', Rate2, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', Rate2, False)

	@property
	def StockLnMrgn(self):
		return self._StockLnMrgn

	@StockLnMrgn.setter
	def StockLnMrgn(self, value):
		self._StockLnMrgn = value if value is not None else base_types.UninitialisedField(self, 'StockLnMrgn', Rate2, False)

	@StockLnMrgn.deleter
	def StockLnMrgn(self):
		del self._StockLnMrgn
		self._StockLnMrgn = base_types.UninitialisedField(self, 'StockLnMrgn', Rate2, False)

	@property
	def TermntnAmtPerPcOfColl(self):
		return self._TermntnAmtPerPcOfColl

	@TermntnAmtPerPcOfColl.setter
	def TermntnAmtPerPcOfColl(self, value):
		self._TermntnAmtPerPcOfColl = value if value is not None else base_types.UninitialisedField(self, 'TermntnAmtPerPcOfColl', AmountAndDirection59, False)

	@TermntnAmtPerPcOfColl.deleter
	def TermntnAmtPerPcOfColl(self):
		del self._TermntnAmtPerPcOfColl
		self._TermntnAmtPerPcOfColl = base_types.UninitialisedField(self, 'TermntnAmtPerPcOfColl', AmountAndDirection59, False)

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if value is not None else base_types.UninitialisedField(self, 'TermntnDt', TerminationDate7Choice, False)

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = base_types.UninitialisedField(self, 'TermntnDt', TerminationDate7Choice, False)

	@property
	def TermntnTxAmt(self):
		return self._TermntnTxAmt

	@TermntnTxAmt.setter
	def TermntnTxAmt(self, value):
		self._TermntnTxAmt = value if value is not None else base_types.UninitialisedField(self, 'TermntnTxAmt', AmountAndDirection59, False)

	@TermntnTxAmt.deleter
	def TermntnTxAmt(self):
		del self._TermntnTxAmt
		self._TermntnTxAmt = base_types.UninitialisedField(self, 'TermntnTxAmt', AmountAndDirection59, False)

	@property
	def TtlNbOfCollInstrs(self):
		return self._TtlNbOfCollInstrs

	@TtlNbOfCollInstrs.setter
	def TtlNbOfCollInstrs(self, value):
		self._TtlNbOfCollInstrs = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfCollInstrs', Exact3NumericText, False)

	@TtlNbOfCollInstrs.deleter
	def TtlNbOfCollInstrs(self):
		del self._TtlNbOfCollInstrs
		self._TtlNbOfCollInstrs = base_types.UninitialisedField(self, 'TtlNbOfCollInstrs', Exact3NumericText, False)

	@property
	def TxCallDely(self):
		return self._TxCallDely

	@TxCallDely.setter
	def TxCallDely(self, value):
		self._TxCallDely = value if value is not None else base_types.UninitialisedField(self, 'TxCallDely', Exact3NumericText, False)

	@TxCallDely.deleter
	def TxCallDely(self):
		del self._TxCallDely
		self._TxCallDely = base_types.UninitialisedField(self, 'TxCallDely', Exact3NumericText, False)

	@property
	def VarblRateSpprt(self):
		return self._VarblRateSpprt

	@VarblRateSpprt.setter
	def VarblRateSpprt(self, value):
		self._VarblRateSpprt = value if value is not None else base_types.UninitialisedField(self, 'VarblRateSpprt', RateName2, False)

	@VarblRateSpprt.deleter
	def VarblRateSpprt(self):
		del self._VarblRateSpprt
		self._VarblRateSpprt = base_types.UninitialisedField(self, 'VarblRateSpprt', RateName2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgLegId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnClctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealAmt', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstCallBckDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrftAmt', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstCmptnMtd', type=InterestComputationMethodFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPmt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglFrmwk', type=LegalFramework4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDtMod', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgRate', type=RateOrName2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmAmt', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateChngDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType67Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvaltn', type=RevaluationIndicator4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLegNrrtv', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTradId', type=RestrictedFINXMax52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesHrcut', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockLnMrgn', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnAmtPerPcOfColl', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=TerminationDate7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnTxAmt', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfCollInstrs', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCallDely', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateSpprt', type=RateName2, min=0, max=1, mutex_group=None, array=False),
	))