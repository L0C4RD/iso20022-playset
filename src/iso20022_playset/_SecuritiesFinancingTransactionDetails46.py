from . import base_types
from ._AmountAndDirection59 import AmountAndDirection59
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._Exact3NumericText import Exact3NumericText
from ._InterestComputationMethodFormat5Choice import InterestComputationMethodFormat5Choice
from ._LegalFramework4Choice import LegalFramework4Choice
from ._Rate2 import Rate2
from ._RateName2 import RateName2
from ._RateOrName2Choice import RateOrName2Choice
from ._RateType67Choice import RateType67Choice
from ._RestrictedFINXMax140Text import RestrictedFINXMax140Text
from ._RestrictedFINXMax16Text import RestrictedFINXMax16Text
from ._RestrictedFINXMax52Text import RestrictedFINXMax52Text
from ._RevaluationIndicator4Choice import RevaluationIndicator4Choice
from ._TerminationDate7Choice import TerminationDate7Choice
from ._YesNoIndicator import YesNoIndicator

class SecuritiesFinancingTransactionDetails46(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_ChrgsRate", "_ClsgLegId", "_ComssnClctnDt", "_DealAmt", "_EarlstCallBckDt", "_FrftAmt", "_IntrstCmptnMtd", "_IntrstPmt", "_LglFrmwk", "_MtrtyDtMod", "_PricgRate", "_PrmAmt", "_RateChngDt", "_RateTp", "_RpRate", "_Rvaltn", "_ScndLegNrrtv", "_SctiesFincgTradId", "_SctiesHrcut", "_Sprd", "_StockLnMrgn", "_TermntnAmtPerPcOfColl", "_TermntnDt", "_TermntnTxAmt", "_TtlNbOfCollInstrs", "_TxCallDely", "_VarblRateSpprt"]
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
	def ChrgsRate(self):
		return self._ChrgsRate

	@ChrgsRate.setter
	def ChrgsRate(self, value):
		self._ChrgsRate = value if type(value) != base_types.auto else self.make_default("ChrgsRate")

	@ChrgsRate.deleter
	def ChrgsRate(self):
		del self._ChrgsRate
		self._ChrgsRate = None

	@property
	def ClsgLegId(self):
		return self._ClsgLegId

	@ClsgLegId.setter
	def ClsgLegId(self, value):
		self._ClsgLegId = value if type(value) != base_types.auto else self.make_default("ClsgLegId")

	@ClsgLegId.deleter
	def ClsgLegId(self):
		del self._ClsgLegId
		self._ClsgLegId = None

	@property
	def ComssnClctnDt(self):
		return self._ComssnClctnDt

	@ComssnClctnDt.setter
	def ComssnClctnDt(self, value):
		self._ComssnClctnDt = value if type(value) != base_types.auto else self.make_default("ComssnClctnDt")

	@ComssnClctnDt.deleter
	def ComssnClctnDt(self):
		del self._ComssnClctnDt
		self._ComssnClctnDt = None

	@property
	def DealAmt(self):
		return self._DealAmt

	@DealAmt.setter
	def DealAmt(self, value):
		self._DealAmt = value if type(value) != base_types.auto else self.make_default("DealAmt")

	@DealAmt.deleter
	def DealAmt(self):
		del self._DealAmt
		self._DealAmt = None

	@property
	def EarlstCallBckDt(self):
		return self._EarlstCallBckDt

	@EarlstCallBckDt.setter
	def EarlstCallBckDt(self, value):
		self._EarlstCallBckDt = value if type(value) != base_types.auto else self.make_default("EarlstCallBckDt")

	@EarlstCallBckDt.deleter
	def EarlstCallBckDt(self):
		del self._EarlstCallBckDt
		self._EarlstCallBckDt = None

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
	def IntrstPmt(self):
		return self._IntrstPmt

	@IntrstPmt.setter
	def IntrstPmt(self, value):
		self._IntrstPmt = value if type(value) != base_types.auto else self.make_default("IntrstPmt")

	@IntrstPmt.deleter
	def IntrstPmt(self):
		del self._IntrstPmt
		self._IntrstPmt = None

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
	def MtrtyDtMod(self):
		return self._MtrtyDtMod

	@MtrtyDtMod.setter
	def MtrtyDtMod(self, value):
		self._MtrtyDtMod = value if type(value) != base_types.auto else self.make_default("MtrtyDtMod")

	@MtrtyDtMod.deleter
	def MtrtyDtMod(self):
		del self._MtrtyDtMod
		self._MtrtyDtMod = None

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
	def ScndLegNrrtv(self):
		return self._ScndLegNrrtv

	@ScndLegNrrtv.setter
	def ScndLegNrrtv(self, value):
		self._ScndLegNrrtv = value if type(value) != base_types.auto else self.make_default("ScndLegNrrtv")

	@ScndLegNrrtv.deleter
	def ScndLegNrrtv(self):
		del self._ScndLegNrrtv
		self._ScndLegNrrtv = None

	@property
	def SctiesFincgTradId(self):
		return self._SctiesFincgTradId

	@SctiesFincgTradId.setter
	def SctiesFincgTradId(self, value):
		self._SctiesFincgTradId = value if type(value) != base_types.auto else self.make_default("SctiesFincgTradId")

	@SctiesFincgTradId.deleter
	def SctiesFincgTradId(self):
		del self._SctiesFincgTradId
		self._SctiesFincgTradId = None

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
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != base_types.auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

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
	def TermntnAmtPerPcOfColl(self):
		return self._TermntnAmtPerPcOfColl

	@TermntnAmtPerPcOfColl.setter
	def TermntnAmtPerPcOfColl(self, value):
		self._TermntnAmtPerPcOfColl = value if type(value) != base_types.auto else self.make_default("TermntnAmtPerPcOfColl")

	@TermntnAmtPerPcOfColl.deleter
	def TermntnAmtPerPcOfColl(self):
		del self._TermntnAmtPerPcOfColl
		self._TermntnAmtPerPcOfColl = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != base_types.auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	@property
	def TermntnTxAmt(self):
		return self._TermntnTxAmt

	@TermntnTxAmt.setter
	def TermntnTxAmt(self, value):
		self._TermntnTxAmt = value if type(value) != base_types.auto else self.make_default("TermntnTxAmt")

	@TermntnTxAmt.deleter
	def TermntnTxAmt(self):
		del self._TermntnTxAmt
		self._TermntnTxAmt = None

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
	def VarblRateSpprt(self):
		return self._VarblRateSpprt

	@VarblRateSpprt.setter
	def VarblRateSpprt(self, value):
		self._VarblRateSpprt = value if type(value) != base_types.auto else self.make_default("VarblRateSpprt")

	@VarblRateSpprt.deleter
	def VarblRateSpprt(self):
		del self._VarblRateSpprt
		self._VarblRateSpprt = None

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

