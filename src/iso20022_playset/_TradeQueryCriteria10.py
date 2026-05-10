from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._TradeAdditionalQueryCriteria7 import TradeAdditionalQueryCriteria7
from ._TradeDateTimeQueryCriteria2 import TradeDateTimeQueryCriteria2
from ._TradePartyQueryCriteria5 import TradePartyQueryCriteria5
from ._TradeTypeQueryCriteria2 import TradeTypeQueryCriteria2

class TradeQueryCriteria10(base_types._BaseFieldType):

	__slots__ = ["_OthrCrit", "_TradLifeCyclHstry", "_OutsdngTradInd", "_TradTpCrit", "_TradPtyCrit", "_TmCrit"]
	@property
	def OthrCrit(self):
		return self._OthrCrit

	@OthrCrit.setter
	def OthrCrit(self, value):
		self._OthrCrit = value if type(value) != base_types.auto else self.make_default("OthrCrit")

	@OthrCrit.deleter
	def OthrCrit(self):
		del self._OthrCrit
		self._OthrCrit = None

	@property
	def OutsdngTradInd(self):
		return self._OutsdngTradInd

	@OutsdngTradInd.setter
	def OutsdngTradInd(self, value):
		self._OutsdngTradInd = value if type(value) != base_types.auto else self.make_default("OutsdngTradInd")

	@OutsdngTradInd.deleter
	def OutsdngTradInd(self):
		del self._OutsdngTradInd
		self._OutsdngTradInd = None

	@property
	def TmCrit(self):
		return self._TmCrit

	@TmCrit.setter
	def TmCrit(self, value):
		self._TmCrit = value if type(value) != base_types.auto else self.make_default("TmCrit")

	@TmCrit.deleter
	def TmCrit(self):
		del self._TmCrit
		self._TmCrit = None

	@property
	def TradLifeCyclHstry(self):
		return self._TradLifeCyclHstry

	@TradLifeCyclHstry.setter
	def TradLifeCyclHstry(self, value):
		self._TradLifeCyclHstry = value if type(value) != base_types.auto else self.make_default("TradLifeCyclHstry")

	@TradLifeCyclHstry.deleter
	def TradLifeCyclHstry(self):
		del self._TradLifeCyclHstry
		self._TradLifeCyclHstry = None

	@property
	def TradPtyCrit(self):
		return self._TradPtyCrit

	@TradPtyCrit.setter
	def TradPtyCrit(self, value):
		self._TradPtyCrit = value if type(value) != base_types.auto else self.make_default("TradPtyCrit")

	@TradPtyCrit.deleter
	def TradPtyCrit(self):
		del self._TradPtyCrit
		self._TradPtyCrit = None

	@property
	def TradTpCrit(self):
		return self._TradTpCrit

	@TradTpCrit.setter
	def TradTpCrit(self, value):
		self._TradTpCrit = value if type(value) != base_types.auto else self.make_default("TradTpCrit")

	@TradTpCrit.deleter
	def TradTpCrit(self):
		del self._TradTpCrit
		self._TradTpCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrCrit', type=TradeAdditionalQueryCriteria7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngTradInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCrit', type=TradeDateTimeQueryCriteria2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLifeCyclHstry', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPtyCrit', type=TradePartyQueryCriteria5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTpCrit', type=TradeTypeQueryCriteria2, min=0, max=1, mutex_group=None, array=False),
	))

