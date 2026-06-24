# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementQueryResponseV02 import IntraBalanceMovementQueryResponseV02

class CAMT_079_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.079.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_IntraBalMvmntQryRspn"]
		@property
		def IntraBalMvmntQryRspn(self):
			return self._IntraBalMvmntQryRspn

		@IntraBalMvmntQryRspn.setter
		def IntraBalMvmntQryRspn(self, value):
			self._IntraBalMvmntQryRspn = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntQryRspn")

		@IntraBalMvmntQryRspn.deleter
		def IntraBalMvmntQryRspn(self):
			del self._IntraBalMvmntQryRspn
			self._IntraBalMvmntQryRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntQryRspn', type=IntraBalanceMovementQueryResponseV02, min=1, max=1, mutex_group=None, array=False),
		))