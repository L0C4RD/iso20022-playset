# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataModification1Code
from . import NewIssueAllocation2

class ModificationScope21(base_types._BaseFieldType):

	__slots__ = ["_IsseAllcn", "_ModScpIndctn"]
	@property
	def IsseAllcn(self):
		return self._IsseAllcn

	@IsseAllcn.setter
	def IsseAllcn(self, value):
		self._IsseAllcn = value if value is not None else base_types.UninitialisedField(self, 'IsseAllcn', NewIssueAllocation2, False)

	@IsseAllcn.deleter
	def IsseAllcn(self):
		del self._IsseAllcn
		self._IsseAllcn = base_types.UninitialisedField(self, 'IsseAllcn', NewIssueAllocation2, False)

	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if value is not None else base_types.UninitialisedField(self, 'ModScpIndctn', DataModification1Code, False)

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = base_types.UninitialisedField(self, 'ModScpIndctn', DataModification1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IsseAllcn', type=NewIssueAllocation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))