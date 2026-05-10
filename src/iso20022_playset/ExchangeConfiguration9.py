from . import base_types
import ExchangePolicy2Code
import ProcessTiming6
import Number
import ProcessRetry3
import ImpliedCurrencyAndAmount

class ExchangeConfiguration9(base_types._BaseFieldType):

	__slots__ = ["_MaxNb", "_MaxAmt", "_TmCond", "_ReTry", "_XchgPlcy"]
	@property
	def MaxNb(self):
		return self._MaxNb

	@MaxNb.setter
	def MaxNb(self, value):
		self._MaxNb = value if type(value) != auto else self.make_default("MaxNb")

	@MaxNb.deleter
	def MaxNb(self):
		del self._MaxNb
		self._MaxNb = None

	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if type(value) != auto else self.make_default("MaxAmt")

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = None

	@property
	def TmCond(self):
		return self._TmCond

	@TmCond.setter
	def TmCond(self, value):
		self._TmCond = value if type(value) != auto else self.make_default("TmCond")

	@TmCond.deleter
	def TmCond(self):
		del self._TmCond
		self._TmCond = None

	@property
	def ReTry(self):
		return self._ReTry

	@ReTry.setter
	def ReTry(self, value):
		self._ReTry = value if type(value) != auto else self.make_default("ReTry")

	@ReTry.deleter
	def ReTry(self):
		del self._ReTry
		self._ReTry = None

	@property
	def XchgPlcy(self):
		return self._XchgPlcy

	@XchgPlcy.setter
	def XchgPlcy(self, value):
		self._XchgPlcy = value if type(value) != auto else self.make_default("XchgPlcy")

	@XchgPlcy.deleter
	def XchgPlcy(self):
		del self._XchgPlcy
		self._XchgPlcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCond', type=ProcessTiming6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReTry', type=ProcessRetry3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgPlcy', type=ExchangePolicy2Code, min=1, max=None, mutex_group=None, array=True),
	))

