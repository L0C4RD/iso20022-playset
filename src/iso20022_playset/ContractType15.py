import base_types
import Max50Text
import SecurityIdentification46
import CountryCode
import TrueFalseIndicator
import CurrencyExchange23
import ProductType4Code
import CFIOct2015Identifier
import MICIdentifier
import SecurityIdentification41Choice
import FinancialInstrumentContractType2Code

class ContractType15(base_types._BaseFieldType):

	__slots__ = ["_UndrlygAsstPricSrc", "_AsstClss", "_PdctClssfctn", "_SttlmCcyScndLeg", "_SttlmCcy", "_PdctId", "_DerivBasedOnCrptAsst", "_CtrctTp", "_UndrlygAsstTradgPltfmIdr", "_UndrlygInstrm", "_PlcOfSttlm"]
	@property
	def UndrlygAsstPricSrc(self):
		return self._UndrlygAsstPricSrc

	@UndrlygAsstPricSrc.setter
	def UndrlygAsstPricSrc(self, value):
		self._UndrlygAsstPricSrc = value if type(value) != auto else self.make_default("UndrlygAsstPricSrc")

	@UndrlygAsstPricSrc.deleter
	def UndrlygAsstPricSrc(self):
		del self._UndrlygAsstPricSrc
		self._UndrlygAsstPricSrc = None

	@property
	def AsstClss(self):
		return self._AsstClss

	@AsstClss.setter
	def AsstClss(self, value):
		self._AsstClss = value if type(value) != auto else self.make_default("AsstClss")

	@AsstClss.deleter
	def AsstClss(self):
		del self._AsstClss
		self._AsstClss = None

	@property
	def PdctClssfctn(self):
		return self._PdctClssfctn

	@PdctClssfctn.setter
	def PdctClssfctn(self, value):
		self._PdctClssfctn = value if type(value) != auto else self.make_default("PdctClssfctn")

	@PdctClssfctn.deleter
	def PdctClssfctn(self):
		del self._PdctClssfctn
		self._PdctClssfctn = None

	@property
	def SttlmCcyScndLeg(self):
		return self._SttlmCcyScndLeg

	@SttlmCcyScndLeg.setter
	def SttlmCcyScndLeg(self, value):
		self._SttlmCcyScndLeg = value if type(value) != auto else self.make_default("SttlmCcyScndLeg")

	@SttlmCcyScndLeg.deleter
	def SttlmCcyScndLeg(self):
		del self._SttlmCcyScndLeg
		self._SttlmCcyScndLeg = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if type(value) != auto else self.make_default("PdctId")

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = None

	@property
	def DerivBasedOnCrptAsst(self):
		return self._DerivBasedOnCrptAsst

	@DerivBasedOnCrptAsst.setter
	def DerivBasedOnCrptAsst(self, value):
		self._DerivBasedOnCrptAsst = value if type(value) != auto else self.make_default("DerivBasedOnCrptAsst")

	@DerivBasedOnCrptAsst.deleter
	def DerivBasedOnCrptAsst(self):
		del self._DerivBasedOnCrptAsst
		self._DerivBasedOnCrptAsst = None

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if type(value) != auto else self.make_default("CtrctTp")

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = None

	@property
	def UndrlygAsstTradgPltfmIdr(self):
		return self._UndrlygAsstTradgPltfmIdr

	@UndrlygAsstTradgPltfmIdr.setter
	def UndrlygAsstTradgPltfmIdr(self, value):
		self._UndrlygAsstTradgPltfmIdr = value if type(value) != auto else self.make_default("UndrlygAsstTradgPltfmIdr")

	@UndrlygAsstTradgPltfmIdr.deleter
	def UndrlygAsstTradgPltfmIdr(self):
		del self._UndrlygAsstTradgPltfmIdr
		self._UndrlygAsstTradgPltfmIdr = None

	@property
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if type(value) != auto else self.make_default("UndrlygInstrm")

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = None

	@property
	def PlcOfSttlm(self):
		return self._PlcOfSttlm

	@PlcOfSttlm.setter
	def PlcOfSttlm(self, value):
		self._PlcOfSttlm = value if type(value) != auto else self.make_default("PlcOfSttlm")

	@PlcOfSttlm.deleter
	def PlcOfSttlm(self):
		del self._PlcOfSttlm
		self._PlcOfSttlm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UndrlygAsstPricSrc', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstClss', type=ProductType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctClssfctn', type=CFIOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcyScndLeg', type=CurrencyExchange23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=CurrencyExchange23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctId', type=SecurityIdentification46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivBasedOnCrptAsst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=FinancialInstrumentContractType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygAsstTradgPltfmIdr', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrm', type=SecurityIdentification41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfSttlm', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

