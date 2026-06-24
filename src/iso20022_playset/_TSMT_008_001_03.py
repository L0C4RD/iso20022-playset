# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmendmentRejectionNotificationV03 import AmendmentRejectionNotificationV03

class TSMT_008_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AmdmntRjctnNtfctn"]
		@property
		def AmdmntRjctnNtfctn(self):
			return self._AmdmntRjctnNtfctn

		@AmdmntRjctnNtfctn.setter
		def AmdmntRjctnNtfctn(self, value):
			self._AmdmntRjctnNtfctn = value if type(value) != base_types.auto else self.make_default("AmdmntRjctnNtfctn")

		@AmdmntRjctnNtfctn.deleter
		def AmdmntRjctnNtfctn(self):
			del self._AmdmntRjctnNtfctn
			self._AmdmntRjctnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntRjctnNtfctn', type=AmendmentRejectionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))