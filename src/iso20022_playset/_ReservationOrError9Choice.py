# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import Reservation3

class ReservationOrError9Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_Rsvatn"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@property
	def Rsvatn(self):
		return self._Rsvatn

	@Rsvatn.setter
	def Rsvatn(self, value):
		self._Rsvatn = value if value is not None else base_types.UninitialisedField(self, 'Rsvatn', Reservation3, False)

	@Rsvatn.deleter
	def Rsvatn(self):
		del self._Rsvatn
		self._Rsvatn = base_types.UninitialisedField(self, 'Rsvatn', Reservation3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Rsvatn', type=Reservation3, min=0, max=1, mutex_group=1, array=False),
	))