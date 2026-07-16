# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaselineReportV04

class TSMT_011_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04"
		_docname = "tsmt.011.001.04"

		__slots__ = ["_BaselnRpt"]
		@property
		def BaselnRpt(self):
			return self._BaselnRpt

		@BaselnRpt.setter
		def BaselnRpt(self, value):
			self._BaselnRpt = value if value is not None else base_types.UninitialisedField(self, 'BaselnRpt', BaselineReportV04, False)

		@BaselnRpt.deleter
		def BaselnRpt(self):
			del self._BaselnRpt
			self._BaselnRpt = base_types.UninitialisedField(self, 'BaselnRpt', BaselineReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BaselnRpt', type=BaselineReportV04, min=1, max=1, mutex_group=None, array=False),
		))