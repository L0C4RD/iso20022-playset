# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DateAndDateTime2Choice

class TrackerData8(base_types._BaseFieldType):

	__slots__ = ["_ConfdAmt", "_ConfdDt", "_PrevslyConfdAmt", "_PrevslyConfdDt", "_RmngToBeConfdAmt", "_RtrdConfdAmt", "_RtrdConfdDt"]
	@property
	def ConfdAmt(self):
		return self._ConfdAmt

	@ConfdAmt.setter
	def ConfdAmt(self, value):
		self._ConfdAmt = value if value is not None else base_types.UninitialisedField(self, 'ConfdAmt', ActiveCurrencyAndAmount, False)

	@ConfdAmt.deleter
	def ConfdAmt(self):
		del self._ConfdAmt
		self._ConfdAmt = base_types.UninitialisedField(self, 'ConfdAmt', ActiveCurrencyAndAmount, False)

	@property
	def ConfdDt(self):
		return self._ConfdDt

	@ConfdDt.setter
	def ConfdDt(self, value):
		self._ConfdDt = value if value is not None else base_types.UninitialisedField(self, 'ConfdDt', DateAndDateTime2Choice, False)

	@ConfdDt.deleter
	def ConfdDt(self):
		del self._ConfdDt
		self._ConfdDt = base_types.UninitialisedField(self, 'ConfdDt', DateAndDateTime2Choice, False)

	@property
	def PrevslyConfdAmt(self):
		return self._PrevslyConfdAmt

	@PrevslyConfdAmt.setter
	def PrevslyConfdAmt(self, value):
		self._PrevslyConfdAmt = value if value is not None else base_types.UninitialisedField(self, 'PrevslyConfdAmt', ActiveCurrencyAndAmount, False)

	@PrevslyConfdAmt.deleter
	def PrevslyConfdAmt(self):
		del self._PrevslyConfdAmt
		self._PrevslyConfdAmt = base_types.UninitialisedField(self, 'PrevslyConfdAmt', ActiveCurrencyAndAmount, False)

	@property
	def PrevslyConfdDt(self):
		return self._PrevslyConfdDt

	@PrevslyConfdDt.setter
	def PrevslyConfdDt(self, value):
		self._PrevslyConfdDt = value if value is not None else base_types.UninitialisedField(self, 'PrevslyConfdDt', DateAndDateTime2Choice, False)

	@PrevslyConfdDt.deleter
	def PrevslyConfdDt(self):
		del self._PrevslyConfdDt
		self._PrevslyConfdDt = base_types.UninitialisedField(self, 'PrevslyConfdDt', DateAndDateTime2Choice, False)

	@property
	def RmngToBeConfdAmt(self):
		return self._RmngToBeConfdAmt

	@RmngToBeConfdAmt.setter
	def RmngToBeConfdAmt(self, value):
		self._RmngToBeConfdAmt = value if value is not None else base_types.UninitialisedField(self, 'RmngToBeConfdAmt', ActiveCurrencyAndAmount, False)

	@RmngToBeConfdAmt.deleter
	def RmngToBeConfdAmt(self):
		del self._RmngToBeConfdAmt
		self._RmngToBeConfdAmt = base_types.UninitialisedField(self, 'RmngToBeConfdAmt', ActiveCurrencyAndAmount, False)

	@property
	def RtrdConfdAmt(self):
		return self._RtrdConfdAmt

	@RtrdConfdAmt.setter
	def RtrdConfdAmt(self, value):
		self._RtrdConfdAmt = value if value is not None else base_types.UninitialisedField(self, 'RtrdConfdAmt', ActiveCurrencyAndAmount, False)

	@RtrdConfdAmt.deleter
	def RtrdConfdAmt(self):
		del self._RtrdConfdAmt
		self._RtrdConfdAmt = base_types.UninitialisedField(self, 'RtrdConfdAmt', ActiveCurrencyAndAmount, False)

	@property
	def RtrdConfdDt(self):
		return self._RtrdConfdDt

	@RtrdConfdDt.setter
	def RtrdConfdDt(self, value):
		self._RtrdConfdDt = value if value is not None else base_types.UninitialisedField(self, 'RtrdConfdDt', DateAndDateTime2Choice, False)

	@RtrdConfdDt.deleter
	def RtrdConfdDt(self):
		del self._RtrdConfdDt
		self._RtrdConfdDt = base_types.UninitialisedField(self, 'RtrdConfdDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslyConfdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslyConfdDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeConfdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrdConfdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrdConfdDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))