from . import base_types
import MemberIdentification3Choice
import MemberReportOrError8Choice

class MemberReport6(base_types._BaseFieldType):

	__slots__ = ["_MmbId", "_MmbOrErr"]
	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if type(value) != auto else self.make_default("MmbId")

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = None

	@property
	def MmbOrErr(self):
		return self._MmbOrErr

	@MmbOrErr.setter
	def MmbOrErr(self, value):
		self._MmbOrErr = value if type(value) != auto else self.make_default("MmbOrErr")

	@MmbOrErr.deleter
	def MmbOrErr(self):
		del self._MmbOrErr
		self._MmbOrErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MmbId', type=MemberIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbOrErr', type=MemberReportOrError8Choice, min=1, max=1, mutex_group=None, array=False),
	))

