from . import base_types
from ._CorporateSectorCriteria6 import CorporateSectorCriteria6
from ._DerivativeEventType3Code import DerivativeEventType3Code
from ._ModificationLevel1Code import ModificationLevel1Code
from ._PartyNatureType1Code import PartyNatureType1Code
from ._ProductClassificationCriteria1 import ProductClassificationCriteria1
from ._ProductType4Code import ProductType4Code
from ._SecuritiesTradeVenueCriteria1Choice import SecuritiesTradeVenueCriteria1Choice
from ._TransactionOperationType8Code import TransactionOperationType8Code

class TradeAdditionalQueryCriteria9(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_AsstClss", "_CorpSctr", "_EvtTp", "_ExctnVn", "_Lvl", "_NtrOfCtrPty", "_PdctClssfctn"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != base_types.auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

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
	def CorpSctr(self):
		return self._CorpSctr

	@CorpSctr.setter
	def CorpSctr(self, value):
		self._CorpSctr = value if type(value) != base_types.auto else self.make_default("CorpSctr")

	@CorpSctr.deleter
	def CorpSctr(self):
		del self._CorpSctr
		self._CorpSctr = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != base_types.auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	@property
	def ExctnVn(self):
		return self._ExctnVn

	@ExctnVn.setter
	def ExctnVn(self, value):
		self._ExctnVn = value if type(value) != base_types.auto else self.make_default("ExctnVn")

	@ExctnVn.deleter
	def ExctnVn(self):
		del self._ExctnVn
		self._ExctnVn = None

	@property
	def Lvl(self):
		return self._Lvl

	@Lvl.setter
	def Lvl(self, value):
		self._Lvl = value if type(value) != base_types.auto else self.make_default("Lvl")

	@Lvl.deleter
	def Lvl(self):
		del self._Lvl
		self._Lvl = None

	@property
	def NtrOfCtrPty(self):
		return self._NtrOfCtrPty

	@NtrOfCtrPty.setter
	def NtrOfCtrPty(self, value):
		self._NtrOfCtrPty = value if type(value) != base_types.auto else self.make_default("NtrOfCtrPty")

	@NtrOfCtrPty.deleter
	def NtrOfCtrPty(self):
		del self._NtrOfCtrPty
		self._NtrOfCtrPty = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TransactionOperationType8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AsstClss', type=ProductType4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpSctr', type=CorporateSectorCriteria6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=DerivativeEventType3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ExctnVn', type=SecuritiesTradeVenueCriteria1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lvl', type=ModificationLevel1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtrOfCtrPty', type=PartyNatureType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctClssfctn', type=ProductClassificationCriteria1, min=0, max=1, mutex_group=None, array=False),
	))

