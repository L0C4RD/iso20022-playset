# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import IntraBalanceMovements4

class IntraBalanceOrOperationalError11Choice(base_types._BaseFieldType):

	__slots__ = ["_Mvmnts", "_OprlErr"]
	@property
	def Mvmnts(self):
		return self._Mvmnts

	@Mvmnts.setter
	def Mvmnts(self, value):
		self._Mvmnts = value if value is not None else base_types.UninitialisedField(self, 'Mvmnts', IntraBalanceMovements4, True)

	@Mvmnts.deleter
	def Mvmnts(self):
		del self._Mvmnts
		self._Mvmnts = base_types.UninitialisedField(self, 'Mvmnts', IntraBalanceMovements4, True)

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if value is not None else base_types.UninitialisedField(self, 'OprlErr', ErrorHandling5, True)

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = base_types.UninitialisedField(self, 'OprlErr', ErrorHandling5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mvmnts', type=IntraBalanceMovements4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))