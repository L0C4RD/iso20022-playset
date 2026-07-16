# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeltaReportV03

class TSMT_015_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03"
		_docname = "tsmt.015.001.03"

		__slots__ = ["_DltaRpt"]
		@property
		def DltaRpt(self):
			return self._DltaRpt

		@DltaRpt.setter
		def DltaRpt(self, value):
			self._DltaRpt = value if value is not None else base_types.UninitialisedField(self, 'DltaRpt', DeltaReportV03, False)

		@DltaRpt.deleter
		def DltaRpt(self):
			del self._DltaRpt
			self._DltaRpt = base_types.UninitialisedField(self, 'DltaRpt', DeltaReportV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DltaRpt', type=DeltaReportV03, min=1, max=1, mutex_group=None, array=False),
		))