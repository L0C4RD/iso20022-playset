# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForwardIntentToPayNotificationV02 import ForwardIntentToPayNotificationV02

class TSMT_045_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.045.001.02"
		_docname = "tsmt.045.001.02"

		__slots__ = ["_FwdInttToPayNtfctn"]
		@property
		def FwdInttToPayNtfctn(self):
			return self._FwdInttToPayNtfctn

		@FwdInttToPayNtfctn.setter
		def FwdInttToPayNtfctn(self, value):
			self._FwdInttToPayNtfctn = value if type(value) != base_types.auto else self.make_default("FwdInttToPayNtfctn")

		@FwdInttToPayNtfctn.deleter
		def FwdInttToPayNtfctn(self):
			del self._FwdInttToPayNtfctn
			self._FwdInttToPayNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FwdInttToPayNtfctn', type=ForwardIntentToPayNotificationV02, min=1, max=1, mutex_group=None, array=False),
		))