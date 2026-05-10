from . import base_types
import LimitIdentification8
import LimitOrError4Choice

class LimitReport8(base_types._BaseFieldType):

	__slots__ = ["_LmtOrErr", "_LmtId"]
	@property
	def LmtOrErr(self):
		return self._LmtOrErr

	@LmtOrErr.setter
	def LmtOrErr(self, value):
		self._LmtOrErr = value if type(value) != auto else self.make_default("LmtOrErr")

	@LmtOrErr.deleter
	def LmtOrErr(self):
		del self._LmtOrErr
		self._LmtOrErr = None

	@property
	def LmtId(self):
		return self._LmtId

	@LmtId.setter
	def LmtId(self, value):
		self._LmtId = value if type(value) != auto else self.make_default("LmtId")

	@LmtId.deleter
	def LmtId(self):
		del self._LmtId
		self._LmtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtOrErr', type=LimitOrError4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtId', type=LimitIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

