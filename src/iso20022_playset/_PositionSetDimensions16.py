from . import base_types
from .AssetClassCommodity6Choice import AssetClassCommodity6Choice
from .ProductType4Code import ProductType4Code
from .OtherPayment6 import OtherPayment6
from .SecurityIdentification41Choice import SecurityIdentification41Choice
from .FinancialInstrumentContractType2Code import FinancialInstrumentContractType2Code
from .TrueFalseIndicator import TrueFalseIndicator
from .Max52Text import Max52Text
from .OptionType2Code import OptionType2Code
from .TradeCounterpartyReport20 import TradeCounterpartyReport20
from .MarginCollateralReport4 import MarginCollateralReport4
from .ExchangeRateBasis1Choice import ExchangeRateBasis1Choice
from .TimeToMaturity1Choice import TimeToMaturity1Choice
from .MasterAgreement8 import MasterAgreement8
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .CreditDerivative7 import CreditDerivative7

class PositionSetDimensions16(base_types._BaseFieldType):

	__slots__ = ["_SttlmCcyScndLeg", "_Clrd", "_SttlmCcy", "_XchgRateBsis", "_Cdt", "_Cmmdty", "_IRSTp", "_UndrlygInstrm", "_IntraGrp", "_NtnlCcy", "_ValCcy", "_OthrPmt", "_Coll", "_CtrctTp", "_MstrAgrmt", "_TmToMtrty", "_CtrPtyId", "_OptnTp", "_NtnlCcyScndLeg", "_AsstClss"]
	@property
	def SttlmCcyScndLeg(self):
		return self._SttlmCcyScndLeg

	@SttlmCcyScndLeg.setter
	def SttlmCcyScndLeg(self, value):
		self._SttlmCcyScndLeg = value if type(value) != base_types.auto else self.make_default("SttlmCcyScndLeg")

	@SttlmCcyScndLeg.deleter
	def SttlmCcyScndLeg(self):
		del self._SttlmCcyScndLeg
		self._SttlmCcyScndLeg = None

	@property
	def Clrd(self):
		return self._Clrd

	@Clrd.setter
	def Clrd(self, value):
		self._Clrd = value if type(value) != base_types.auto else self.make_default("Clrd")

	@Clrd.deleter
	def Clrd(self):
		del self._Clrd
		self._Clrd = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != base_types.auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def XchgRateBsis(self):
		return self._XchgRateBsis

	@XchgRateBsis.setter
	def XchgRateBsis(self, value):
		self._XchgRateBsis = value if type(value) != base_types.auto else self.make_default("XchgRateBsis")

	@XchgRateBsis.deleter
	def XchgRateBsis(self):
		del self._XchgRateBsis
		self._XchgRateBsis = None

	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if type(value) != base_types.auto else self.make_default("Cdt")

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = None

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if type(value) != base_types.auto else self.make_default("Cmmdty")

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = None

	@property
	def IRSTp(self):
		return self._IRSTp

	@IRSTp.setter
	def IRSTp(self, value):
		self._IRSTp = value if type(value) != base_types.auto else self.make_default("IRSTp")

	@IRSTp.deleter
	def IRSTp(self):
		del self._IRSTp
		self._IRSTp = None

	@property
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if type(value) != base_types.auto else self.make_default("UndrlygInstrm")

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = None

	@property
	def IntraGrp(self):
		return self._IntraGrp

	@IntraGrp.setter
	def IntraGrp(self, value):
		self._IntraGrp = value if type(value) != base_types.auto else self.make_default("IntraGrp")

	@IntraGrp.deleter
	def IntraGrp(self):
		del self._IntraGrp
		self._IntraGrp = None

	@property
	def NtnlCcy(self):
		return self._NtnlCcy

	@NtnlCcy.setter
	def NtnlCcy(self, value):
		self._NtnlCcy = value if type(value) != base_types.auto else self.make_default("NtnlCcy")

	@NtnlCcy.deleter
	def NtnlCcy(self):
		del self._NtnlCcy
		self._NtnlCcy = None

	@property
	def ValCcy(self):
		return self._ValCcy

	@ValCcy.setter
	def ValCcy(self, value):
		self._ValCcy = value if type(value) != base_types.auto else self.make_default("ValCcy")

	@ValCcy.deleter
	def ValCcy(self):
		del self._ValCcy
		self._ValCcy = None

	@property
	def OthrPmt(self):
		return self._OthrPmt

	@OthrPmt.setter
	def OthrPmt(self, value):
		self._OthrPmt = value if type(value) != base_types.auto else self.make_default("OthrPmt")

	@OthrPmt.deleter
	def OthrPmt(self):
		del self._OthrPmt
		self._OthrPmt = None

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if type(value) != base_types.auto else self.make_default("Coll")

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = None

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if type(value) != base_types.auto else self.make_default("CtrctTp")

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = None

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if type(value) != base_types.auto else self.make_default("MstrAgrmt")

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = None

	@property
	def TmToMtrty(self):
		return self._TmToMtrty

	@TmToMtrty.setter
	def TmToMtrty(self, value):
		self._TmToMtrty = value if type(value) != base_types.auto else self.make_default("TmToMtrty")

	@TmToMtrty.deleter
	def TmToMtrty(self):
		del self._TmToMtrty
		self._TmToMtrty = None

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != base_types.auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def NtnlCcyScndLeg(self):
		return self._NtnlCcyScndLeg

	@NtnlCcyScndLeg.setter
	def NtnlCcyScndLeg(self, value):
		self._NtnlCcyScndLeg = value if type(value) != base_types.auto else self.make_default("NtnlCcyScndLeg")

	@NtnlCcyScndLeg.deleter
	def NtnlCcyScndLeg(self):
		del self._NtnlCcyScndLeg
		self._NtnlCcyScndLeg = None

	@property
	def AsstClss(self):
		return self._AsstClss

	@AsstClss.setter
	def AsstClss(self, value):
		self._AsstClss = value if type(value) != base_types.auto else self.make_default("AsstClss")

	@AsstClss.deleter
	def AsstClss(self):
		del self._AsstClss
		self._AsstClss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmCcyScndLeg', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateBsis', type=ExchangeRateBasis1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdt', type=CreditDerivative7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmmdty', type=AssetClassCommodity6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IRSTp', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrm', type=SecurityIdentification41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraGrp', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmt', type=OtherPayment6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=MarginCollateralReport4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=FinancialInstrumentContractType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmToMtrty', type=TimeToMaturity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=TradeCounterpartyReport20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcyScndLeg', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstClss', type=ProductType4Code, min=0, max=1, mutex_group=None, array=False),
	))

