# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BaselineReSubmissionV05 import BaselineReSubmissionV05

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
			self._BaselnReSubmissn = value if type(value) != base_types.auto else self.make_default("BaselnReSubmissn")

		@BaselnReSubmissn.deleter
		def BaselnReSubmissn(self):
			del self._BaselnReSubmissn
			self._BaselnReSubmissn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BaselnReSubmissn', type=BaselineReSubmissionV05, min=1, max=1, mutex_group=None, array=False),
		))