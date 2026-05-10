from . import base_types
import ErrorHandling5
import SecurityIdentification39

class BusinessError4(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_FinInstrmId"]
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

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=1, max=1, mutex_group=None, array=False),
	))

