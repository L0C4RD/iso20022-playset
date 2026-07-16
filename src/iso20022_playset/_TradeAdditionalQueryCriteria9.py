# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateSectorCriteria6
from . import DerivativeEventType3Code
from . import ModificationLevel1Code
from . import PartyNatureType1Code
from . import ProductClassificationCriteria1
from . import ProductType4Code
from . import SecuritiesTradeVenueCriteria1Choice
from . import TransactionOperationType8Code

class TradeAdditionalQueryCriteria9(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_AsstClss", "_CorpSctr", "_EvtTp", "_ExctnVn", "_Lvl", "_NtrOfCtrPty", "_PdctClssfctn"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType8Code, True)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType8Code, True)

	@property
	def AsstClss(self):
		return self._AsstClss

	@AsstClss.setter
	def AsstClss(self, value):
		self._AsstClss = value if value is not None else base_types.UninitialisedField(self, 'AsstClss', ProductType4Code, True)

	@AsstClss.deleter
	def AsstClss(self):
		del self._AsstClss
		self._AsstClss = base_types.UninitialisedField(self, 'AsstClss', ProductType4Code, True)

	@property
	def CorpSctr(self):
		return self._CorpSctr

	@CorpSctr.setter
	def CorpSctr(self, value):
		self._CorpSctr = value if value is not None else base_types.UninitialisedField(self, 'CorpSctr', CorporateSectorCriteria6, False)

	@CorpSctr.deleter
	def CorpSctr(self):
		del self._CorpSctr
		self._CorpSctr = base_types.UninitialisedField(self, 'CorpSctr', CorporateSectorCriteria6, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', DerivativeEventType3Code, True)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', DerivativeEventType3Code, True)

	@property
	def ExctnVn(self):
		return self._ExctnVn

	@ExctnVn.setter
	def ExctnVn(self, value):
		self._ExctnVn = value if value is not None else base_types.UninitialisedField(self, 'ExctnVn', SecuritiesTradeVenueCriteria1Choice, False)

	@ExctnVn.deleter
	def ExctnVn(self):
		del self._ExctnVn
		self._ExctnVn = base_types.UninitialisedField(self, 'ExctnVn', SecuritiesTradeVenueCriteria1Choice, False)

	@property
	def Lvl(self):
		return self._Lvl

	@Lvl.setter
	def Lvl(self, value):
		self._Lvl = value if value is not None else base_types.UninitialisedField(self, 'Lvl', ModificationLevel1Code, False)

	@Lvl.deleter
	def Lvl(self):
		del self._Lvl
		self._Lvl = base_types.UninitialisedField(self, 'Lvl', ModificationLevel1Code, False)

	@property
	def NtrOfCtrPty(self):
		return self._NtrOfCtrPty

	@NtrOfCtrPty.setter
	def NtrOfCtrPty(self, value):
		self._NtrOfCtrPty = value if value is not None else base_types.UninitialisedField(self, 'NtrOfCtrPty', PartyNatureType1Code, False)

	@NtrOfCtrPty.deleter
	def NtrOfCtrPty(self):
		del self._NtrOfCtrPty
		self._NtrOfCtrPty = base_types.UninitialisedField(self, 'NtrOfCtrPty', PartyNatureType1Code, False)

	@property
	def PdctClssfctn(self):
		return self._PdctClssfctn

	@PdctClssfctn.setter
	def PdctClssfctn(self, value):
		self._PdctClssfctn = value if value is not None else base_types.UninitialisedField(self, 'PdctClssfctn', ProductClassificationCriteria1, False)

	@PdctClssfctn.deleter
	def PdctClssfctn(self):
		del self._PdctClssfctn
		self._PdctClssfctn = base_types.UninitialisedField(self, 'PdctClssfctn', ProductClassificationCriteria1, False)

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