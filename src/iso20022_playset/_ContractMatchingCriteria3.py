from . import base_types
from .CompareFinancialInstrumentContractType1 import CompareFinancialInstrumentContractType1
from .CompareISINIdentifier2 import CompareISINIdentifier2
from .CompareCFIIdentifier3 import CompareCFIIdentifier3
from .CompareActiveOrHistoricCurrencyCode1 import CompareActiveOrHistoricCurrencyCode1
from .CompareUnderlyingInstrument3 import CompareUnderlyingInstrument3
from .CompareAssetClass1 import CompareAssetClass1
from .CompareTrueFalseIndicator3 import CompareTrueFalseIndicator3
from .CompareText1 import CompareText1
from .CompareUniqueProductIdentifier2 import CompareUniqueProductIdentifier2

class ContractMatchingCriteria3(base_types._BaseFieldType):

	__slots__ = ["_DerivBasedOnCrptAsst", "_AltrntvInstrmId", "_AsstClss", "_UnqPdctIdr", "_SttlmCcy", "_PdctClssfctn", "_ISIN", "_CtrctTp", "_SttlmCcyScndLeg", "_UndrlygInstrm"]
	@property
	def DerivBasedOnCrptAsst(self):
		return self._DerivBasedOnCrptAsst

	@DerivBasedOnCrptAsst.setter
	def DerivBasedOnCrptAsst(self, value):
		self._DerivBasedOnCrptAsst = value if type(value) != base_types.auto else self.make_default("DerivBasedOnCrptAsst")

	@DerivBasedOnCrptAsst.deleter
	def DerivBasedOnCrptAsst(self):
		del self._DerivBasedOnCrptAsst
		self._DerivBasedOnCrptAsst = None

	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if type(value) != base_types.auto else self.make_default("AltrntvInstrmId")

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = None

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

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if type(value) != base_types.auto else self.make_default("UnqPdctIdr")

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = None

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
	def PdctClssfctn(self):
		return self._PdctClssfctn

	@PdctClssfctn.setter
	def PdctClssfctn(self, value):
		self._PdctClssfctn = value if type(value) != base_types.auto else self.make_default("PdctClssfctn")

	@PdctClssfctn.deleter
	def PdctClssfctn(self):
		del self._PdctClssfctn
		self._PdctClssfctn = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

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
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if type(value) != base_types.auto else self.make_default("UndrlygInstrm")

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DerivBasedOnCrptAsst', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrntvInstrmId', type=CompareText1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstClss', type=CompareAssetClass1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=CompareUniqueProductIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=CompareActiveOrHistoricCurrencyCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctClssfctn', type=CompareCFIIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISIN', type=CompareISINIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=CompareFinancialInstrumentContractType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcyScndLeg', type=CompareActiveOrHistoricCurrencyCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrm', type=CompareUnderlyingInstrument3, min=0, max=1, mutex_group=None, array=False),
	))

