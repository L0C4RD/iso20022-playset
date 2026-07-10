# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ProprietaryFormatInvestigationV06 import ProprietaryFormatInvestigationV06

class CAMT_035_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.035.001.06"
		_docname = "camt.035.001.06"

		__slots__ = ["_PrtryFrmtInvstgtn"]
		@property
		def PrtryFrmtInvstgtn(self):
			return self._PrtryFrmtInvstgtn

		@PrtryFrmtInvstgtn.setter
		def PrtryFrmtInvstgtn(self, value):
			self._PrtryFrmtInvstgtn = value if type(value) != base_types.auto else self.make_default("PrtryFrmtInvstgtn")

		@PrtryFrmtInvstgtn.deleter
		def PrtryFrmtInvstgtn(self):
			del self._PrtryFrmtInvstgtn
			self._PrtryFrmtInvstgtn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtryFrmtInvstgtn', type=ProprietaryFormatInvestigationV06, min=1, max=1, mutex_group=None, array=False),
		))