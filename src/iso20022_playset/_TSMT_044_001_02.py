# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntentToPayNotificationV02 import IntentToPayNotificationV02

class TSMT_044_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_InttToPayNtfctn"]
		@property
		def InttToPayNtfctn(self):
			return self._InttToPayNtfctn

		@InttToPayNtfctn.setter
		def InttToPayNtfctn(self, value):
			self._InttToPayNtfctn = value if type(value) != base_types.auto else self.make_default("InttToPayNtfctn")

		@InttToPayNtfctn.deleter
		def InttToPayNtfctn(self):
			del self._InttToPayNtfctn
			self._InttToPayNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InttToPayNtfctn', type=IntentToPayNotificationV02, min=1, max=1, mutex_group=None, array=False),
		))