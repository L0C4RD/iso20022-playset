# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementCancellationRequestStatusAdviceV02 import IntraBalanceMovementCancellationRequestStatusAdviceV02

class CAMT_075_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.075.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_IntraBalMvmntCxlReqStsAdvc"]
		@property
		def IntraBalMvmntCxlReqStsAdvc(self):
			return self._IntraBalMvmntCxlReqStsAdvc

		@IntraBalMvmntCxlReqStsAdvc.setter
		def IntraBalMvmntCxlReqStsAdvc(self, value):
			self._IntraBalMvmntCxlReqStsAdvc = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntCxlReqStsAdvc")

		@IntraBalMvmntCxlReqStsAdvc.deleter
		def IntraBalMvmntCxlReqStsAdvc(self):
			del self._IntraBalMvmntCxlReqStsAdvc
			self._IntraBalMvmntCxlReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlReqStsAdvc', type=IntraBalanceMovementCancellationRequestStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))