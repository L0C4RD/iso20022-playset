# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NetworkManagementInitiationV04

class CANM_001_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:canm.001.001.04"
		_docname = "canm.001.001.04"

		__slots__ = ["_NtwkMgmtInitn"]
		@property
		def NtwkMgmtInitn(self):
			return self._NtwkMgmtInitn

		@NtwkMgmtInitn.setter
		def NtwkMgmtInitn(self, value):
			self._NtwkMgmtInitn = value if value is not None else base_types.UninitialisedField(self, 'NtwkMgmtInitn', NetworkManagementInitiationV04, False)

		@NtwkMgmtInitn.deleter
		def NtwkMgmtInitn(self):
			del self._NtwkMgmtInitn
			self._NtwkMgmtInitn = base_types.UninitialisedField(self, 'NtwkMgmtInitn', NetworkManagementInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtwkMgmtInitn', type=NetworkManagementInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))