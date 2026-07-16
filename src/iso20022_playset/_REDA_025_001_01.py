# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligibleSecuritiesCreationRequestV01

class REDA_025_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.025.001.01"
		_docname = "reda.025.001.01"

		__slots__ = ["_ElgblSctiesCreReq"]
		@property
		def ElgblSctiesCreReq(self):
			return self._ElgblSctiesCreReq

		@ElgblSctiesCreReq.setter
		def ElgblSctiesCreReq(self, value):
			self._ElgblSctiesCreReq = value if value is not None else base_types.UninitialisedField(self, 'ElgblSctiesCreReq', EligibleSecuritiesCreationRequestV01, False)

		@ElgblSctiesCreReq.deleter
		def ElgblSctiesCreReq(self):
			del self._ElgblSctiesCreReq
			self._ElgblSctiesCreReq = base_types.UninitialisedField(self, 'ElgblSctiesCreReq', EligibleSecuritiesCreationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblSctiesCreReq', type=EligibleSecuritiesCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))