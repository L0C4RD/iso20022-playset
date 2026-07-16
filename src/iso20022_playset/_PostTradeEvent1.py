# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ISODate
from . import Max35Text
from . import PostTradeEventType2Choice
from . import ProfitAndLossAmount2

class PostTradeEvent1(base_types._BaseFieldType):

	__slots__ = ["_OrgnlRef", "_OutsdngSttlmAmt", "_PrftOrLoss", "_PrftOrLossSttlmDt", "_Tp", "_UndrlygLbltyRef"]
	@property
	def OrgnlRef(self):
		return self._OrgnlRef

	@OrgnlRef.setter
	def OrgnlRef(self, value):
		self._OrgnlRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRef', Max35Text, False)

	@OrgnlRef.deleter
	def OrgnlRef(self):
		del self._OrgnlRef
		self._OrgnlRef = base_types.UninitialisedField(self, 'OrgnlRef', Max35Text, False)

	@property
	def OutsdngSttlmAmt(self):
		return self._OutsdngSttlmAmt

	@OutsdngSttlmAmt.setter
	def OutsdngSttlmAmt(self, value):
		self._OutsdngSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'OutsdngSttlmAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@OutsdngSttlmAmt.deleter
	def OutsdngSttlmAmt(self):
		del self._OutsdngSttlmAmt
		self._OutsdngSttlmAmt = base_types.UninitialisedField(self, 'OutsdngSttlmAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def PrftOrLoss(self):
		return self._PrftOrLoss

	@PrftOrLoss.setter
	def PrftOrLoss(self, value):
		self._PrftOrLoss = value if value is not None else base_types.UninitialisedField(self, 'PrftOrLoss', ProfitAndLossAmount2, False)

	@PrftOrLoss.deleter
	def PrftOrLoss(self):
		del self._PrftOrLoss
		self._PrftOrLoss = base_types.UninitialisedField(self, 'PrftOrLoss', ProfitAndLossAmount2, False)

	@property
	def PrftOrLossSttlmDt(self):
		return self._PrftOrLossSttlmDt

	@PrftOrLossSttlmDt.setter
	def PrftOrLossSttlmDt(self, value):
		self._PrftOrLossSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'PrftOrLossSttlmDt', ISODate, False)

	@PrftOrLossSttlmDt.deleter
	def PrftOrLossSttlmDt(self):
		del self._PrftOrLossSttlmDt
		self._PrftOrLossSttlmDt = base_types.UninitialisedField(self, 'PrftOrLossSttlmDt', ISODate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PostTradeEventType2Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PostTradeEventType2Choice, False)

	@property
	def UndrlygLbltyRef(self):
		return self._UndrlygLbltyRef

	@UndrlygLbltyRef.setter
	def UndrlygLbltyRef(self, value):
		self._UndrlygLbltyRef = value if value is not None else base_types.UninitialisedField(self, 'UndrlygLbltyRef', Max35Text, False)

	@UndrlygLbltyRef.deleter
	def UndrlygLbltyRef(self):
		del self._UndrlygLbltyRef
		self._UndrlygLbltyRef = base_types.UninitialisedField(self, 'UndrlygLbltyRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrftOrLoss', type=ProfitAndLossAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrftOrLossSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PostTradeEventType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygLbltyRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))