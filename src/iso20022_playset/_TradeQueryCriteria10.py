# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeAdditionalQueryCriteria7
from . import TradeDateTimeQueryCriteria2
from . import TradePartyQueryCriteria5
from . import TradeTypeQueryCriteria2
from . import TrueFalseIndicator

class TradeQueryCriteria10(base_types._BaseFieldType):

	__slots__ = ["_OthrCrit", "_OutsdngTradInd", "_TmCrit", "_TradLifeCyclHstry", "_TradPtyCrit", "_TradTpCrit"]
	@property
	def OthrCrit(self):
		return self._OthrCrit

	@OthrCrit.setter
	def OthrCrit(self, value):
		self._OthrCrit = value if value is not None else base_types.UninitialisedField(self, 'OthrCrit', TradeAdditionalQueryCriteria7, False)

	@OthrCrit.deleter
	def OthrCrit(self):
		del self._OthrCrit
		self._OthrCrit = base_types.UninitialisedField(self, 'OthrCrit', TradeAdditionalQueryCriteria7, False)

	@property
	def OutsdngTradInd(self):
		return self._OutsdngTradInd

	@OutsdngTradInd.setter
	def OutsdngTradInd(self, value):
		self._OutsdngTradInd = value if value is not None else base_types.UninitialisedField(self, 'OutsdngTradInd', TrueFalseIndicator, False)

	@OutsdngTradInd.deleter
	def OutsdngTradInd(self):
		del self._OutsdngTradInd
		self._OutsdngTradInd = base_types.UninitialisedField(self, 'OutsdngTradInd', TrueFalseIndicator, False)

	@property
	def TmCrit(self):
		return self._TmCrit

	@TmCrit.setter
	def TmCrit(self, value):
		self._TmCrit = value if value is not None else base_types.UninitialisedField(self, 'TmCrit', TradeDateTimeQueryCriteria2, False)

	@TmCrit.deleter
	def TmCrit(self):
		del self._TmCrit
		self._TmCrit = base_types.UninitialisedField(self, 'TmCrit', TradeDateTimeQueryCriteria2, False)

	@property
	def TradLifeCyclHstry(self):
		return self._TradLifeCyclHstry

	@TradLifeCyclHstry.setter
	def TradLifeCyclHstry(self, value):
		self._TradLifeCyclHstry = value if value is not None else base_types.UninitialisedField(self, 'TradLifeCyclHstry', TrueFalseIndicator, False)

	@TradLifeCyclHstry.deleter
	def TradLifeCyclHstry(self):
		del self._TradLifeCyclHstry
		self._TradLifeCyclHstry = base_types.UninitialisedField(self, 'TradLifeCyclHstry', TrueFalseIndicator, False)

	@property
	def TradPtyCrit(self):
		return self._TradPtyCrit

	@TradPtyCrit.setter
	def TradPtyCrit(self, value):
		self._TradPtyCrit = value if value is not None else base_types.UninitialisedField(self, 'TradPtyCrit', TradePartyQueryCriteria5, False)

	@TradPtyCrit.deleter
	def TradPtyCrit(self):
		del self._TradPtyCrit
		self._TradPtyCrit = base_types.UninitialisedField(self, 'TradPtyCrit', TradePartyQueryCriteria5, False)

	@property
	def TradTpCrit(self):
		return self._TradTpCrit

	@TradTpCrit.setter
	def TradTpCrit(self, value):
		self._TradTpCrit = value if value is not None else base_types.UninitialisedField(self, 'TradTpCrit', TradeTypeQueryCriteria2, False)

	@TradTpCrit.deleter
	def TradTpCrit(self):
		del self._TradTpCrit
		self._TradTpCrit = base_types.UninitialisedField(self, 'TradTpCrit', TradeTypeQueryCriteria2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrCrit', type=TradeAdditionalQueryCriteria7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngTradInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCrit', type=TradeDateTimeQueryCriteria2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLifeCyclHstry', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPtyCrit', type=TradePartyQueryCriteria5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTpCrit', type=TradeTypeQueryCriteria2, min=0, max=1, mutex_group=None, array=False),
	))