# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ResolutionOfInvestigationV13

class CAMT_029_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.029.001.13"
		_docname = "camt.029.001.13"

		__slots__ = ["_RsltnOfInvstgtn"]
		@property
		def RsltnOfInvstgtn(self):
			return self._RsltnOfInvstgtn

		@RsltnOfInvstgtn.setter
		def RsltnOfInvstgtn(self, value):
			self._RsltnOfInvstgtn = value if value is not None else base_types.UninitialisedField(self, 'RsltnOfInvstgtn', ResolutionOfInvestigationV13, False)

		@RsltnOfInvstgtn.deleter
		def RsltnOfInvstgtn(self):
			del self._RsltnOfInvstgtn
			self._RsltnOfInvstgtn = base_types.UninitialisedField(self, 'RsltnOfInvstgtn', ResolutionOfInvestigationV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RsltnOfInvstgtn', type=ResolutionOfInvestigationV13, min=1, max=1, mutex_group=None, array=False),
		))