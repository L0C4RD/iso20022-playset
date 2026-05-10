from . import base_types
from .UUIDv4Identifier import UUIDv4Identifier
from .OriginalGroupInformation29 import OriginalGroupInformation29
from .Max35Text import Max35Text

class UnderlyingStatementEntry3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlStmtId", "_OrgnlGrpInf", "_OrgnlNtryId", "_OrgnlUETR"]
	@property
	def OrgnlStmtId(self):
		return self._OrgnlStmtId

	@OrgnlStmtId.setter
	def OrgnlStmtId(self, value):
		self._OrgnlStmtId = value if type(value) != base_types.auto else self.make_default("OrgnlStmtId")

	@OrgnlStmtId.deleter
	def OrgnlStmtId(self):
		del self._OrgnlStmtId
		self._OrgnlStmtId = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def OrgnlNtryId(self):
		return self._OrgnlNtryId

	@OrgnlNtryId.setter
	def OrgnlNtryId(self, value):
		self._OrgnlNtryId = value if type(value) != base_types.auto else self.make_default("OrgnlNtryId")

	@OrgnlNtryId.deleter
	def OrgnlNtryId(self):
		del self._OrgnlNtryId
		self._OrgnlNtryId = None

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != base_types.auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlStmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))

