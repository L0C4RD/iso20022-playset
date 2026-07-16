# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import PartyReport4

class PartyOrOperationalError4Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_PtyRpt"]
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

	@property
	def PtyRpt(self):
		return self._PtyRpt

	@PtyRpt.setter
	def PtyRpt(self, value):
		self._PtyRpt = value if value is not None else base_types.UninitialisedField(self, 'PtyRpt', PartyReport4, True)

	@PtyRpt.deleter
	def PtyRpt(self):
		del self._PtyRpt
		self._PtyRpt = base_types.UninitialisedField(self, 'PtyRpt', PartyReport4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='PtyRpt', type=PartyReport4, min=1, max=None, mutex_group=1, array=True),
	))