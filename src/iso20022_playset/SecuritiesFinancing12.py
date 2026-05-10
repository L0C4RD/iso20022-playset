from . import base_types
from .Number24Choice import Number24Choice
from .InterestComputationMethod3Choice import InterestComputationMethod3Choice
from .Reversible2Choice import Reversible2Choice
from .BaseOneRate import BaseOneRate
from .RateOrName1Choice import RateOrName1Choice
from .Agreement5 import Agreement5
from .RateName1 import RateName1
from .SecuritiesLendingType2Choice import SecuritiesLendingType2Choice
from .LegalFramework1Code import LegalFramework1Code
from .ISODate import ISODate
from .Rate2 import Rate2
from .LendingTransactionMethod2Choice import LendingTransactionMethod2Choice
from .Revaluation3Choice import Revaluation3Choice
from .ISODateTime import ISODateTime
from .Max3NumericText import Max3NumericText
from .RateType35Choice import RateType35Choice
from .AmountAndDirection5 import AmountAndDirection5
from .PercentageRate import PercentageRate
from .Max3Number import Max3Number
from .BorrowingReason2Choice import BorrowingReason2Choice
from .SpreadRate1 import SpreadRate1
from .YesNoIndicator import YesNoIndicator
from .CollateralType4Choice import CollateralType4Choice

class SecuritiesFinancing12(base_types._BaseFieldType):

	__slots__ = ["_MinDtForCallBck", "_PrdcPmt", "_LndgTxMtd", "_TtlNbOfCollInstrs", "_EndNbOfDaysAcrd", "_FrftAmt", "_Rvsbl", "_Rvaltn", "_AcrdIntrstAmt", "_SctiesLndgTp", "_StdCollAmt", "_ExCpn", "_RateTp", "_ClsgAmtPerPcsOfColl", "_IntrstRate", "_EndFctr", "_SctiesHrcut", "_CllblTradInd", "_CollTp", "_AcrdIntrstPctg", "_PricgRate", "_FincgAgrmt", "_PrmAmt", "_DvddRatio", "_VarblRateSpprt", "_RateChngDt", "_NbOfDaysLndgBrrwg", "_IntrstCmptnMtd", "_TxCallDely", "_AcrdIntrstTax", "_LglFrmwk", "_CtrctTermsModChngd", "_SprdRate", "_LndgWthColl", "_StockLnMrgn", "_BrrwgRate", "_StdCollRatio", "_RollOver", "_RpRate", "_BrrwgRsn"]
	@property
	def MinDtForCallBck(self):
		return self._MinDtForCallBck

	@MinDtForCallBck.setter
	def MinDtForCallBck(self, value):
		self._MinDtForCallBck = value if type(value) != base_types.auto else self.make_default("MinDtForCallBck")

	@MinDtForCallBck.deleter
	def MinDtForCallBck(self):
		del self._MinDtForCallBck
		self._MinDtForCallBck = None

	@property
	def PrdcPmt(self):
		return self._PrdcPmt

	@PrdcPmt.setter
	def PrdcPmt(self, value):
		self._PrdcPmt = value if type(value) != base_types.auto else self.make_default("PrdcPmt")

	@PrdcPmt.deleter
	def PrdcPmt(self):
		del self._PrdcPmt
		self._PrdcPmt = None

	@property
	def LndgTxMtd(self):
		return self._LndgTxMtd

	@LndgTxMtd.setter
	def LndgTxMtd(self, value):
		self._LndgTxMtd = value if type(value) != base_types.auto else self.make_default("LndgTxMtd")

	@LndgTxMtd.deleter
	def LndgTxMtd(self):
		del self._LndgTxMtd
		self._LndgTxMtd = None

	@property
	def TtlNbOfCollInstrs(self):
		return self._TtlNbOfCollInstrs

	@TtlNbOfCollInstrs.setter
	def TtlNbOfCollInstrs(self, value):
		self._TtlNbOfCollInstrs = value if type(value) != base_types.auto else self.make_default("TtlNbOfCollInstrs")

	@TtlNbOfCollInstrs.deleter
	def TtlNbOfCollInstrs(self):
		del self._TtlNbOfCollInstrs
		self._TtlNbOfCollInstrs = None

	@property
	def EndNbOfDaysAcrd(self):
		return self._EndNbOfDaysAcrd

	@EndNbOfDaysAcrd.setter
	def EndNbOfDaysAcrd(self, value):
		self._EndNbOfDaysAcrd = value if type(value) != base_types.auto else self.make_default("EndNbOfDaysAcrd")

	@EndNbOfDaysAcrd.deleter
	def EndNbOfDaysAcrd(self):
		del self._EndNbOfDaysAcrd
		self._EndNbOfDaysAcrd = None

	@property
	def FrftAmt(self):
		return self._FrftAmt

	@FrftAmt.setter
	def FrftAmt(self, value):
		self._FrftAmt = value if type(value) != base_types.auto else self.make_default("FrftAmt")

	@FrftAmt.deleter
	def FrftAmt(self):
		del self._FrftAmt
		self._FrftAmt = None

	@property
	def Rvsbl(self):
		return self._Rvsbl

	@Rvsbl.setter
	def Rvsbl(self, value):
		self._Rvsbl = value if type(value) != base_types.auto else self.make_default("Rvsbl")

	@Rvsbl.deleter
	def Rvsbl(self):
		del self._Rvsbl
		self._Rvsbl = None

	@property
	def Rvaltn(self):
		return self._Rvaltn

	@Rvaltn.setter
	def Rvaltn(self, value):
		self._Rvaltn = value if type(value) != base_types.auto else self.make_default("Rvaltn")

	@Rvaltn.deleter
	def Rvaltn(self):
		del self._Rvaltn
		self._Rvaltn = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != base_types.auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def SctiesLndgTp(self):
		return self._SctiesLndgTp

	@SctiesLndgTp.setter
	def SctiesLndgTp(self, value):
		self._SctiesLndgTp = value if type(value) != base_types.auto else self.make_default("SctiesLndgTp")

	@SctiesLndgTp.deleter
	def SctiesLndgTp(self):
		del self._SctiesLndgTp
		self._SctiesLndgTp = None

	@property
	def StdCollAmt(self):
		return self._StdCollAmt

	@StdCollAmt.setter
	def StdCollAmt(self, value):
		self._StdCollAmt = value if type(value) != base_types.auto else self.make_default("StdCollAmt")

	@StdCollAmt.deleter
	def StdCollAmt(self):
		del self._StdCollAmt
		self._StdCollAmt = None

	@property
	def ExCpn(self):
		return self._ExCpn

	@ExCpn.setter
	def ExCpn(self, value):
		self._ExCpn = value if type(value) != base_types.auto else self.make_default("ExCpn")

	@ExCpn.deleter
	def ExCpn(self):
		del self._ExCpn
		self._ExCpn = None

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != base_types.auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	@property
	def ClsgAmtPerPcsOfColl(self):
		return self._ClsgAmtPerPcsOfColl

	@ClsgAmtPerPcsOfColl.setter
	def ClsgAmtPerPcsOfColl(self, value):
		self._ClsgAmtPerPcsOfColl = value if type(value) != base_types.auto else self.make_default("ClsgAmtPerPcsOfColl")

	@ClsgAmtPerPcsOfColl.deleter
	def ClsgAmtPerPcsOfColl(self):
		del self._ClsgAmtPerPcsOfColl
		self._ClsgAmtPerPcsOfColl = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def EndFctr(self):
		return self._EndFctr

	@EndFctr.setter
	def EndFctr(self, value):
		self._EndFctr = value if type(value) != base_types.auto else self.make_default("EndFctr")

	@EndFctr.deleter
	def EndFctr(self):
		del self._EndFctr
		self._EndFctr = None

	@property
	def SctiesHrcut(self):
		return self._SctiesHrcut

	@SctiesHrcut.setter
	def SctiesHrcut(self, value):
		self._SctiesHrcut = value if type(value) != base_types.auto else self.make_default("SctiesHrcut")

	@SctiesHrcut.deleter
	def SctiesHrcut(self):
		del self._SctiesHrcut
		self._SctiesHrcut = None

	@property
	def CllblTradInd(self):
		return self._CllblTradInd

	@CllblTradInd.setter
	def CllblTradInd(self, value):
		self._CllblTradInd = value if type(value) != base_types.auto else self.make_default("CllblTradInd")

	@CllblTradInd.deleter
	def CllblTradInd(self):
		del self._CllblTradInd
		self._CllblTradInd = None

	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if type(value) != base_types.auto else self.make_default("CollTp")

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = None

	@property
	def AcrdIntrstPctg(self):
		return self._AcrdIntrstPctg

	@AcrdIntrstPctg.setter
	def AcrdIntrstPctg(self, value):
		self._AcrdIntrstPctg = value if type(value) != base_types.auto else self.make_default("AcrdIntrstPctg")

	@AcrdIntrstPctg.deleter
	def AcrdIntrstPctg(self):
		del self._AcrdIntrstPctg
		self._AcrdIntrstPctg = None

	@property
	def PricgRate(self):
		return self._PricgRate

	@PricgRate.setter
	def PricgRate(self, value):
		self._PricgRate = value if type(value) != base_types.auto else self.make_default("PricgRate")

	@PricgRate.deleter
	def PricgRate(self):
		del self._PricgRate
		self._PricgRate = None

	@property
	def FincgAgrmt(self):
		return self._FincgAgrmt

	@FincgAgrmt.setter
	def FincgAgrmt(self, value):
		self._FincgAgrmt = value if type(value) != base_types.auto else self.make_default("FincgAgrmt")

	@FincgAgrmt.deleter
	def FincgAgrmt(self):
		del self._FincgAgrmt
		self._FincgAgrmt = None

	@property
	def PrmAmt(self):
		return self._PrmAmt

	@PrmAmt.setter
	def PrmAmt(self, value):
		self._PrmAmt = value if type(value) != base_types.auto else self.make_default("PrmAmt")

	@PrmAmt.deleter
	def PrmAmt(self):
		del self._PrmAmt
		self._PrmAmt = None

	@property
	def DvddRatio(self):
		return self._DvddRatio

	@DvddRatio.setter
	def DvddRatio(self, value):
		self._DvddRatio = value if type(value) != base_types.auto else self.make_default("DvddRatio")

	@DvddRatio.deleter
	def DvddRatio(self):
		del self._DvddRatio
		self._DvddRatio = None

	@property
	def VarblRateSpprt(self):
		return self._VarblRateSpprt

	@VarblRateSpprt.setter
	def VarblRateSpprt(self, value):
		self._VarblRateSpprt = value if type(value) != base_types.auto else self.make_default("VarblRateSpprt")

	@VarblRateSpprt.deleter
	def VarblRateSpprt(self):
		del self._VarblRateSpprt
		self._VarblRateSpprt = None

	@property
	def RateChngDt(self):
		return self._RateChngDt

	@RateChngDt.setter
	def RateChngDt(self, value):
		self._RateChngDt = value if type(value) != base_types.auto else self.make_default("RateChngDt")

	@RateChngDt.deleter
	def RateChngDt(self):
		del self._RateChngDt
		self._RateChngDt = None

	@property
	def NbOfDaysLndgBrrwg(self):
		return self._NbOfDaysLndgBrrwg

	@NbOfDaysLndgBrrwg.setter
	def NbOfDaysLndgBrrwg(self, value):
		self._NbOfDaysLndgBrrwg = value if type(value) != base_types.auto else self.make_default("NbOfDaysLndgBrrwg")

	@NbOfDaysLndgBrrwg.deleter
	def NbOfDaysLndgBrrwg(self):
		del self._NbOfDaysLndgBrrwg
		self._NbOfDaysLndgBrrwg = None

	@property
	def IntrstCmptnMtd(self):
		return self._IntrstCmptnMtd

	@IntrstCmptnMtd.setter
	def IntrstCmptnMtd(self, value):
		self._IntrstCmptnMtd = value if type(value) != base_types.auto else self.make_default("IntrstCmptnMtd")

	@IntrstCmptnMtd.deleter
	def IntrstCmptnMtd(self):
		del self._IntrstCmptnMtd
		self._IntrstCmptnMtd = None

	@property
	def TxCallDely(self):
		return self._TxCallDely

	@TxCallDely.setter
	def TxCallDely(self, value):
		self._TxCallDely = value if type(value) != base_types.auto else self.make_default("TxCallDely")

	@TxCallDely.deleter
	def TxCallDely(self):
		del self._TxCallDely
		self._TxCallDely = None

	@property
	def AcrdIntrstTax(self):
		return self._AcrdIntrstTax

	@AcrdIntrstTax.setter
	def AcrdIntrstTax(self, value):
		self._AcrdIntrstTax = value if type(value) != base_types.auto else self.make_default("AcrdIntrstTax")

	@AcrdIntrstTax.deleter
	def AcrdIntrstTax(self):
		del self._AcrdIntrstTax
		self._AcrdIntrstTax = None

	@property
	def LglFrmwk(self):
		return self._LglFrmwk

	@LglFrmwk.setter
	def LglFrmwk(self, value):
		self._LglFrmwk = value if type(value) != base_types.auto else self.make_default("LglFrmwk")

	@LglFrmwk.deleter
	def LglFrmwk(self):
		del self._LglFrmwk
		self._LglFrmwk = None

	@property
	def CtrctTermsModChngd(self):
		return self._CtrctTermsModChngd

	@CtrctTermsModChngd.setter
	def CtrctTermsModChngd(self, value):
		self._CtrctTermsModChngd = value if type(value) != base_types.auto else self.make_default("CtrctTermsModChngd")

	@CtrctTermsModChngd.deleter
	def CtrctTermsModChngd(self):
		del self._CtrctTermsModChngd
		self._CtrctTermsModChngd = None

	@property
	def SprdRate(self):
		return self._SprdRate

	@SprdRate.setter
	def SprdRate(self, value):
		self._SprdRate = value if type(value) != base_types.auto else self.make_default("SprdRate")

	@SprdRate.deleter
	def SprdRate(self):
		del self._SprdRate
		self._SprdRate = None

	@property
	def LndgWthColl(self):
		return self._LndgWthColl

	@LndgWthColl.setter
	def LndgWthColl(self, value):
		self._LndgWthColl = value if type(value) != base_types.auto else self.make_default("LndgWthColl")

	@LndgWthColl.deleter
	def LndgWthColl(self):
		del self._LndgWthColl
		self._LndgWthColl = None

	@property
	def StockLnMrgn(self):
		return self._StockLnMrgn

	@StockLnMrgn.setter
	def StockLnMrgn(self, value):
		self._StockLnMrgn = value if type(value) != base_types.auto else self.make_default("StockLnMrgn")

	@StockLnMrgn.deleter
	def StockLnMrgn(self):
		del self._StockLnMrgn
		self._StockLnMrgn = None

	@property
	def BrrwgRate(self):
		return self._BrrwgRate

	@BrrwgRate.setter
	def BrrwgRate(self, value):
		self._BrrwgRate = value if type(value) != base_types.auto else self.make_default("BrrwgRate")

	@BrrwgRate.deleter
	def BrrwgRate(self):
		del self._BrrwgRate
		self._BrrwgRate = None

	@property
	def StdCollRatio(self):
		return self._StdCollRatio

	@StdCollRatio.setter
	def StdCollRatio(self, value):
		self._StdCollRatio = value if type(value) != base_types.auto else self.make_default("StdCollRatio")

	@StdCollRatio.deleter
	def StdCollRatio(self):
		del self._StdCollRatio
		self._StdCollRatio = None

	@property
	def RollOver(self):
		return self._RollOver

	@RollOver.setter
	def RollOver(self, value):
		self._RollOver = value if type(value) != base_types.auto else self.make_default("RollOver")

	@RollOver.deleter
	def RollOver(self):
		del self._RollOver
		self._RollOver = None

	@property
	def RpRate(self):
		return self._RpRate

	@RpRate.setter
	def RpRate(self, value):
		self._RpRate = value if type(value) != base_types.auto else self.make_default("RpRate")

	@RpRate.deleter
	def RpRate(self):
		del self._RpRate
		self._RpRate = None

	@property
	def BrrwgRsn(self):
		return self._BrrwgRsn

	@BrrwgRsn.setter
	def BrrwgRsn(self, value):
		self._BrrwgRsn = value if type(value) != base_types.auto else self.make_default("BrrwgRsn")

	@BrrwgRsn.deleter
	def BrrwgRsn(self):
		del self._BrrwgRsn
		self._BrrwgRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MinDtForCallBck', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdcPmt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LndgTxMtd', type=LendingTransactionMethod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfCollInstrs', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndNbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrftAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvsbl', type=Reversible2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvaltn', type=Revaluation3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesLndgTp', type=SecuritiesLendingType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdCollAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExCpn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgAmtPerPcsOfColl', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesHrcut', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllblTradInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTp', type=CollateralType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgRate', type=RateOrName1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgAgrmt', type=Agreement5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddRatio', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateSpprt', type=RateName1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateChngDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysLndgBrrwg', type=Number24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstCmptnMtd', type=InterestComputationMethod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCallDely', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstTax', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglFrmwk', type=LegalFramework1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTermsModChngd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SprdRate', type=SpreadRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LndgWthColl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockLnMrgn', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwgRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdCollRatio', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RollOver', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwgRsn', type=BorrowingReason2Choice, min=0, max=1, mutex_group=None, array=False),
	))

