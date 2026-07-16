# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyReportV02

class REDA_017_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.017.001.02"
		_docname = "reda.017.001.02"

		__slots__ = ["_PtyRpt"]
		@property
		def PtyRpt(self):
			return self._PtyRpt

		@PtyRpt.setter
		def PtyRpt(self, value):
			self._PtyRpt = value if value is not None else base_types.UninitialisedField(self, 'PtyRpt', PartyReportV02, False)

		@PtyRpt.deleter
		def PtyRpt(self):
			del self._PtyRpt
			self._PtyRpt = base_types.UninitialisedField(self, 'PtyRpt', PartyReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRpt', type=PartyReportV02, min=1, max=1, mutex_group=None, array=False),
		))