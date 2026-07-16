# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReturnStandingOrderV06

class CAMT_070_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.070.001.06"
		_docname = "camt.070.001.06"

		__slots__ = ["_RtrStgOrdr"]
		@property
		def RtrStgOrdr(self):
			return self._RtrStgOrdr

		@RtrStgOrdr.setter
		def RtrStgOrdr(self, value):
			self._RtrStgOrdr = value if value is not None else base_types.UninitialisedField(self, 'RtrStgOrdr', ReturnStandingOrderV06, False)

		@RtrStgOrdr.deleter
		def RtrStgOrdr(self):
			del self._RtrStgOrdr
			self._RtrStgOrdr = base_types.UninitialisedField(self, 'RtrStgOrdr', ReturnStandingOrderV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrStgOrdr', type=ReturnStandingOrderV06, min=1, max=1, mutex_group=None, array=False),
		))