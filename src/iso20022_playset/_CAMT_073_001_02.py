# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementModificationRequestStatusAdviceV02 import IntraBalanceMovementModificationRequestStatusAdviceV02

class CAMT_073_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.073.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_IntraBalMvmntModReqStsAdvc"]
		@property
		def IntraBalMvmntModReqStsAdvc(self):
			return self._IntraBalMvmntModReqStsAdvc

		@IntraBalMvmntModReqStsAdvc.setter
		def IntraBalMvmntModReqStsAdvc(self, value):
			self._IntraBalMvmntModReqStsAdvc = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntModReqStsAdvc")

		@IntraBalMvmntModReqStsAdvc.deleter
		def IntraBalMvmntModReqStsAdvc(self):
			del self._IntraBalMvmntModReqStsAdvc
			self._IntraBalMvmntModReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModReqStsAdvc', type=IntraBalanceMovementModificationRequestStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))