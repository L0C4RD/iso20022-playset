# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMTransferRequestV02 import ATMTransferRequestV02

class CATP_016_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02"
		_docname = "catp.016.001.02"

		__slots__ = ["_ATMTrfReq"]
		@property
		def ATMTrfReq(self):
			return self._ATMTrfReq

		@ATMTrfReq.setter
		def ATMTrfReq(self, value):
			self._ATMTrfReq = value if type(value) != base_types.auto else self.make_default("ATMTrfReq")

		@ATMTrfReq.deleter
		def ATMTrfReq(self):
			del self._ATMTrfReq
			self._ATMTrfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMTrfReq', type=ATMTransferRequestV02, min=1, max=1, mutex_group=None, array=False),
		))