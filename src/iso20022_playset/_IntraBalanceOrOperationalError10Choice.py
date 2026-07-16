# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import IntraBalanceCancellation7

class IntraBalanceOrOperationalError10Choice(base_types._BaseFieldType):

	__slots__ = ["_Cxls", "_OprlErr"]
	@property
	def Cxls(self):
		return self._Cxls

	@Cxls.setter
	def Cxls(self, value):
		self._Cxls = value if value is not None else base_types.UninitialisedField(self, 'Cxls', IntraBalanceCancellation7, True)

	@Cxls.deleter
	def Cxls(self):
		del self._Cxls
		self._Cxls = base_types.UninitialisedField(self, 'Cxls', IntraBalanceCancellation7, True)

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
		base_types.FieldEntry(name='Cxls', type=IntraBalanceCancellation7, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))