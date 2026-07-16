# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountReport35
from . import ErrorHandling5

class AccountOrOperationalError6Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctRpt", "_OprlErr"]
	@property
	def AcctRpt(self):
		return self._AcctRpt

	@AcctRpt.setter
	def AcctRpt(self, value):
		self._AcctRpt = value if value is not None else base_types.UninitialisedField(self, 'AcctRpt', AccountReport35, True)

	@AcctRpt.deleter
	def AcctRpt(self):
		del self._AcctRpt
		self._AcctRpt = base_types.UninitialisedField(self, 'AcctRpt', AccountReport35, True)

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
		base_types.FieldEntry(name='AcctRpt', type=AccountReport35, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))