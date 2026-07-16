# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationResponseV03

class CAMT_111_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.111.001.03"
		_docname = "camt.111.001.03"

		__slots__ = ["_InvstgtnRspn"]
		@property
		def InvstgtnRspn(self):
			return self._InvstgtnRspn

		@InvstgtnRspn.setter
		def InvstgtnRspn(self, value):
			self._InvstgtnRspn = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnRspn', InvestigationResponseV03, False)

		@InvstgtnRspn.deleter
		def InvstgtnRspn(self):
			del self._InvstgtnRspn
			self._InvstgtnRspn = base_types.UninitialisedField(self, 'InvstgtnRspn', InvestigationResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvstgtnRspn', type=InvestigationResponseV03, min=1, max=1, mutex_group=None, array=False),
		))