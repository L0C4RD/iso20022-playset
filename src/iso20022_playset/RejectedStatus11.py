from . import base_types
import RejectedStatus56Choice
import Quantity51Choice

class RejectedStatus11(base_types._BaseFieldType):

	__slots__ = ["_RjctdRsn", "_RjctdQty"]
	@property
	def RjctdRsn(self):
		return self._RjctdRsn

	@RjctdRsn.setter
	def RjctdRsn(self, value):
		self._RjctdRsn = value if type(value) != auto else self.make_default("RjctdRsn")

	@RjctdRsn.deleter
	def RjctdRsn(self):
		del self._RjctdRsn
		self._RjctdRsn = None

	@property
	def RjctdQty(self):
		return self._RjctdQty

	@RjctdQty.setter
	def RjctdQty(self, value):
		self._RjctdQty = value if type(value) != auto else self.make_default("RjctdQty")

	@RjctdQty.deleter
	def RjctdQty(self):
		del self._RjctdQty
		self._RjctdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctdRsn', type=RejectedStatus56Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
	))

