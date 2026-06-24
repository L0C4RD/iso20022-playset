# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EligibleCounterpartCSDCreationRequestV01 import EligibleCounterpartCSDCreationRequestV01

class REDA_026_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_ElgblCntrptCSDCreReq"]
		@property
		def ElgblCntrptCSDCreReq(self):
			return self._ElgblCntrptCSDCreReq

		@ElgblCntrptCSDCreReq.setter
		def ElgblCntrptCSDCreReq(self, value):
			self._ElgblCntrptCSDCreReq = value if type(value) != base_types.auto else self.make_default("ElgblCntrptCSDCreReq")

		@ElgblCntrptCSDCreReq.deleter
		def ElgblCntrptCSDCreReq(self):
			del self._ElgblCntrptCSDCreReq
			self._ElgblCntrptCSDCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblCntrptCSDCreReq', type=EligibleCounterpartCSDCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))