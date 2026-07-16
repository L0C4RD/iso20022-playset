# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CFIOct2015Identifier
from . import CountryCode
from . import CurrencyExchange23
from . import FinancialInstrumentContractType2Code
from . import MICIdentifier
from . import Max50Text
from . import ProductType4Code
from . import SecurityIdentification41Choice
from . import SecurityIdentification46
from . import TrueFalseIndicator

class ContractType15(base_types._BaseFieldType):

	__slots__ = ["_AsstClss", "_CtrctTp", "_DerivBasedOnCrptAsst", "_PdctClssfctn", "_PdctId", "_PlcOfSttlm", "_SttlmCcy", "_SttlmCcyScndLeg", "_UndrlygAsstPricSrc", "_UndrlygAsstTradgPltfmIdr", "_UndrlygInstrm"]
	@property
	def AsstClss(self):
		return self._AsstClss

	@AsstClss.setter
	def AsstClss(self, value):
		self._AsstClss = value if value is not None else base_types.UninitialisedField(self, 'AsstClss', ProductType4Code, False)

	@AsstClss.deleter
	def AsstClss(self):
		del self._AsstClss
		self._AsstClss = base_types.UninitialisedField(self, 'AsstClss', ProductType4Code, False)

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctTp', FinancialInstrumentContractType2Code, False)

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = base_types.UninitialisedField(self, 'CtrctTp', FinancialInstrumentContractType2Code, False)

	@property
	def DerivBasedOnCrptAsst(self):
		return self._DerivBasedOnCrptAsst

	@DerivBasedOnCrptAsst.setter
	def DerivBasedOnCrptAsst(self, value):
		self._DerivBasedOnCrptAsst = value if value is not None else base_types.UninitialisedField(self, 'DerivBasedOnCrptAsst', TrueFalseIndicator, False)

	@DerivBasedOnCrptAsst.deleter
	def DerivBasedOnCrptAsst(self):
		del self._DerivBasedOnCrptAsst
		self._DerivBasedOnCrptAsst = base_types.UninitialisedField(self, 'DerivBasedOnCrptAsst', TrueFalseIndicator, False)

	@property
	def PdctClssfctn(self):
		return self._PdctClssfctn

	@PdctClssfctn.setter
	def PdctClssfctn(self, value):
		self._PdctClssfctn = value if value is not None else base_types.UninitialisedField(self, 'PdctClssfctn', CFIOct2015Identifier, False)

	@PdctClssfctn.deleter
	def PdctClssfctn(self):
		del self._PdctClssfctn
		self._PdctClssfctn = base_types.UninitialisedField(self, 'PdctClssfctn', CFIOct2015Identifier, False)

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if value is not None else base_types.UninitialisedField(self, 'PdctId', SecurityIdentification46, False)

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = base_types.UninitialisedField(self, 'PdctId', SecurityIdentification46, False)

	@property
	def PlcOfSttlm(self):
		return self._PlcOfSttlm

	@PlcOfSttlm.setter
	def PlcOfSttlm(self, value):
		self._PlcOfSttlm = value if value is not None else base_types.UninitialisedField(self, 'PlcOfSttlm', CountryCode, False)

	@PlcOfSttlm.deleter
	def PlcOfSttlm(self):
		del self._PlcOfSttlm
		self._PlcOfSttlm = base_types.UninitialisedField(self, 'PlcOfSttlm', CountryCode, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', CurrencyExchange23, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', CurrencyExchange23, False)

	@property
	def SttlmCcyScndLeg(self):
		return self._SttlmCcyScndLeg

	@SttlmCcyScndLeg.setter
	def SttlmCcyScndLeg(self, value):
		self._SttlmCcyScndLeg = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcyScndLeg', CurrencyExchange23, False)

	@SttlmCcyScndLeg.deleter
	def SttlmCcyScndLeg(self):
		del self._SttlmCcyScndLeg
		self._SttlmCcyScndLeg = base_types.UninitialisedField(self, 'SttlmCcyScndLeg', CurrencyExchange23, False)

	@property
	def UndrlygAsstPricSrc(self):
		return self._UndrlygAsstPricSrc

	@UndrlygAsstPricSrc.setter
	def UndrlygAsstPricSrc(self, value):
		self._UndrlygAsstPricSrc = value if value is not None else base_types.UninitialisedField(self, 'UndrlygAsstPricSrc', Max50Text, False)

	@UndrlygAsstPricSrc.deleter
	def UndrlygAsstPricSrc(self):
		del self._UndrlygAsstPricSrc
		self._UndrlygAsstPricSrc = base_types.UninitialisedField(self, 'UndrlygAsstPricSrc', Max50Text, False)

	@property
	def UndrlygAsstTradgPltfmIdr(self):
		return self._UndrlygAsstTradgPltfmIdr

	@UndrlygAsstTradgPltfmIdr.setter
	def UndrlygAsstTradgPltfmIdr(self, value):
		self._UndrlygAsstTradgPltfmIdr = value if value is not None else base_types.UninitialisedField(self, 'UndrlygAsstTradgPltfmIdr', MICIdentifier, False)

	@UndrlygAsstTradgPltfmIdr.deleter
	def UndrlygAsstTradgPltfmIdr(self):
		del self._UndrlygAsstTradgPltfmIdr
		self._UndrlygAsstTradgPltfmIdr = base_types.UninitialisedField(self, 'UndrlygAsstTradgPltfmIdr', MICIdentifier, False)

	@property
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if value is not None else base_types.UninitialisedField(self, 'UndrlygInstrm', SecurityIdentification41Choice, False)

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = base_types.UninitialisedField(self, 'UndrlygInstrm', SecurityIdentification41Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstClss', type=ProductType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=FinancialInstrumentContractType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivBasedOnCrptAsst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctClssfctn', type=CFIOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctId', type=SecurityIdentification46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfSttlm', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=CurrencyExchange23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcyScndLeg', type=CurrencyExchange23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygAsstPricSrc', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygAsstTradgPltfmIdr', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrm', type=SecurityIdentification41Choice, min=0, max=1, mutex_group=None, array=False),
	))