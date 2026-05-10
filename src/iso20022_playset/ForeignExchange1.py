import base_types
import BaseOneRate
import ActiveOrHistoricCurrencyCode
import DecimalNumber

class ForeignExchange1(base_types._BaseFieldType):

	__slots__ = ["_FrgnCcy", "_XchgSpotRate", "_XchgFwdPt"]
	@property
	def FrgnCcy(self):
		return self._FrgnCcy

	@FrgnCcy.setter
	def FrgnCcy(self, value):
		self._FrgnCcy = value if type(value) != auto else self.make_default("FrgnCcy")

	@FrgnCcy.deleter
	def FrgnCcy(self):
		del self._FrgnCcy
		self._FrgnCcy = None

	@property
	def XchgSpotRate(self):
		return self._XchgSpotRate

	@XchgSpotRate.setter
	def XchgSpotRate(self, value):
		self._XchgSpotRate = value if type(value) != auto else self.make_default("XchgSpotRate")

	@XchgSpotRate.deleter
	def XchgSpotRate(self):
		del self._XchgSpotRate
		self._XchgSpotRate = None

	@property
	def XchgFwdPt(self):
		return self._XchgFwdPt

	@XchgFwdPt.setter
	def XchgFwdPt(self, value):
		self._XchgFwdPt = value if type(value) != auto else self.make_default("XchgFwdPt")

	@XchgFwdPt.deleter
	def XchgFwdPt(self):
		del self._XchgFwdPt
		self._XchgFwdPt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrgnCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgSpotRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgFwdPt', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

