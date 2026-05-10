from . import base_types
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .ReuseValue1Choice import ReuseValue1Choice

class VolumeMetrics4(base_types._BaseFieldType):

	__slots__ = ["_RinvstdCshAmt", "_ReuseVal"]
	@property
	def RinvstdCshAmt(self):
		return self._RinvstdCshAmt

	@RinvstdCshAmt.setter
	def RinvstdCshAmt(self, value):
		self._RinvstdCshAmt = value if type(value) != base_types.auto else self.make_default("RinvstdCshAmt")

	@RinvstdCshAmt.deleter
	def RinvstdCshAmt(self):
		del self._RinvstdCshAmt
		self._RinvstdCshAmt = None

	@property
	def ReuseVal(self):
		return self._ReuseVal

	@ReuseVal.setter
	def ReuseVal(self, value):
		self._ReuseVal = value if type(value) != base_types.auto else self.make_default("ReuseVal")

	@ReuseVal.deleter
	def ReuseVal(self):
		del self._ReuseVal
		self._ReuseVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RinvstdCshAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReuseVal', type=ReuseValue1Choice, min=0, max=1, mutex_group=None, array=False),
	))

