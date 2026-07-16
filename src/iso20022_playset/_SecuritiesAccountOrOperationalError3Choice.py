# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import SecuritiesAccountReport3

class SecuritiesAccountOrOperationalError3Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_SctiesAcctRpt"]
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
	def SctiesAcctRpt(self):
		return self._SctiesAcctRpt

	@SctiesAcctRpt.setter
	def SctiesAcctRpt(self, value):
		self._SctiesAcctRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctRpt', SecuritiesAccountReport3, True)

	@SctiesAcctRpt.deleter
	def SctiesAcctRpt(self):
		del self._SctiesAcctRpt
		self._SctiesAcctRpt = base_types.UninitialisedField(self, 'SctiesAcctRpt', SecuritiesAccountReport3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctiesAcctRpt', type=SecuritiesAccountReport3, min=1, max=None, mutex_group=1, array=True),
	))