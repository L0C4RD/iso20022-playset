# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NetworkManagementInitiationV04 import NetworkManagementInitiationV04

class CANM_001_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:canm.001.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_NtwkMgmtInitn"]
		@property
		def NtwkMgmtInitn(self):
			return self._NtwkMgmtInitn

		@NtwkMgmtInitn.setter
		def NtwkMgmtInitn(self, value):
			self._NtwkMgmtInitn = value if type(value) != base_types.auto else self.make_default("NtwkMgmtInitn")

		@NtwkMgmtInitn.deleter
		def NtwkMgmtInitn(self):
			del self._NtwkMgmtInitn
			self._NtwkMgmtInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtwkMgmtInitn', type=NetworkManagementInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))