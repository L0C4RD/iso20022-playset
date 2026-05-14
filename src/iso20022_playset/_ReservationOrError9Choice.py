# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ErrorHandling5 import ErrorHandling5
from ._Reservation3 import Reservation3

class ReservationOrError9Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_Rsvatn"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	@property
	def Rsvatn(self):
		return self._Rsvatn

	@Rsvatn.setter
	def Rsvatn(self, value):
		self._Rsvatn = value if type(value) != base_types.auto else self.make_default("Rsvatn")

	@Rsvatn.deleter
	def Rsvatn(self):
		del self._Rsvatn
		self._Rsvatn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Rsvatn', type=Reservation3, min=0, max=1, mutex_group=1, array=False),
	))