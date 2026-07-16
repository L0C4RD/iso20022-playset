# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntentToPayReportV01

class TSMT_046_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01"
		_docname = "tsmt.046.001.01"

		__slots__ = ["_InttToPayRpt"]
		@property
		def InttToPayRpt(self):
			return self._InttToPayRpt

		@InttToPayRpt.setter
		def InttToPayRpt(self, value):
			self._InttToPayRpt = value if value is not None else base_types.UninitialisedField(self, 'InttToPayRpt', IntentToPayReportV01, False)

		@InttToPayRpt.deleter
		def InttToPayRpt(self):
			del self._InttToPayRpt
			self._InttToPayRpt = base_types.UninitialisedField(self, 'InttToPayRpt', IntentToPayReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InttToPayRpt', type=IntentToPayReportV01, min=1, max=1, mutex_group=None, array=False),
		))