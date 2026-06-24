# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementStatusAdvice002V07 import IntraPositionMovementStatusAdvice002V07

class SEMT_014_002_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.014.002.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_IntraPosMvmntStsAdvc"]
		@property
		def IntraPosMvmntStsAdvc(self):
			return self._IntraPosMvmntStsAdvc

		@IntraPosMvmntStsAdvc.setter
		def IntraPosMvmntStsAdvc(self, value):
			self._IntraPosMvmntStsAdvc = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntStsAdvc")

		@IntraPosMvmntStsAdvc.deleter
		def IntraPosMvmntStsAdvc(self):
			del self._IntraPosMvmntStsAdvc
			self._IntraPosMvmntStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntStsAdvc', type=IntraPositionMovementStatusAdvice002V07, min=1, max=1, mutex_group=None, array=False),
		))