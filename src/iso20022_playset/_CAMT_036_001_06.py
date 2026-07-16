# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebitAuthorisationResponseV06

class CAMT_036_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.036.001.06"
		_docname = "camt.036.001.06"

		__slots__ = ["_DbtAuthstnRspn"]
		@property
		def DbtAuthstnRspn(self):
			return self._DbtAuthstnRspn

		@DbtAuthstnRspn.setter
		def DbtAuthstnRspn(self, value):
			self._DbtAuthstnRspn = value if value is not None else base_types.UninitialisedField(self, 'DbtAuthstnRspn', DebitAuthorisationResponseV06, False)

		@DbtAuthstnRspn.deleter
		def DbtAuthstnRspn(self):
			del self._DbtAuthstnRspn
			self._DbtAuthstnRspn = base_types.UninitialisedField(self, 'DbtAuthstnRspn', DebitAuthorisationResponseV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DbtAuthstnRspn', type=DebitAuthorisationResponseV06, min=1, max=1, mutex_group=None, array=False),
		))