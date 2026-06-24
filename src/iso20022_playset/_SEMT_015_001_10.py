# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementConfirmationV10 import IntraPositionMovementConfirmationV10

class SEMT_015_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.015.001.10"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_IntraPosMvmntConf"]
		@property
		def IntraPosMvmntConf(self):
			return self._IntraPosMvmntConf

		@IntraPosMvmntConf.setter
		def IntraPosMvmntConf(self, value):
			self._IntraPosMvmntConf = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntConf")

		@IntraPosMvmntConf.deleter
		def IntraPosMvmntConf(self):
			del self._IntraPosMvmntConf
			self._IntraPosMvmntConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntConf', type=IntraPositionMovementConfirmationV10, min=1, max=1, mutex_group=None, array=False),
		))