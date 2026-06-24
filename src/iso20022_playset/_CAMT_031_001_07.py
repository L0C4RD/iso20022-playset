# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RejectInvestigationV07 import RejectInvestigationV07

class CAMT_031_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.031.001.07",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_RjctInvstgtn"]
		@property
		def RjctInvstgtn(self):
			return self._RjctInvstgtn

		@RjctInvstgtn.setter
		def RjctInvstgtn(self, value):
			self._RjctInvstgtn = value if type(value) != base_types.auto else self.make_default("RjctInvstgtn")

		@RjctInvstgtn.deleter
		def RjctInvstgtn(self):
			del self._RjctInvstgtn
			self._RjctInvstgtn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RjctInvstgtn', type=RejectInvestigationV07, min=1, max=1, mutex_group=None, array=False),
		))