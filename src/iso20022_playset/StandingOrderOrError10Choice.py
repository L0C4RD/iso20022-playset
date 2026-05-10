from . import base_types
import ErrorHandling5
import StandingOrder11

class StandingOrderOrError10Choice(base_types._BaseFieldType):

	__slots__ = ["_StgOrdr", "_BizErr"]
	@property
	def StgOrdr(self):
		return self._StgOrdr

	@StgOrdr.setter
	def StgOrdr(self, value):
		self._StgOrdr = value if type(value) != auto else self.make_default("StgOrdr")

	@StgOrdr.deleter
	def StgOrdr(self):
		del self._StgOrdr
		self._StgOrdr = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StgOrdr', type=StandingOrder11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

