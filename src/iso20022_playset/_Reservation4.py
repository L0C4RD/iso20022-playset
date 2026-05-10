from . import base_types
from ._Amount2Choice import Amount2Choice
from ._DateAndDateTime2Choice import DateAndDateTime2Choice

class Reservation4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_StartDtTm"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def StartDtTm(self):
		return self._StartDtTm

	@StartDtTm.setter
	def StartDtTm(self, value):
		self._StartDtTm = value if type(value) != base_types.auto else self.make_default("StartDtTm")

	@StartDtTm.deleter
	def StartDtTm(self):
		del self._StartDtTm
		self._StartDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

