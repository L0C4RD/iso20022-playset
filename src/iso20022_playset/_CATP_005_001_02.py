# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMRejectV02

class CATP_005_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.005.001.02"
		_docname = "catp.005.001.02"

		__slots__ = ["_ATMRjct"]
		@property
		def ATMRjct(self):
			return self._ATMRjct

		@ATMRjct.setter
		def ATMRjct(self, value):
			self._ATMRjct = value if value is not None else base_types.UninitialisedField(self, 'ATMRjct', ATMRejectV02, False)

		@ATMRjct.deleter
		def ATMRjct(self):
			del self._ATMRjct
			self._ATMRjct = base_types.UninitialisedField(self, 'ATMRjct', ATMRejectV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRjct', type=ATMRejectV02, min=1, max=1, mutex_group=None, array=False),
		))