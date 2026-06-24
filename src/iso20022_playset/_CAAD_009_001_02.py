# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdministrativeResponseV02 import AdministrativeResponseV02

class CAAD_009_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caad.009.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AdmstvRspn"]
		@property
		def AdmstvRspn(self):
			return self._AdmstvRspn

		@AdmstvRspn.setter
		def AdmstvRspn(self, value):
			self._AdmstvRspn = value if type(value) != base_types.auto else self.make_default("AdmstvRspn")

		@AdmstvRspn.deleter
		def AdmstvRspn(self):
			del self._AdmstvRspn
			self._AdmstvRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdmstvRspn', type=AdministrativeResponseV02, min=1, max=1, mutex_group=None, array=False),
		))