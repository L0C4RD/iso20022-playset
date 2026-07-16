# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementModificationRequestStatusAdviceV02

class CAMT_073_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.073.001.02"
		_docname = "camt.073.001.02"

		__slots__ = ["_IntraBalMvmntModReqStsAdvc"]
		@property
		def IntraBalMvmntModReqStsAdvc(self):
			return self._IntraBalMvmntModReqStsAdvc

		@IntraBalMvmntModReqStsAdvc.setter
		def IntraBalMvmntModReqStsAdvc(self, value):
			self._IntraBalMvmntModReqStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntModReqStsAdvc', IntraBalanceMovementModificationRequestStatusAdviceV02, False)

		@IntraBalMvmntModReqStsAdvc.deleter
		def IntraBalMvmntModReqStsAdvc(self):
			del self._IntraBalMvmntModReqStsAdvc
			self._IntraBalMvmntModReqStsAdvc = base_types.UninitialisedField(self, 'IntraBalMvmntModReqStsAdvc', IntraBalanceMovementModificationRequestStatusAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModReqStsAdvc', type=IntraBalanceMovementModificationRequestStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))