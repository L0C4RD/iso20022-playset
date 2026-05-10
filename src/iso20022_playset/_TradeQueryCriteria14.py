from . import base_types
from ._TradeAdditionalQueryCriteria9 import TradeAdditionalQueryCriteria9
from ._TradeDateTimeQueryCriteria6 import TradeDateTimeQueryCriteria6
from ._TradePartyQueryCriteria7 import TradePartyQueryCriteria7
from ._TradeSecurityIdentificationQueryCriteria3 import TradeSecurityIdentificationQueryCriteria3
from ._TrueFalseIndicator import TrueFalseIndicator

class TradeQueryCriteria14(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmCrit", "_MrgnLifeCyclHstry", "_OthrCrit", "_OutsdngTradInd", "_TmCrit", "_TradLifeCyclHstry", "_TradPtyCrit"]
	@property
	def FinInstrmCrit(self):
		return self._FinInstrmCrit

	@FinInstrmCrit.setter
	def FinInstrmCrit(self, value):
		self._FinInstrmCrit = value if type(value) != base_types.auto else self.make_default("FinInstrmCrit")

	@FinInstrmCrit.deleter
	def FinInstrmCrit(self):
		del self._FinInstrmCrit
		self._FinInstrmCrit = None

	@property
	def MrgnLifeCyclHstry(self):
		return self._MrgnLifeCyclHstry

	@MrgnLifeCyclHstry.setter
	def MrgnLifeCyclHstry(self, value):
		self._MrgnLifeCyclHstry = value if type(value) != base_types.auto else self.make_default("MrgnLifeCyclHstry")

	@MrgnLifeCyclHstry.deleter
	def MrgnLifeCyclHstry(self):
		del self._MrgnLifeCyclHstry
		self._MrgnLifeCyclHstry = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmCrit', type=TradeSecurityIdentificationQueryCriteria3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLifeCyclHstry', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCrit', type=TradeAdditionalQueryCriteria9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngTradInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCrit', type=TradeDateTimeQueryCriteria6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLifeCyclHstry', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPtyCrit', type=TradePartyQueryCriteria7, min=0, max=1, mutex_group=None, array=False),
	))

