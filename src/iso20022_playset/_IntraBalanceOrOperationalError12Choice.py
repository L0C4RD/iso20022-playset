# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import IntraBalanceModification7

class IntraBalanceOrOperationalError12Choice(base_types._BaseFieldType):

	__slots__ = ["_Mods", "_OprlErr"]
	@property
	def Mods(self):
		return self._Mods

	@Mods.setter
	def Mods(self, value):
		self._Mods = value if value is not None else base_types.UninitialisedField(self, 'Mods', IntraBalanceModification7, True)

	@Mods.deleter
	def Mods(self):
		del self._Mods
		self._Mods = base_types.UninitialisedField(self, 'Mods', IntraBalanceModification7, True)

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
		base_types.FieldEntry(name='Mods', type=IntraBalanceModification7, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))