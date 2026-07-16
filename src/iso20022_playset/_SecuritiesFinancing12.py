# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Agreement5
from . import AmountAndDirection5
from . import BaseOneRate
from . import BorrowingReason2Choice
from . import CollateralType4Choice
from . import ISODate
from . import ISODateTime
from . import InterestComputationMethod3Choice
from . import LegalFramework1Code
from . import LendingTransactionMethod2Choice
from . import Max3Number
from . import Max3NumericText
from . import Number24Choice
from . import PercentageRate
from . import Rate2
from . import RateName1
from . import RateOrName1Choice
from . import RateType35Choice
from . import Revaluation3Choice
from . import Reversible2Choice
from . import SecuritiesLendingType2Choice
from . import SpreadRate1
from . import YesNoIndicator

class SecuritiesFinancing12(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_AcrdIntrstPctg", "_AcrdIntrstTax", "_BrrwgRate", "_BrrwgRsn", "_CllblTradInd", "_ClsgAmtPerPcsOfColl", "_CollTp", "_CtrctTermsModChngd", "_DvddRatio", "_EndFctr", "_EndNbOfDaysAcrd", "_ExCpn", "_FincgAgrmt", "_FrftAmt", "_IntrstCmptnMtd", "_IntrstRate", "_LglFrmwk", "_LndgTxMtd", "_LndgWthColl", "_MinDtForCallBck", "_NbOfDaysLndgBrrwg", "_PrdcPmt", "_PricgRate", "_PrmAmt", "_RateChngDt", "_RateTp", "_RollOver", "_RpRate", "_Rvaltn", "_Rvsbl", "_SctiesHrcut", "_SctiesLndgTp", "_SprdRate", "_StdCollAmt", "_StdCollRatio", "_StockLnMrgn", "_TtlNbOfCollInstrs", "_TxCallDely", "_VarblRateSpprt"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection5, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection5, False)

	@property
	def AcrdIntrstPctg(self):
		return self._AcrdIntrstPctg

	@AcrdIntrstPctg.setter
	def AcrdIntrstPctg(self, value):
		self._AcrdIntrstPctg = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstPctg', PercentageRate, False)

	@AcrdIntrstPctg.deleter
	def AcrdIntrstPctg(self):
		del self._AcrdIntrstPctg
		self._AcrdIntrstPctg = base_types.UninitialisedField(self, 'AcrdIntrstPctg', PercentageRate, False)

	@property
	def AcrdIntrstTax(self):
		return self._AcrdIntrstTax

	@AcrdIntrstTax.setter
	def AcrdIntrstTax(self, value):
		self._AcrdIntrstTax = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstTax', YesNoIndicator, False)

	@AcrdIntrstTax.deleter
	def AcrdIntrstTax(self):
		del self._AcrdIntrstTax
		self._AcrdIntrstTax = base_types.UninitialisedField(self, 'AcrdIntrstTax', YesNoIndicator, False)

	@property
	def BrrwgRate(self):
		return self._BrrwgRate

	@BrrwgRate.setter
	def BrrwgRate(self, value):
		self._BrrwgRate = value if value is not None else base_types.UninitialisedField(self, 'BrrwgRate', Rate2, False)

	@BrrwgRate.deleter
	def BrrwgRate(self):
		del self._BrrwgRate
		self._BrrwgRate = base_types.UninitialisedField(self, 'BrrwgRate', Rate2, False)

	@property
	def BrrwgRsn(self):
		return self._BrrwgRsn

	@BrrwgRsn.setter
	def BrrwgRsn(self, value):
		self._BrrwgRsn = value if value is not None else base_types.UninitialisedField(self, 'BrrwgRsn', BorrowingReason2Choice, False)

	@BrrwgRsn.deleter
	def BrrwgRsn(self):
		del self._BrrwgRsn
		self._BrrwgRsn = base_types.UninitialisedField(self, 'BrrwgRsn', BorrowingReason2Choice, False)

	@property
	def CllblTradInd(self):
		return self._CllblTradInd

	@CllblTradInd.setter
	def CllblTradInd(self, value):
		self._CllblTradInd = value if value is not None else base_types.UninitialisedField(self, 'CllblTradInd', YesNoIndicator, False)

	@CllblTradInd.deleter
	def CllblTradInd(self):
		del self._CllblTradInd
		self._CllblTradInd = base_types.UninitialisedField(self, 'CllblTradInd', YesNoIndicator, False)

	@property
	def ClsgAmtPerPcsOfColl(self):
		return self._ClsgAmtPerPcsOfColl

	@ClsgAmtPerPcsOfColl.setter
	def ClsgAmtPerPcsOfColl(self, value):
		self._ClsgAmtPerPcsOfColl = value if value is not None else base_types.UninitialisedField(self, 'ClsgAmtPerPcsOfColl', AmountAndDirection5, False)

	@ClsgAmtPerPcsOfColl.deleter
	def ClsgAmtPerPcsOfColl(self):
		del self._ClsgAmtPerPcsOfColl
		self._ClsgAmtPerPcsOfColl = base_types.UninitialisedField(self, 'ClsgAmtPerPcsOfColl', AmountAndDirection5, False)

	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if value is not None else base_types.UninitialisedField(self, 'CollTp', CollateralType4Choice, False)

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = base_types.UninitialisedField(self, 'CollTp', CollateralType4Choice, False)

	@property
	def CtrctTermsModChngd(self):
		return self._CtrctTermsModChngd

	@CtrctTermsModChngd.setter
	def CtrctTermsModChngd(self, value):
		self._CtrctTermsModChngd = value if value is not None else base_types.UninitialisedField(self, 'CtrctTermsModChngd', YesNoIndicator, False)

	@CtrctTermsModChngd.deleter
	def CtrctTermsModChngd(self):
		del self._CtrctTermsModChngd
		self._CtrctTermsModChngd = base_types.UninitialisedField(self, 'CtrctTermsModChngd', YesNoIndicator, False)

	@property
	def DvddRatio(self):
		return self._DvddRatio

	@DvddRatio.setter
	def DvddRatio(self, value):
		self._DvddRatio = value if value is not None else base_types.UninitialisedField(self, 'DvddRatio', Rate2, False)

	@DvddRatio.deleter
	def DvddRatio(self):
		del self._DvddRatio
		self._DvddRatio = base_types.UninitialisedField(self, 'DvddRatio', Rate2, False)

	@property
	def EndFctr(self):
		return self._EndFctr

	@EndFctr.setter
	def EndFctr(self, value):
		self._EndFctr = value if value is not None else base_types.UninitialisedField(self, 'EndFctr', BaseOneRate, False)

	@EndFctr.deleter
	def EndFctr(self):
		del self._EndFctr
		self._EndFctr = base_types.UninitialisedField(self, 'EndFctr', BaseOneRate, False)

	@property
	def EndNbOfDaysAcrd(self):
		return self._EndNbOfDaysAcrd

	@EndNbOfDaysAcrd.setter
	def EndNbOfDaysAcrd(self, value):
		self._EndNbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'EndNbOfDaysAcrd', Max3Number, False)

	@EndNbOfDaysAcrd.deleter
	def EndNbOfDaysAcrd(self):
		del self._EndNbOfDaysAcrd
		self._EndNbOfDaysAcrd = base_types.UninitialisedField(self, 'EndNbOfDaysAcrd', Max3Number, False)

	@property
	def ExCpn(self):
		return self._ExCpn

	@ExCpn.setter
	def ExCpn(self, value):
		self._ExCpn = value if value is not None else base_types.UninitialisedField(self, 'ExCpn', YesNoIndicator, False)

	@ExCpn.deleter
	def ExCpn(self):
		del self._ExCpn
		self._ExCpn = base_types.UninitialisedField(self, 'ExCpn', YesNoIndicator, False)

	@property
	def FincgAgrmt(self):
		return self._FincgAgrmt

	@FincgAgrmt.setter
	def FincgAgrmt(self, value):
		self._FincgAgrmt = value if value is not None else base_types.UninitialisedField(self, 'FincgAgrmt', Agreement5, False)

	@FincgAgrmt.deleter
	def FincgAgrmt(self):
		del self._FincgAgrmt
		self._FincgAgrmt = base_types.UninitialisedField(self, 'FincgAgrmt', Agreement5, False)

	@property
	def FrftAmt(self):
		return self._FrftAmt

	@FrftAmt.setter
	def FrftAmt(self, value):
		self._FrftAmt = value if value is not None else base_types.UninitialisedField(self, 'FrftAmt', AmountAndDirection5, False)

	@FrftAmt.deleter
	def FrftAmt(self):
		del self._FrftAmt
		self._FrftAmt = base_types.UninitialisedField(self, 'FrftAmt', AmountAndDirection5, False)

	@property
	def IntrstCmptnMtd(self):
		return self._IntrstCmptnMtd

	@IntrstCmptnMtd.setter
	def IntrstCmptnMtd(self, value):
		self._IntrstCmptnMtd = value if value is not None else base_types.UninitialisedField(self, 'IntrstCmptnMtd', InterestComputationMethod3Choice, False)

	@IntrstCmptnMtd.deleter
	def IntrstCmptnMtd(self):
		del self._IntrstCmptnMtd
		self._IntrstCmptnMtd = base_types.UninitialisedField(self, 'IntrstCmptnMtd', InterestComputationMethod3Choice, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', Rate2, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', Rate2, False)

	@property
	def LglFrmwk(self):
		return self._LglFrmwk

	@LglFrmwk.setter
	def LglFrmwk(self, value):
		self._LglFrmwk = value if value is not None else base_types.UninitialisedField(self, 'LglFrmwk', LegalFramework1Code, False)

	@LglFrmwk.deleter
	def LglFrmwk(self):
		del self._LglFrmwk
		self._LglFrmwk = base_types.UninitialisedField(self, 'LglFrmwk', LegalFramework1Code, False)

	@property
	def LndgTxMtd(self):
		return self._LndgTxMtd

	@LndgTxMtd.setter
	def LndgTxMtd(self, value):
		self._LndgTxMtd = value if value is not None else base_types.UninitialisedField(self, 'LndgTxMtd', LendingTransactionMethod2Choice, False)

	@LndgTxMtd.deleter
	def LndgTxMtd(self):
		del self._LndgTxMtd
		self._LndgTxMtd = base_types.UninitialisedField(self, 'LndgTxMtd', LendingTransactionMethod2Choice, False)

	@property
	def LndgWthColl(self):
		return self._LndgWthColl

	@LndgWthColl.setter
	def LndgWthColl(self, value):
		self._LndgWthColl = value if value is not None else base_types.UninitialisedField(self, 'LndgWthColl', YesNoIndicator, False)

	@LndgWthColl.deleter
	def LndgWthColl(self):
		del self._LndgWthColl
		self._LndgWthColl = base_types.UninitialisedField(self, 'LndgWthColl', YesNoIndicator, False)

	@property
	def MinDtForCallBck(self):
		return self._MinDtForCallBck

	@MinDtForCallBck.setter
	def MinDtForCallBck(self, value):
		self._MinDtForCallBck = value if value is not None else base_types.UninitialisedField(self, 'MinDtForCallBck', ISODate, False)

	@MinDtForCallBck.deleter
	def MinDtForCallBck(self):
		del self._MinDtForCallBck
		self._MinDtForCallBck = base_types.UninitialisedField(self, 'MinDtForCallBck', ISODate, False)

	@property
	def NbOfDaysLndgBrrwg(self):
		return self._NbOfDaysLndgBrrwg

	@NbOfDaysLndgBrrwg.setter
	def NbOfDaysLndgBrrwg(self, value):
		self._NbOfDaysLndgBrrwg = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysLndgBrrwg', Number24Choice, False)

	@NbOfDaysLndgBrrwg.deleter
	def NbOfDaysLndgBrrwg(self):
		del self._NbOfDaysLndgBrrwg
		self._NbOfDaysLndgBrrwg = base_types.UninitialisedField(self, 'NbOfDaysLndgBrrwg', Number24Choice, False)

	@property
	def PrdcPmt(self):
		return self._PrdcPmt

	@PrdcPmt.setter
	def PrdcPmt(self, value):
		self._PrdcPmt = value if value is not None else base_types.UninitialisedField(self, 'PrdcPmt', YesNoIndicator, False)

	@PrdcPmt.deleter
	def PrdcPmt(self):
		del self._PrdcPmt
		self._PrdcPmt = base_types.UninitialisedField(self, 'PrdcPmt', YesNoIndicator, False)

	@property
	def PricgRate(self):
		return self._PricgRate

	@PricgRate.setter
	def PricgRate(self, value):
		self._PricgRate = value if value is not None else base_types.UninitialisedField(self, 'PricgRate', RateOrName1Choice, False)

	@PricgRate.deleter
	def PricgRate(self):
		del self._PricgRate
		self._PricgRate = base_types.UninitialisedField(self, 'PricgRate', RateOrName1Choice, False)

	@property
	def PrmAmt(self):
		return self._PrmAmt

	@PrmAmt.setter
	def PrmAmt(self, value):
		self._PrmAmt = value if value is not None else base_types.UninitialisedField(self, 'PrmAmt', AmountAndDirection5, False)

	@PrmAmt.deleter
	def PrmAmt(self):
		del self._PrmAmt
		self._PrmAmt = base_types.UninitialisedField(self, 'PrmAmt', AmountAndDirection5, False)

	@property
	def RateChngDt(self):
		return self._RateChngDt

	@RateChngDt.setter
	def RateChngDt(self, value):
		self._RateChngDt = value if value is not None else base_types.UninitialisedField(self, 'RateChngDt', ISODateTime, False)

	@RateChngDt.deleter
	def RateChngDt(self):
		del self._RateChngDt
		self._RateChngDt = base_types.UninitialisedField(self, 'RateChngDt', ISODateTime, False)

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if value is not None else base_types.UninitialisedField(self, 'RateTp', RateType35Choice, False)

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = base_types.UninitialisedField(self, 'RateTp', RateType35Choice, False)

	@property
	def RollOver(self):
		return self._RollOver

	@RollOver.setter
	def RollOver(self, value):
		self._RollOver = value if value is not None else base_types.UninitialisedField(self, 'RollOver', YesNoIndicator, False)

	@RollOver.deleter
	def RollOver(self):
		del self._RollOver
		self._RollOver = base_types.UninitialisedField(self, 'RollOver', YesNoIndicator, False)

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
		self._Rvaltn = value if value is not None else base_types.UninitialisedField(self, 'Rvaltn', Revaluation3Choice, False)

	@Rvaltn.deleter
	def Rvaltn(self):
		del self._Rvaltn
		self._Rvaltn = base_types.UninitialisedField(self, 'Rvaltn', Revaluation3Choice, False)

	@property
	def Rvsbl(self):
		return self._Rvsbl

	@Rvsbl.setter
	def Rvsbl(self, value):
		self._Rvsbl = value if value is not None else base_types.UninitialisedField(self, 'Rvsbl', Reversible2Choice, False)

	@Rvsbl.deleter
	def Rvsbl(self):
		del self._Rvsbl
		self._Rvsbl = base_types.UninitialisedField(self, 'Rvsbl', Reversible2Choice, False)

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
	def SctiesLndgTp(self):
		return self._SctiesLndgTp

	@SctiesLndgTp.setter
	def SctiesLndgTp(self, value):
		self._SctiesLndgTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesLndgTp', SecuritiesLendingType2Choice, False)

	@SctiesLndgTp.deleter
	def SctiesLndgTp(self):
		del self._SctiesLndgTp
		self._SctiesLndgTp = base_types.UninitialisedField(self, 'SctiesLndgTp', SecuritiesLendingType2Choice, False)

	@property
	def SprdRate(self):
		return self._SprdRate

	@SprdRate.setter
	def SprdRate(self, value):
		self._SprdRate = value if value is not None else base_types.UninitialisedField(self, 'SprdRate', SpreadRate1, False)

	@SprdRate.deleter
	def SprdRate(self):
		del self._SprdRate
		self._SprdRate = base_types.UninitialisedField(self, 'SprdRate', SpreadRate1, False)

	@property
	def StdCollAmt(self):
		return self._StdCollAmt

	@StdCollAmt.setter
	def StdCollAmt(self, value):
		self._StdCollAmt = value if value is not None else base_types.UninitialisedField(self, 'StdCollAmt', AmountAndDirection5, False)

	@StdCollAmt.deleter
	def StdCollAmt(self):
		del self._StdCollAmt
		self._StdCollAmt = base_types.UninitialisedField(self, 'StdCollAmt', AmountAndDirection5, False)

	@property
	def StdCollRatio(self):
		return self._StdCollRatio

	@StdCollRatio.setter
	def StdCollRatio(self, value):
		self._StdCollRatio = value if value is not None else base_types.UninitialisedField(self, 'StdCollRatio', Rate2, False)

	@StdCollRatio.deleter
	def StdCollRatio(self):
		del self._StdCollRatio
		self._StdCollRatio = base_types.UninitialisedField(self, 'StdCollRatio', Rate2, False)

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
	def TtlNbOfCollInstrs(self):
		return self._TtlNbOfCollInstrs

	@TtlNbOfCollInstrs.setter
	def TtlNbOfCollInstrs(self, value):
		self._TtlNbOfCollInstrs = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfCollInstrs', Max3NumericText, False)

	@TtlNbOfCollInstrs.deleter
	def TtlNbOfCollInstrs(self):
		del self._TtlNbOfCollInstrs
		self._TtlNbOfCollInstrs = base_types.UninitialisedField(self, 'TtlNbOfCollInstrs', Max3NumericText, False)

	@property
	def TxCallDely(self):
		return self._TxCallDely

	@TxCallDely.setter
	def TxCallDely(self, value):
		self._TxCallDely = value if value is not None else base_types.UninitialisedField(self, 'TxCallDely', Max3NumericText, False)

	@TxCallDely.deleter
	def TxCallDely(self):
		del self._TxCallDely
		self._TxCallDely = base_types.UninitialisedField(self, 'TxCallDely', Max3NumericText, False)

	@property
	def VarblRateSpprt(self):
		return self._VarblRateSpprt

	@VarblRateSpprt.setter
	def VarblRateSpprt(self, value):
		self._VarblRateSpprt = value if value is not None else base_types.UninitialisedField(self, 'VarblRateSpprt', RateName1, False)

	@VarblRateSpprt.deleter
	def VarblRateSpprt(self):
		del self._VarblRateSpprt
		self._VarblRateSpprt = base_types.UninitialisedField(self, 'VarblRateSpprt', RateName1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstTax', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwgRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwgRsn', type=BorrowingReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllblTradInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgAmtPerPcsOfColl', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTp', type=CollateralType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTermsModChngd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddRatio', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndNbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExCpn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgAgrmt', type=Agreement5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrftAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstCmptnMtd', type=InterestComputationMethod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglFrmwk', type=LegalFramework1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LndgTxMtd', type=LendingTransactionMethod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LndgWthColl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinDtForCallBck', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysLndgBrrwg', type=Number24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdcPmt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgRate', type=RateOrName1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateChngDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RollOver', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvaltn', type=Revaluation3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvsbl', type=Reversible2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesHrcut', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesLndgTp', type=SecuritiesLendingType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SprdRate', type=SpreadRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdCollAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdCollRatio', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockLnMrgn', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfCollInstrs', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCallDely', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateSpprt', type=RateName1, min=0, max=1, mutex_group=None, array=False),
	))