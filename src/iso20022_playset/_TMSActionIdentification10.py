# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataSetIdentification11
from . import TerminalManagementAction5Code

class TMSActionIdentification10(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_DataSetId"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction5Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction5Code, False)

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if value is not None else base_types.UninitialisedField(self, 'DataSetId', DataSetIdentification11, False)

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = base_types.UninitialisedField(self, 'DataSetId', DataSetIdentification11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification11, min=0, max=1, mutex_group=None, array=False),
	))