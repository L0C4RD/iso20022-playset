from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ExchangePolicy2Code import ExchangePolicy2Code
from ._ProcessRetry3 import ProcessRetry3
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._ProcessTiming6 import ProcessTiming6
from ._Number import Number

class ExchangeConfiguration10(base_types._BaseFieldType):

	__slots__ = ["_XchgDclnd", "_ReTry", "_MaxNb", "_MaxAmt", "_XchgPlcy", "_TmCond", "_XchgFaild"]
	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if type(value) != base_types.auto else self.make_default("MaxAmt")

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = None

	@property
	def MaxNb(self):
		return self._MaxNb

	@MaxNb.setter
	def MaxNb(self, value):
		self._MaxNb = value if type(value) != base_types.auto else self.make_default("MaxNb")

	@MaxNb.deleter
	def MaxNb(self):
		del self._MaxNb
		self._MaxNb = None

	@property
	def ReTry(self):
		return self._ReTry

	@ReTry.setter
	def ReTry(self, value):
		self._ReTry = value if type(value) != base_types.auto else self.make_default("ReTry")

	@ReTry.deleter
	def ReTry(self):
		del self._ReTry
		self._ReTry = None

	@property
	def TmCond(self):
		return self._TmCond

	@TmCond.setter
	def TmCond(self, value):
		self._TmCond = value if type(value) != base_types.auto else self.make_default("TmCond")

	@TmCond.deleter
	def TmCond(self):
		del self._TmCond
		self._TmCond = None

	@property
	def XchgDclnd(self):
		return self._XchgDclnd

	@XchgDclnd.setter
	def XchgDclnd(self, value):
		self._XchgDclnd = value if type(value) != base_types.auto else self.make_default("XchgDclnd")

	@XchgDclnd.deleter
	def XchgDclnd(self):
		del self._XchgDclnd
		self._XchgDclnd = None

	@property
	def XchgFaild(self):
		return self._XchgFaild

	@XchgFaild.setter
	def XchgFaild(self, value):
		self._XchgFaild = value if type(value) != base_types.auto else self.make_default("XchgFaild")

	@XchgFaild.deleter
	def XchgFaild(self):
		del self._XchgFaild
		self._XchgFaild = None

	@property
	def XchgPlcy(self):
		return self._XchgPlcy

	@XchgPlcy.setter
	def XchgPlcy(self, value):
		self._XchgPlcy = value if type(value) != base_types.auto else self.make_default("XchgPlcy")

	@XchgPlcy.deleter
	def XchgPlcy(self):
		del self._XchgPlcy
		self._XchgPlcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReTry', type=ProcessRetry3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCond', type=ProcessTiming6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgDclnd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgFaild', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgPlcy', type=ExchangePolicy2Code, min=1, max=None, mutex_group=None, array=True),
	))

