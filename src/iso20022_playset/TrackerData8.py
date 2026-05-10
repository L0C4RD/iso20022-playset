import base_types
import DateAndDateTime2Choice
import ActiveCurrencyAndAmount

class TrackerData8(base_types._BaseFieldType):

	__slots__ = ["_RmngToBeConfdAmt", "_RtrdConfdAmt", "_ConfdAmt", "_PrevslyConfdAmt", "_ConfdDt", "_RtrdConfdDt", "_PrevslyConfdDt"]
	@property
	def RmngToBeConfdAmt(self):
		return self._RmngToBeConfdAmt

	@RmngToBeConfdAmt.setter
	def RmngToBeConfdAmt(self, value):
		self._RmngToBeConfdAmt = value if type(value) != auto else self.make_default("RmngToBeConfdAmt")

	@RmngToBeConfdAmt.deleter
	def RmngToBeConfdAmt(self):
		del self._RmngToBeConfdAmt
		self._RmngToBeConfdAmt = None

	@property
	def RtrdConfdAmt(self):
		return self._RtrdConfdAmt

	@RtrdConfdAmt.setter
	def RtrdConfdAmt(self, value):
		self._RtrdConfdAmt = value if type(value) != auto else self.make_default("RtrdConfdAmt")

	@RtrdConfdAmt.deleter
	def RtrdConfdAmt(self):
		del self._RtrdConfdAmt
		self._RtrdConfdAmt = None

	@property
	def ConfdAmt(self):
		return self._ConfdAmt

	@ConfdAmt.setter
	def ConfdAmt(self, value):
		self._ConfdAmt = value if type(value) != auto else self.make_default("ConfdAmt")

	@ConfdAmt.deleter
	def ConfdAmt(self):
		del self._ConfdAmt
		self._ConfdAmt = None

	@property
	def PrevslyConfdAmt(self):
		return self._PrevslyConfdAmt

	@PrevslyConfdAmt.setter
	def PrevslyConfdAmt(self, value):
		self._PrevslyConfdAmt = value if type(value) != auto else self.make_default("PrevslyConfdAmt")

	@PrevslyConfdAmt.deleter
	def PrevslyConfdAmt(self):
		del self._PrevslyConfdAmt
		self._PrevslyConfdAmt = None

	@property
	def ConfdDt(self):
		return self._ConfdDt

	@ConfdDt.setter
	def ConfdDt(self, value):
		self._ConfdDt = value if type(value) != auto else self.make_default("ConfdDt")

	@ConfdDt.deleter
	def ConfdDt(self):
		del self._ConfdDt
		self._ConfdDt = None

	@property
	def RtrdConfdDt(self):
		return self._RtrdConfdDt

	@RtrdConfdDt.setter
	def RtrdConfdDt(self, value):
		self._RtrdConfdDt = value if type(value) != auto else self.make_default("RtrdConfdDt")

	@RtrdConfdDt.deleter
	def RtrdConfdDt(self):
		del self._RtrdConfdDt
		self._RtrdConfdDt = None

	@property
	def PrevslyConfdDt(self):
		return self._PrevslyConfdDt

	@PrevslyConfdDt.setter
	def PrevslyConfdDt(self, value):
		self._PrevslyConfdDt = value if type(value) != auto else self.make_default("PrevslyConfdDt")

	@PrevslyConfdDt.deleter
	def PrevslyConfdDt(self):
		del self._PrevslyConfdDt
		self._PrevslyConfdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmngToBeConfdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrdConfdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslyConfdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrdConfdDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslyConfdDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

