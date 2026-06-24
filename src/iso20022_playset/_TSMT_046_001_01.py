# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntentToPayReportV01 import IntentToPayReportV01

class TSMT_046_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_InttToPayRpt"]
		@property
		def InttToPayRpt(self):
			return self._InttToPayRpt

		@InttToPayRpt.setter
		def InttToPayRpt(self, value):
			self._InttToPayRpt = value if type(value) != base_types.auto else self.make_default("InttToPayRpt")

		@InttToPayRpt.deleter
		def InttToPayRpt(self):
			del self._InttToPayRpt
			self._InttToPayRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InttToPayRpt', type=IntentToPayReportV01, min=1, max=1, mutex_group=None, array=False),
		))