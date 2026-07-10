# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InitialBaselineSubmissionV05 import InitialBaselineSubmissionV05

class TSMT_019_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05"
		_docname = "tsmt.019.001.05"

		__slots__ = ["_InitlBaselnSubmissn"]
		@property
		def InitlBaselnSubmissn(self):
			return self._InitlBaselnSubmissn

		@InitlBaselnSubmissn.setter
		def InitlBaselnSubmissn(self, value):
			self._InitlBaselnSubmissn = value if type(value) != base_types.auto else self.make_default("InitlBaselnSubmissn")

		@InitlBaselnSubmissn.deleter
		def InitlBaselnSubmissn(self):
			del self._InitlBaselnSubmissn
			self._InitlBaselnSubmissn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InitlBaselnSubmissn', type=InitialBaselineSubmissionV05, min=1, max=1, mutex_group=None, array=False),
		))