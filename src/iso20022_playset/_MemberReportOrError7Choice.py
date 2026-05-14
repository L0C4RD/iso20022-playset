# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ErrorHandling3 import ErrorHandling3
from ._MemberReport6 import MemberReport6

class MemberReportOrError7Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_Rpt"]
	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if type(value) != base_types.auto else self.make_default("Rpt")

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling3, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Rpt', type=MemberReport6, min=1, max=None, mutex_group=1, array=True),
	))