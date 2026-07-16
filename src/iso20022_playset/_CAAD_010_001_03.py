# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomReportV03

class CAAD_010_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.010.001.03"
		_docname = "caad.010.001.03"

		__slots__ = ["_CstmRpt"]
		@property
		def CstmRpt(self):
			return self._CstmRpt

		@CstmRpt.setter
		def CstmRpt(self, value):
			self._CstmRpt = value if value is not None else base_types.UninitialisedField(self, 'CstmRpt', CustomReportV03, False)

		@CstmRpt.deleter
		def CstmRpt(self):
			del self._CstmRpt
			self._CstmRpt = base_types.UninitialisedField(self, 'CstmRpt', CustomReportV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmRpt', type=CustomReportV03, min=1, max=1, mutex_group=None, array=False),
		))