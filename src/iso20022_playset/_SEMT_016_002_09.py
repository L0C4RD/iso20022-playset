# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementPostingReport002V09 import IntraPositionMovementPostingReport002V09

class SEMT_016_002_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.016.002.09"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_IntraPosMvmntPstngRpt"]
		@property
		def IntraPosMvmntPstngRpt(self):
			return self._IntraPosMvmntPstngRpt

		@IntraPosMvmntPstngRpt.setter
		def IntraPosMvmntPstngRpt(self, value):
			self._IntraPosMvmntPstngRpt = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntPstngRpt")

		@IntraPosMvmntPstngRpt.deleter
		def IntraPosMvmntPstngRpt(self):
			del self._IntraPosMvmntPstngRpt
			self._IntraPosMvmntPstngRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntPstngRpt', type=IntraPositionMovementPostingReport002V09, min=1, max=1, mutex_group=None, array=False),
		))