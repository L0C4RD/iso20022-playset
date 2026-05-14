# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPMemberObligationsReportV01 import CCPMemberObligationsReportV01

class AUTH_056_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPMmbOblgtnsRpt"]
		@property
		def CCPMmbOblgtnsRpt(self):
			return self._CCPMmbOblgtnsRpt

		@CCPMmbOblgtnsRpt.setter
		def CCPMmbOblgtnsRpt(self, value):
			self._CCPMmbOblgtnsRpt = value if type(value) != base_types.auto else self.make_default("CCPMmbOblgtnsRpt")

		@CCPMmbOblgtnsRpt.deleter
		def CCPMmbOblgtnsRpt(self):
			del self._CCPMmbOblgtnsRpt
			self._CCPMmbOblgtnsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPMmbOblgtnsRpt', type=CCPMemberObligationsReportV01, min=1, max=1, mutex_group=None, array=False),
		))