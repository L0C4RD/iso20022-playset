import base_types
import Max35Text
import OriginalGroupInformation29
import UUIDv4Identifier

class UnderlyingStatementEntry3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlUETR", "_OrgnlNtryId", "_OrgnlGrpInf", "_OrgnlStmtId"]
	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	@property
	def OrgnlNtryId(self):
		return self._OrgnlNtryId

	@OrgnlNtryId.setter
	def OrgnlNtryId(self, value):
		self._OrgnlNtryId = value if type(value) != auto else self.make_default("OrgnlNtryId")

	@OrgnlNtryId.deleter
	def OrgnlNtryId(self):
		del self._OrgnlNtryId
		self._OrgnlNtryId = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def OrgnlStmtId(self):
		return self._OrgnlStmtId

	@OrgnlStmtId.setter
	def OrgnlStmtId(self, value):
		self._OrgnlStmtId = value if type(value) != auto else self.make_default("OrgnlStmtId")

	@OrgnlStmtId.deleter
	def OrgnlStmtId(self):
		del self._OrgnlStmtId
		self._OrgnlStmtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlStmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

