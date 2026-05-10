from . import base_types
from ._Max35Text import Max35Text
from ._ProfitAndLossAmount2 import ProfitAndLossAmount2
from ._PostTradeEventType2Choice import PostTradeEventType2Choice
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ISODate import ISODate

class PostTradeEvent1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_UndrlygLbltyRef", "_OutsdngSttlmAmt", "_PrftOrLossSttlmDt", "_PrftOrLoss", "_OrgnlRef"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def UndrlygLbltyRef(self):
		return self._UndrlygLbltyRef

	@UndrlygLbltyRef.setter
	def UndrlygLbltyRef(self, value):
		self._UndrlygLbltyRef = value if type(value) != base_types.auto else self.make_default("UndrlygLbltyRef")

	@UndrlygLbltyRef.deleter
	def UndrlygLbltyRef(self):
		del self._UndrlygLbltyRef
		self._UndrlygLbltyRef = None

	@property
	def OutsdngSttlmAmt(self):
		return self._OutsdngSttlmAmt

	@OutsdngSttlmAmt.setter
	def OutsdngSttlmAmt(self, value):
		self._OutsdngSttlmAmt = value if type(value) != base_types.auto else self.make_default("OutsdngSttlmAmt")

	@OutsdngSttlmAmt.deleter
	def OutsdngSttlmAmt(self):
		del self._OutsdngSttlmAmt
		self._OutsdngSttlmAmt = None

	@property
	def PrftOrLossSttlmDt(self):
		return self._PrftOrLossSttlmDt

	@PrftOrLossSttlmDt.setter
	def PrftOrLossSttlmDt(self, value):
		self._PrftOrLossSttlmDt = value if type(value) != base_types.auto else self.make_default("PrftOrLossSttlmDt")

	@PrftOrLossSttlmDt.deleter
	def PrftOrLossSttlmDt(self):
		del self._PrftOrLossSttlmDt
		self._PrftOrLossSttlmDt = None

	@property
	def PrftOrLoss(self):
		return self._PrftOrLoss

	@PrftOrLoss.setter
	def PrftOrLoss(self, value):
		self._PrftOrLoss = value if type(value) != base_types.auto else self.make_default("PrftOrLoss")

	@PrftOrLoss.deleter
	def PrftOrLoss(self):
		del self._PrftOrLoss
		self._PrftOrLoss = None

	@property
	def OrgnlRef(self):
		return self._OrgnlRef

	@OrgnlRef.setter
	def OrgnlRef(self, value):
		self._OrgnlRef = value if type(value) != base_types.auto else self.make_default("OrgnlRef")

	@OrgnlRef.deleter
	def OrgnlRef(self):
		del self._OrgnlRef
		self._OrgnlRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=PostTradeEventType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygLbltyRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrftOrLossSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrftOrLoss', type=ProfitAndLossAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

