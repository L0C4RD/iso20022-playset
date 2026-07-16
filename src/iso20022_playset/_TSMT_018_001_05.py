# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FullPushThroughReportV05

class TSMT_018_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.018.001.05"
		_docname = "tsmt.018.001.05"

		__slots__ = ["_FullPushThrghRpt"]
		@property
		def FullPushThrghRpt(self):
			return self._FullPushThrghRpt

		@FullPushThrghRpt.setter
		def FullPushThrghRpt(self, value):
			self._FullPushThrghRpt = value if value is not None else base_types.UninitialisedField(self, 'FullPushThrghRpt', FullPushThroughReportV05, False)

		@FullPushThrghRpt.deleter
		def FullPushThrghRpt(self):
			del self._FullPushThrghRpt
			self._FullPushThrghRpt = base_types.UninitialisedField(self, 'FullPushThrghRpt', FullPushThroughReportV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FullPushThrghRpt', type=FullPushThroughReportV05, min=1, max=1, mutex_group=None, array=False),
		))