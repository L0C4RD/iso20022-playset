# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareActiveOrHistoricCurrencyCode1
from . import CompareAssetClass1
from . import CompareCFIIdentifier3
from . import CompareFinancialInstrumentContractType1
from . import CompareISINIdentifier2
from . import CompareText1
from . import CompareTrueFalseIndicator3
from . import CompareUnderlyingInstrument3
from . import CompareUniqueProductIdentifier2

class ContractMatchingCriteria3(base_types._BaseFieldType):

	__slots__ = ["_AltrntvInstrmId", "_AsstClss", "_CtrctTp", "_DerivBasedOnCrptAsst", "_ISIN", "_PdctClssfctn", "_SttlmCcy", "_SttlmCcyScndLeg", "_UndrlygInstrm", "_UnqPdctIdr"]
	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if value is not None else base_types.UninitialisedField(self, 'AltrntvInstrmId', CompareText1, False)

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = base_types.UninitialisedField(self, 'AltrntvInstrmId', CompareText1, False)

	@property
	def AsstClss(self):
		return self._AsstClss

	@AsstClss.setter
	def AsstClss(self, value):
		self._AsstClss = value if value is not None else base_types.UninitialisedField(self, 'AsstClss', CompareAssetClass1, False)

	@AsstClss.deleter
	def AsstClss(self):
		del self._AsstClss
		self._AsstClss = base_types.UninitialisedField(self, 'AsstClss', CompareAssetClass1, False)

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctTp', CompareFinancialInstrumentContractType1, False)

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = base_types.UninitialisedField(self, 'CtrctTp', CompareFinancialInstrumentContractType1, False)

	@property
	def DerivBasedOnCrptAsst(self):
		return self._DerivBasedOnCrptAsst

	@DerivBasedOnCrptAsst.setter
	def DerivBasedOnCrptAsst(self, value):
		self._DerivBasedOnCrptAsst = value if value is not None else base_types.UninitialisedField(self, 'DerivBasedOnCrptAsst', CompareTrueFalseIndicator3, False)

	@DerivBasedOnCrptAsst.deleter
	def DerivBasedOnCrptAsst(self):
		del self._DerivBasedOnCrptAsst
		self._DerivBasedOnCrptAsst = base_types.UninitialisedField(self, 'DerivBasedOnCrptAsst', CompareTrueFalseIndicator3, False)

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', CompareISINIdentifier2, False)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', CompareISINIdentifier2, False)

	@property
	def PdctClssfctn(self):
		return self._PdctClssfctn

	@PdctClssfctn.setter
	def PdctClssfctn(self, value):
		self._PdctClssfctn = value if value is not None else base_types.UninitialisedField(self, 'PdctClssfctn', CompareCFIIdentifier3, False)

	@PdctClssfctn.deleter
	def PdctClssfctn(self):
		del self._PdctClssfctn
		self._PdctClssfctn = base_types.UninitialisedField(self, 'PdctClssfctn', CompareCFIIdentifier3, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', CompareActiveOrHistoricCurrencyCode1, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', CompareActiveOrHistoricCurrencyCode1, False)

	@property
	def SttlmCcyScndLeg(self):
		return self._SttlmCcyScndLeg

	@SttlmCcyScndLeg.setter
	def SttlmCcyScndLeg(self, value):
		self._SttlmCcyScndLeg = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcyScndLeg', CompareActiveOrHistoricCurrencyCode1, False)

	@SttlmCcyScndLeg.deleter
	def SttlmCcyScndLeg(self):
		del self._SttlmCcyScndLeg
		self._SttlmCcyScndLeg = base_types.UninitialisedField(self, 'SttlmCcyScndLeg', CompareActiveOrHistoricCurrencyCode1, False)

	@property
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if value is not None else base_types.UninitialisedField(self, 'UndrlygInstrm', CompareUnderlyingInstrument3, False)

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = base_types.UninitialisedField(self, 'UndrlygInstrm', CompareUnderlyingInstrument3, False)

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqPdctIdr', CompareUniqueProductIdentifier2, False)

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = base_types.UninitialisedField(self, 'UnqPdctIdr', CompareUniqueProductIdentifier2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvInstrmId', type=CompareText1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstClss', type=CompareAssetClass1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=CompareFinancialInstrumentContractType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivBasedOnCrptAsst', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISIN', type=CompareISINIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctClssfctn', type=CompareCFIIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=CompareActiveOrHistoricCurrencyCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcyScndLeg', type=CompareActiveOrHistoricCurrencyCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrm', type=CompareUnderlyingInstrument3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=CompareUniqueProductIdentifier2, min=0, max=1, mutex_group=None, array=False),
	))