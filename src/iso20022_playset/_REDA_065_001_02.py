# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CalendarReportV02

class REDA_065_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02"
		_docname = "reda.065.001.02"

		__slots__ = ["_CalRpt"]
		@property
		def CalRpt(self):
			return self._CalRpt

		@CalRpt.setter
		def CalRpt(self, value):
			self._CalRpt = value if value is not None else base_types.UninitialisedField(self, 'CalRpt', CalendarReportV02, False)

		@CalRpt.deleter
		def CalRpt(self):
			del self._CalRpt
			self._CalRpt = base_types.UninitialisedField(self, 'CalRpt', CalendarReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CalRpt', type=CalendarReportV02, min=1, max=1, mutex_group=None, array=False),
		))