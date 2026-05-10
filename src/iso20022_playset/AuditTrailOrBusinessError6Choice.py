import base_types
import ErrorHandling5
import AuditTrail1

class AuditTrailOrBusinessError6Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_AudtTrl"]
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
	def AudtTrl(self):
		return self._AudtTrl

	@AudtTrl.setter
	def AudtTrl(self, value):
		self._AudtTrl = value if type(value) != auto else self.make_default("AudtTrl")

	@AudtTrl.deleter
	def AudtTrl(self):
		del self._AudtTrl
		self._AudtTrl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='AudtTrl', type=AuditTrail1, min=1, max=None, mutex_group=1, array=True),
	))

