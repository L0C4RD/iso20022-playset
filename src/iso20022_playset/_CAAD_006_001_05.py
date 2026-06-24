# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReconciliationResponseV05 import ReconciliationResponseV05

class CAAD_006_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caad.006.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_RcncltnRspn"]
		@property
		def RcncltnRspn(self):
			return self._RcncltnRspn

		@RcncltnRspn.setter
		def RcncltnRspn(self, value):
			self._RcncltnRspn = value if type(value) != base_types.auto else self.make_default("RcncltnRspn")

		@RcncltnRspn.deleter
		def RcncltnRspn(self):
			del self._RcncltnRspn
			self._RcncltnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RcncltnRspn', type=ReconciliationResponseV05, min=1, max=1, mutex_group=None, array=False),
		))