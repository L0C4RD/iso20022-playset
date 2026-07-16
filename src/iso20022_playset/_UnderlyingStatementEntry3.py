# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import OriginalGroupInformation29
from . import UUIDv4Identifier

class UnderlyingStatementEntry3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlGrpInf", "_OrgnlNtryId", "_OrgnlStmtId", "_OrgnlUETR"]
	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation29, False)

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation29, False)

	@property
	def OrgnlNtryId(self):
		return self._OrgnlNtryId

	@OrgnlNtryId.setter
	def OrgnlNtryId(self, value):
		self._OrgnlNtryId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNtryId', Max35Text, False)

	@OrgnlNtryId.deleter
	def OrgnlNtryId(self):
		del self._OrgnlNtryId
		self._OrgnlNtryId = base_types.UninitialisedField(self, 'OrgnlNtryId', Max35Text, False)

	@property
	def OrgnlStmtId(self):
		return self._OrgnlStmtId

	@OrgnlStmtId.setter
	def OrgnlStmtId(self, value):
		self._OrgnlStmtId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlStmtId', Max35Text, False)

	@OrgnlStmtId.deleter
	def OrgnlStmtId(self):
		del self._OrgnlStmtId
		self._OrgnlStmtId = base_types.UninitialisedField(self, 'OrgnlStmtId', Max35Text, False)

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if value is not None else base_types.UninitialisedField(self, 'OrgnlUETR', UUIDv4Identifier, False)

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = base_types.UninitialisedField(self, 'OrgnlUETR', UUIDv4Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlStmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))