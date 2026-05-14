# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ErrorHandling5 import ErrorHandling5
from ._IntraBalanceMovements4 import IntraBalanceMovements4

class IntraBalanceOrOperationalError11Choice(base_types._BaseFieldType):

	__slots__ = ["_Mvmnts", "_OprlErr"]
	@property
	def Mvmnts(self):
		return self._Mvmnts

	@Mvmnts.setter
	def Mvmnts(self, value):
		self._Mvmnts = value if type(value) != base_types.auto else self.make_default("Mvmnts")

	@Mvmnts.deleter
	def Mvmnts(self):
		del self._Mvmnts
		self._Mvmnts = None

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mvmnts', type=IntraBalanceMovements4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))