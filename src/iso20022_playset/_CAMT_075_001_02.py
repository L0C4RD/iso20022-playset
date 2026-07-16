# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementCancellationRequestStatusAdviceV02

class CAMT_075_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.075.001.02"
		_docname = "camt.075.001.02"

		__slots__ = ["_IntraBalMvmntCxlReqStsAdvc"]
		@property
		def IntraBalMvmntCxlReqStsAdvc(self):
			return self._IntraBalMvmntCxlReqStsAdvc

		@IntraBalMvmntCxlReqStsAdvc.setter
		def IntraBalMvmntCxlReqStsAdvc(self, value):
			self._IntraBalMvmntCxlReqStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntCxlReqStsAdvc', IntraBalanceMovementCancellationRequestStatusAdviceV02, False)

		@IntraBalMvmntCxlReqStsAdvc.deleter
		def IntraBalMvmntCxlReqStsAdvc(self):
			del self._IntraBalMvmntCxlReqStsAdvc
			self._IntraBalMvmntCxlReqStsAdvc = base_types.UninitialisedField(self, 'IntraBalMvmntCxlReqStsAdvc', IntraBalanceMovementCancellationRequestStatusAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlReqStsAdvc', type=IntraBalanceMovementCancellationRequestStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))