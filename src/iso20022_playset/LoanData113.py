import base_types
import ISODate
import AmountAndDirection53
import Max52Text

class LoanData113(base_types._BaseFieldType):

	__slots__ = ["_MktVal", "_UnqTradIdr", "_EvtDt"]
	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if type(value) != auto else self.make_default("UnqTradIdr")

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = None

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if type(value) != auto else self.make_default("EvtDt")

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

