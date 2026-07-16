# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementCancellationRequestV02

class CAMT_074_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.074.001.02"
		_docname = "camt.074.001.02"

		__slots__ = ["_IntraBalMvmntCxlReq"]
		@property
		def IntraBalMvmntCxlReq(self):
			return self._IntraBalMvmntCxlReq

		@IntraBalMvmntCxlReq.setter
		def IntraBalMvmntCxlReq(self, value):
			self._IntraBalMvmntCxlReq = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntCxlReq', IntraBalanceMovementCancellationRequestV02, False)

		@IntraBalMvmntCxlReq.deleter
		def IntraBalMvmntCxlReq(self):
			del self._IntraBalMvmntCxlReq
			self._IntraBalMvmntCxlReq = base_types.UninitialisedField(self, 'IntraBalMvmntCxlReq', IntraBalanceMovementCancellationRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlReq', type=IntraBalanceMovementCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))