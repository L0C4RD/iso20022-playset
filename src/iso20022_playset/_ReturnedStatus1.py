# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Quantity51Choice
from . import ReturnedStatus2Choice

class ReturnedStatus1(base_types._BaseFieldType):

	__slots__ = ["_RtrdQty", "_RtrdRsn"]
	@property
	def RtrdQty(self):
		return self._RtrdQty

	@RtrdQty.setter
	def RtrdQty(self, value):
		self._RtrdQty = value if value is not None else base_types.UninitialisedField(self, 'RtrdQty', Quantity51Choice, False)

	@RtrdQty.deleter
	def RtrdQty(self):
		del self._RtrdQty
		self._RtrdQty = base_types.UninitialisedField(self, 'RtrdQty', Quantity51Choice, False)

	@property
	def RtrdRsn(self):
		return self._RtrdRsn

	@RtrdRsn.setter
	def RtrdRsn(self, value):
		self._RtrdRsn = value if value is not None else base_types.UninitialisedField(self, 'RtrdRsn', ReturnedStatus2Choice, False)

	@RtrdRsn.deleter
	def RtrdRsn(self):
		del self._RtrdRsn
		self._RtrdRsn = base_types.UninitialisedField(self, 'RtrdRsn', ReturnedStatus2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RtrdQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrdRsn', type=ReturnedStatus2Choice, min=1, max=1, mutex_group=None, array=False),
	))