# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExchangePolicy2Code
from . import ImpliedCurrencyAndAmount
from . import Number
from . import ProcessRetry3
from . import ProcessTiming6
from . import TrueFalseIndicator

class ExchangeConfiguration10(base_types._BaseFieldType):

	__slots__ = ["_MaxAmt", "_MaxNb", "_ReTry", "_TmCond", "_XchgDclnd", "_XchgFaild", "_XchgPlcy"]
	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxAmt', ImpliedCurrencyAndAmount, False)

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = base_types.UninitialisedField(self, 'MaxAmt', ImpliedCurrencyAndAmount, False)

	@property
	def MaxNb(self):
		return self._MaxNb

	@MaxNb.setter
	def MaxNb(self, value):
		self._MaxNb = value if value is not None else base_types.UninitialisedField(self, 'MaxNb', Number, False)

	@MaxNb.deleter
	def MaxNb(self):
		del self._MaxNb
		self._MaxNb = base_types.UninitialisedField(self, 'MaxNb', Number, False)

	@property
	def ReTry(self):
		return self._ReTry

	@ReTry.setter
	def ReTry(self, value):
		self._ReTry = value if value is not None else base_types.UninitialisedField(self, 'ReTry', ProcessRetry3, False)

	@ReTry.deleter
	def ReTry(self):
		del self._ReTry
		self._ReTry = base_types.UninitialisedField(self, 'ReTry', ProcessRetry3, False)

	@property
	def TmCond(self):
		return self._TmCond

	@TmCond.setter
	def TmCond(self, value):
		self._TmCond = value if value is not None else base_types.UninitialisedField(self, 'TmCond', ProcessTiming6, False)

	@TmCond.deleter
	def TmCond(self):
		del self._TmCond
		self._TmCond = base_types.UninitialisedField(self, 'TmCond', ProcessTiming6, False)

	@property
	def XchgDclnd(self):
		return self._XchgDclnd

	@XchgDclnd.setter
	def XchgDclnd(self, value):
		self._XchgDclnd = value if value is not None else base_types.UninitialisedField(self, 'XchgDclnd', TrueFalseIndicator, False)

	@XchgDclnd.deleter
	def XchgDclnd(self):
		del self._XchgDclnd
		self._XchgDclnd = base_types.UninitialisedField(self, 'XchgDclnd', TrueFalseIndicator, False)

	@property
	def XchgFaild(self):
		return self._XchgFaild

	@XchgFaild.setter
	def XchgFaild(self, value):
		self._XchgFaild = value if value is not None else base_types.UninitialisedField(self, 'XchgFaild', TrueFalseIndicator, False)

	@XchgFaild.deleter
	def XchgFaild(self):
		del self._XchgFaild
		self._XchgFaild = base_types.UninitialisedField(self, 'XchgFaild', TrueFalseIndicator, False)

	@property
	def XchgPlcy(self):
		return self._XchgPlcy

	@XchgPlcy.setter
	def XchgPlcy(self, value):
		self._XchgPlcy = value if value is not None else base_types.UninitialisedField(self, 'XchgPlcy', ExchangePolicy2Code, True)

	@XchgPlcy.deleter
	def XchgPlcy(self):
		del self._XchgPlcy
		self._XchgPlcy = base_types.UninitialisedField(self, 'XchgPlcy', ExchangePolicy2Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReTry', type=ProcessRetry3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCond', type=ProcessTiming6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgDclnd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgFaild', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgPlcy', type=ExchangePolicy2Code, min=1, max=None, mutex_group=None, array=True),
	))