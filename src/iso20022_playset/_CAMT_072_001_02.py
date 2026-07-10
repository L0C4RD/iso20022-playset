# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementModificationRequestV02 import IntraBalanceMovementModificationRequestV02

class CAMT_072_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.072.001.02"
		_docname = "camt.072.001.02"

		__slots__ = ["_IntraBalMvmntModReq"]
		@property
		def IntraBalMvmntModReq(self):
			return self._IntraBalMvmntModReq

		@IntraBalMvmntModReq.setter
		def IntraBalMvmntModReq(self, value):
			self._IntraBalMvmntModReq = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntModReq")

		@IntraBalMvmntModReq.deleter
		def IntraBalMvmntModReq(self):
			del self._IntraBalMvmntModReq
			self._IntraBalMvmntModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModReq', type=IntraBalanceMovementModificationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))