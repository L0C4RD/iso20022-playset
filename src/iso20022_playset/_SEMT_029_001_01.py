# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementQueryResponseV01 import IntraPositionMovementQueryResponseV01

class SEMT_029_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.029.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_IntraPosMvmntQryRspn"]
		@property
		def IntraPosMvmntQryRspn(self):
			return self._IntraPosMvmntQryRspn

		@IntraPosMvmntQryRspn.setter
		def IntraPosMvmntQryRspn(self, value):
			self._IntraPosMvmntQryRspn = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntQryRspn")

		@IntraPosMvmntQryRspn.deleter
		def IntraPosMvmntQryRspn(self):
			del self._IntraPosMvmntQryRspn
			self._IntraPosMvmntQryRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntQryRspn', type=IntraPositionMovementQueryResponseV01, min=1, max=1, mutex_group=None, array=False),
		))