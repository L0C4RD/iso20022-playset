from . import base_types
from ._BasketIdentificationAndEligibilitySetProfile1 import BasketIdentificationAndEligibilitySetProfile1
from ._GenericIdentification30 import GenericIdentification30
from ._CollateralTransactionType1Choice import CollateralTransactionType1Choice
from ._RateOrType1Choice import RateOrType1Choice
from ._ResponseStatus9Choice import ResponseStatus9Choice
from ._ExposureType23Choice import ExposureType23Choice
from ._CollateralRole1Code import CollateralRole1Code
from ._YesNoIndicator import YesNoIndicator
from ._AdditionalInformation24 import AdditionalInformation24

class CollateralParameters10(base_types._BaseFieldType):

	__slots__ = ["_RspnSts", "_TrfTitl", "_AutomtcAllcn", "_ValSghtMrgnRate", "_XpsrTp", "_BsktIdAndElgbltySetPrfl", "_Prty", "_AddtlInf", "_CollInstrTp", "_CollSd", "_SttlmPrc", "_FaildSttlmSlvtn", "_MainTradgAcctCollstn"]
	@property
	def RspnSts(self):
		return self._RspnSts

	@RspnSts.setter
	def RspnSts(self, value):
		self._RspnSts = value if type(value) != base_types.auto else self.make_default("RspnSts")

	@RspnSts.deleter
	def RspnSts(self):
		del self._RspnSts
		self._RspnSts = None

	@property
	def TrfTitl(self):
		return self._TrfTitl

	@TrfTitl.setter
	def TrfTitl(self, value):
		self._TrfTitl = value if type(value) != base_types.auto else self.make_default("TrfTitl")

	@TrfTitl.deleter
	def TrfTitl(self):
		del self._TrfTitl
		self._TrfTitl = None

	@property
	def AutomtcAllcn(self):
		return self._AutomtcAllcn

	@AutomtcAllcn.setter
	def AutomtcAllcn(self, value):
		self._AutomtcAllcn = value if type(value) != base_types.auto else self.make_default("AutomtcAllcn")

	@AutomtcAllcn.deleter
	def AutomtcAllcn(self):
		del self._AutomtcAllcn
		self._AutomtcAllcn = None

	@property
	def ValSghtMrgnRate(self):
		return self._ValSghtMrgnRate

	@ValSghtMrgnRate.setter
	def ValSghtMrgnRate(self, value):
		self._ValSghtMrgnRate = value if type(value) != base_types.auto else self.make_default("ValSghtMrgnRate")

	@ValSghtMrgnRate.deleter
	def ValSghtMrgnRate(self):
		del self._ValSghtMrgnRate
		self._ValSghtMrgnRate = None

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != base_types.auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

	@property
	def BsktIdAndElgbltySetPrfl(self):
		return self._BsktIdAndElgbltySetPrfl

	@BsktIdAndElgbltySetPrfl.setter
	def BsktIdAndElgbltySetPrfl(self, value):
		self._BsktIdAndElgbltySetPrfl = value if type(value) != base_types.auto else self.make_default("BsktIdAndElgbltySetPrfl")

	@BsktIdAndElgbltySetPrfl.deleter
	def BsktIdAndElgbltySetPrfl(self):
		del self._BsktIdAndElgbltySetPrfl
		self._BsktIdAndElgbltySetPrfl = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CollInstrTp(self):
		return self._CollInstrTp

	@CollInstrTp.setter
	def CollInstrTp(self, value):
		self._CollInstrTp = value if type(value) != base_types.auto else self.make_default("CollInstrTp")

	@CollInstrTp.deleter
	def CollInstrTp(self):
		del self._CollInstrTp
		self._CollInstrTp = None

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if type(value) != base_types.auto else self.make_default("CollSd")

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = None

	@property
	def SttlmPrc(self):
		return self._SttlmPrc

	@SttlmPrc.setter
	def SttlmPrc(self, value):
		self._SttlmPrc = value if type(value) != base_types.auto else self.make_default("SttlmPrc")

	@SttlmPrc.deleter
	def SttlmPrc(self):
		del self._SttlmPrc
		self._SttlmPrc = None

	@property
	def FaildSttlmSlvtn(self):
		return self._FaildSttlmSlvtn

	@FaildSttlmSlvtn.setter
	def FaildSttlmSlvtn(self, value):
		self._FaildSttlmSlvtn = value if type(value) != base_types.auto else self.make_default("FaildSttlmSlvtn")

	@FaildSttlmSlvtn.deleter
	def FaildSttlmSlvtn(self):
		del self._FaildSttlmSlvtn
		self._FaildSttlmSlvtn = None

	@property
	def MainTradgAcctCollstn(self):
		return self._MainTradgAcctCollstn

	@MainTradgAcctCollstn.setter
	def MainTradgAcctCollstn(self, value):
		self._MainTradgAcctCollstn = value if type(value) != base_types.auto else self.make_default("MainTradgAcctCollstn")

	@MainTradgAcctCollstn.deleter
	def MainTradgAcctCollstn(self):
		del self._MainTradgAcctCollstn
		self._MainTradgAcctCollstn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnSts', type=ResponseStatus9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTitl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutomtcAllcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValSghtMrgnRate', type=RateOrType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdAndElgbltySetPrfl', type=BasketIdentificationAndEligibilitySetProfile1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInstrTp', type=CollateralTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaildSttlmSlvtn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainTradgAcctCollstn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

