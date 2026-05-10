from . import base_types
from ._DataModification1Code import DataModification1Code
from ._NewIssueAllocation2 import NewIssueAllocation2

class ModificationScope21(base_types._BaseFieldType):

	__slots__ = ["_IsseAllcn", "_ModScpIndctn"]
	@property
	def IsseAllcn(self):
		return self._IsseAllcn

	@IsseAllcn.setter
	def IsseAllcn(self, value):
		self._IsseAllcn = value if type(value) != base_types.auto else self.make_default("IsseAllcn")

	@IsseAllcn.deleter
	def IsseAllcn(self):
		del self._IsseAllcn
		self._IsseAllcn = None

	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if type(value) != base_types.auto else self.make_default("ModScpIndctn")

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IsseAllcn', type=NewIssueAllocation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))

