import base_types
import LimitIdentification9
import LimitIdentification8

class LimitStructure3Choice(base_types._BaseFieldType):

	__slots__ = ["_AllCurLmts", "_CurLmtId"]
	@property
	def AllCurLmts(self):
		return self._AllCurLmts

	@AllCurLmts.setter
	def AllCurLmts(self, value):
		self._AllCurLmts = value if type(value) != auto else self.make_default("AllCurLmts")

	@AllCurLmts.deleter
	def AllCurLmts(self):
		del self._AllCurLmts
		self._AllCurLmts = None

	@property
	def CurLmtId(self):
		return self._CurLmtId

	@CurLmtId.setter
	def CurLmtId(self, value):
		self._CurLmtId = value if type(value) != auto else self.make_default("CurLmtId")

	@CurLmtId.deleter
	def CurLmtId(self):
		del self._CurLmtId
		self._CurLmtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllCurLmts', type=LimitIdentification9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CurLmtId', type=LimitIdentification8, min=0, max=1, mutex_group=1, array=False),
	))

