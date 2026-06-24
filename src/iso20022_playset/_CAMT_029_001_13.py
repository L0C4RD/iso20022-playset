# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ResolutionOfInvestigationV13 import ResolutionOfInvestigationV13

class CAMT_029_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.029.001.13",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_RsltnOfInvstgtn"]
		@property
		def RsltnOfInvstgtn(self):
			return self._RsltnOfInvstgtn

		@RsltnOfInvstgtn.setter
		def RsltnOfInvstgtn(self, value):
			self._RsltnOfInvstgtn = value if type(value) != base_types.auto else self.make_default("RsltnOfInvstgtn")

		@RsltnOfInvstgtn.deleter
		def RsltnOfInvstgtn(self):
			del self._RsltnOfInvstgtn
			self._RsltnOfInvstgtn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RsltnOfInvstgtn', type=ResolutionOfInvestigationV13, min=1, max=1, mutex_group=None, array=False),
		))