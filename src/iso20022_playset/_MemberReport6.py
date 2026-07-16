# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MemberIdentification3Choice
from . import MemberReportOrError8Choice

class MemberReport6(base_types._BaseFieldType):

	__slots__ = ["_MmbId", "_MmbOrErr"]
	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if value is not None else base_types.UninitialisedField(self, 'MmbId', MemberIdentification3Choice, False)

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = base_types.UninitialisedField(self, 'MmbId', MemberIdentification3Choice, False)

	@property
	def MmbOrErr(self):
		return self._MmbOrErr

	@MmbOrErr.setter
	def MmbOrErr(self, value):
		self._MmbOrErr = value if value is not None else base_types.UninitialisedField(self, 'MmbOrErr', MemberReportOrError8Choice, False)

	@MmbOrErr.deleter
	def MmbOrErr(self):
		del self._MmbOrErr
		self._MmbOrErr = base_types.UninitialisedField(self, 'MmbOrErr', MemberReportOrError8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MmbId', type=MemberIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbOrErr', type=MemberReportOrError8Choice, min=1, max=1, mutex_group=None, array=False),
	))