# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Quantity51Choice import Quantity51Choice
from ._RejectedStatus64Choice import RejectedStatus64Choice

class RejectedStatus15(base_types._BaseFieldType):

	__slots__ = ["_RjctdQty", "_RjctdRsn"]
	@property
	def RjctdQty(self):
		return self._RjctdQty

	@RjctdQty.setter
	def RjctdQty(self, value):
		self._RjctdQty = value if type(value) != base_types.auto else self.make_default("RjctdQty")

	@RjctdQty.deleter
	def RjctdQty(self):
		del self._RjctdQty
		self._RjctdQty = None

	@property
	def RjctdRsn(self):
		return self._RjctdRsn

	@RjctdRsn.setter
	def RjctdRsn(self, value):
		self._RjctdRsn = value if type(value) != base_types.auto else self.make_default("RjctdRsn")

	@RjctdRsn.deleter
	def RjctdRsn(self):
		del self._RjctdRsn
		self._RjctdRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctdQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdRsn', type=RejectedStatus64Choice, min=1, max=1, mutex_group=None, array=False),
	))