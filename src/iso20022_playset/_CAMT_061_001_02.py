# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PayInCallV02

class CAMT_061_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.061.001.02"
		_docname = "camt.061.001.02"

		__slots__ = ["_PayInCall"]
		@property
		def PayInCall(self):
			return self._PayInCall

		@PayInCall.setter
		def PayInCall(self, value):
			self._PayInCall = value if value is not None else base_types.UninitialisedField(self, 'PayInCall', PayInCallV02, False)

		@PayInCall.deleter
		def PayInCall(self):
			del self._PayInCall
			self._PayInCall = base_types.UninitialisedField(self, 'PayInCall', PayInCallV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PayInCall', type=PayInCallV02, min=1, max=1, mutex_group=None, array=False),
		))