# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorReportV03

class TSMT_016_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03"
		_docname = "tsmt.016.001.03"

		__slots__ = ["_ErrRpt"]
		@property
		def ErrRpt(self):
			return self._ErrRpt

		@ErrRpt.setter
		def ErrRpt(self, value):
			self._ErrRpt = value if value is not None else base_types.UninitialisedField(self, 'ErrRpt', ErrorReportV03, False)

		@ErrRpt.deleter
		def ErrRpt(self):
			del self._ErrRpt
			self._ErrRpt = base_types.UninitialisedField(self, 'ErrRpt', ErrorReportV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ErrRpt', type=ErrorReportV03, min=1, max=1, mutex_group=None, array=False),
		))