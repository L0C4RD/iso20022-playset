# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation24
from . import BasketIdentificationAndEligibilitySetProfile1
from . import CollateralRole1Code
from . import CollateralTransactionType1Choice
from . import ExposureType23Choice
from . import GenericIdentification30
from . import RateOrType1Choice
from . import ResponseStatus9Choice
from . import YesNoIndicator

class CollateralParameters10(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AutomtcAllcn", "_BsktIdAndElgbltySetPrfl", "_CollInstrTp", "_CollSd", "_FaildSttlmSlvtn", "_MainTradgAcctCollstn", "_Prty", "_RspnSts", "_SttlmPrc", "_TrfTitl", "_ValSghtMrgnRate", "_XpsrTp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation24, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation24, False)

	@property
	def AutomtcAllcn(self):
		return self._AutomtcAllcn

	@AutomtcAllcn.setter
	def AutomtcAllcn(self, value):
		self._AutomtcAllcn = value if value is not None else base_types.UninitialisedField(self, 'AutomtcAllcn', YesNoIndicator, False)

	@AutomtcAllcn.deleter
	def AutomtcAllcn(self):
		del self._AutomtcAllcn
		self._AutomtcAllcn = base_types.UninitialisedField(self, 'AutomtcAllcn', YesNoIndicator, False)

	@property
	def BsktIdAndElgbltySetPrfl(self):
		return self._BsktIdAndElgbltySetPrfl

	@BsktIdAndElgbltySetPrfl.setter
	def BsktIdAndElgbltySetPrfl(self, value):
		self._BsktIdAndElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'BsktIdAndElgbltySetPrfl', BasketIdentificationAndEligibilitySetProfile1, False)

	@BsktIdAndElgbltySetPrfl.deleter
	def BsktIdAndElgbltySetPrfl(self):
		del self._BsktIdAndElgbltySetPrfl
		self._BsktIdAndElgbltySetPrfl = base_types.UninitialisedField(self, 'BsktIdAndElgbltySetPrfl', BasketIdentificationAndEligibilitySetProfile1, False)

	@property
	def CollInstrTp(self):
		return self._CollInstrTp

	@CollInstrTp.setter
	def CollInstrTp(self, value):
		self._CollInstrTp = value if value is not None else base_types.UninitialisedField(self, 'CollInstrTp', CollateralTransactionType1Choice, False)

	@CollInstrTp.deleter
	def CollInstrTp(self):
		del self._CollInstrTp
		self._CollInstrTp = base_types.UninitialisedField(self, 'CollInstrTp', CollateralTransactionType1Choice, False)

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if value is not None else base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@property
	def FaildSttlmSlvtn(self):
		return self._FaildSttlmSlvtn

	@FaildSttlmSlvtn.setter
	def FaildSttlmSlvtn(self, value):
		self._FaildSttlmSlvtn = value if value is not None else base_types.UninitialisedField(self, 'FaildSttlmSlvtn', YesNoIndicator, False)

	@FaildSttlmSlvtn.deleter
	def FaildSttlmSlvtn(self):
		del self._FaildSttlmSlvtn
		self._FaildSttlmSlvtn = base_types.UninitialisedField(self, 'FaildSttlmSlvtn', YesNoIndicator, False)

	@property
	def MainTradgAcctCollstn(self):
		return self._MainTradgAcctCollstn

	@MainTradgAcctCollstn.setter
	def MainTradgAcctCollstn(self, value):
		self._MainTradgAcctCollstn = value if value is not None else base_types.UninitialisedField(self, 'MainTradgAcctCollstn', YesNoIndicator, False)

	@MainTradgAcctCollstn.deleter
	def MainTradgAcctCollstn(self):
		del self._MainTradgAcctCollstn
		self._MainTradgAcctCollstn = base_types.UninitialisedField(self, 'MainTradgAcctCollstn', YesNoIndicator, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', GenericIdentification30, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', GenericIdentification30, False)

	@property
	def RspnSts(self):
		return self._RspnSts

	@RspnSts.setter
	def RspnSts(self, value):
		self._RspnSts = value if value is not None else base_types.UninitialisedField(self, 'RspnSts', ResponseStatus9Choice, False)

	@RspnSts.deleter
	def RspnSts(self):
		del self._RspnSts
		self._RspnSts = base_types.UninitialisedField(self, 'RspnSts', ResponseStatus9Choice, False)

	@property
	def SttlmPrc(self):
		return self._SttlmPrc

	@SttlmPrc.setter
	def SttlmPrc(self, value):
		self._SttlmPrc = value if value is not None else base_types.UninitialisedField(self, 'SttlmPrc', GenericIdentification30, False)

	@SttlmPrc.deleter
	def SttlmPrc(self):
		del self._SttlmPrc
		self._SttlmPrc = base_types.UninitialisedField(self, 'SttlmPrc', GenericIdentification30, False)

	@property
	def TrfTitl(self):
		return self._TrfTitl

	@TrfTitl.setter
	def TrfTitl(self, value):
		self._TrfTitl = value if value is not None else base_types.UninitialisedField(self, 'TrfTitl', YesNoIndicator, False)

	@TrfTitl.deleter
	def TrfTitl(self):
		del self._TrfTitl
		self._TrfTitl = base_types.UninitialisedField(self, 'TrfTitl', YesNoIndicator, False)

	@property
	def ValSghtMrgnRate(self):
		return self._ValSghtMrgnRate

	@ValSghtMrgnRate.setter
	def ValSghtMrgnRate(self, value):
		self._ValSghtMrgnRate = value if value is not None else base_types.UninitialisedField(self, 'ValSghtMrgnRate', RateOrType1Choice, False)

	@ValSghtMrgnRate.deleter
	def ValSghtMrgnRate(self):
		del self._ValSghtMrgnRate
		self._ValSghtMrgnRate = base_types.UninitialisedField(self, 'ValSghtMrgnRate', RateOrType1Choice, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType23Choice, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType23Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutomtcAllcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdAndElgbltySetPrfl', type=BasketIdentificationAndEligibilitySetProfile1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInstrTp', type=CollateralTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaildSttlmSlvtn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainTradgAcctCollstn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSts', type=ResponseStatus9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrc', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTitl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValSghtMrgnRate', type=RateOrType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
	))