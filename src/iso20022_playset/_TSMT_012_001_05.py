# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaselineReSubmissionV05

class TSMT_012_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.012.001.05"
		_docname = "tsmt.012.001.05"

		__slots__ = ["_BaselnReSubmissn"]
		@property
		def BaselnReSubmissn(self):
			return self._BaselnReSubmissn

		@BaselnReSubmissn.setter
		def BaselnReSubmissn(self, value):
			self._BaselnReSubmissn = value if value is not None else base_types.UninitialisedField(self, 'BaselnReSubmissn', BaselineReSubmissionV05, False)

		@BaselnReSubmissn.deleter
		def BaselnReSubmissn(self):
			del self._BaselnReSubmissn
			self._BaselnReSubmissn = base_types.UninitialisedField(self, 'BaselnReSubmissn', BaselineReSubmissionV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BaselnReSubmissn', type=BaselineReSubmissionV05, min=1, max=1, mutex_group=None, array=False),
		))