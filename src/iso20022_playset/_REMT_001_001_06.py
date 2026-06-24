# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RemittanceAdviceV06 import RemittanceAdviceV06

class REMT_001_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:remt.001.001.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_RmtAdvc"]
		@property
		def RmtAdvc(self):
			return self._RmtAdvc

		@RmtAdvc.setter
		def RmtAdvc(self, value):
			self._RmtAdvc = value if type(value) != base_types.auto else self.make_default("RmtAdvc")

		@RmtAdvc.deleter
		def RmtAdvc(self):
			del self._RmtAdvc
			self._RmtAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RmtAdvc', type=RemittanceAdviceV06, min=1, max=1, mutex_group=None, array=False),
		))