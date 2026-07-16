# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligibleCounterpartCSDCreationRequestV01

class REDA_026_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01"
		_docname = "reda.026.001.01"

		__slots__ = ["_ElgblCntrptCSDCreReq"]
		@property
		def ElgblCntrptCSDCreReq(self):
			return self._ElgblCntrptCSDCreReq

		@ElgblCntrptCSDCreReq.setter
		def ElgblCntrptCSDCreReq(self, value):
			self._ElgblCntrptCSDCreReq = value if value is not None else base_types.UninitialisedField(self, 'ElgblCntrptCSDCreReq', EligibleCounterpartCSDCreationRequestV01, False)

		@ElgblCntrptCSDCreReq.deleter
		def ElgblCntrptCSDCreReq(self):
			del self._ElgblCntrptCSDCreReq
			self._ElgblCntrptCSDCreReq = base_types.UninitialisedField(self, 'ElgblCntrptCSDCreReq', EligibleCounterpartCSDCreationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblCntrptCSDCreReq', type=EligibleCounterpartCSDCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))