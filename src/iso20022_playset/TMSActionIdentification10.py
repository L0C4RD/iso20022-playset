from . import base_types
from .DataSetIdentification11 import DataSetIdentification11
from .TerminalManagementAction5Code import TerminalManagementAction5Code

class TMSActionIdentification10(base_types._BaseFieldType):

	__slots__ = ["_DataSetId", "_ActnTp"]
	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction5Code, min=1, max=1, mutex_group=None, array=False),
	))

