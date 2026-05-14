# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CalendarReportV02 import CalendarReportV02

class REDA_065_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CalRpt"]
		@property
		def CalRpt(self):
			return self._CalRpt

		@CalRpt.setter
		def CalRpt(self, value):
			self._CalRpt = value if type(value) != base_types.auto else self.make_default("CalRpt")

		@CalRpt.deleter
		def CalRpt(self):
			del self._CalRpt
			self._CalRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CalRpt', type=CalendarReportV02, min=1, max=1, mutex_group=None, array=False),
		))