# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NettingCutOffReferenceDataUpdateRequestV02

class REDA_060_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02"
		_docname = "reda.060.001.02"

		__slots__ = ["_NetgCutOffRefDataUpdReq"]
		@property
		def NetgCutOffRefDataUpdReq(self):
			return self._NetgCutOffRefDataUpdReq

		@NetgCutOffRefDataUpdReq.setter
		def NetgCutOffRefDataUpdReq(self, value):
			self._NetgCutOffRefDataUpdReq = value if value is not None else base_types.UninitialisedField(self, 'NetgCutOffRefDataUpdReq', NettingCutOffReferenceDataUpdateRequestV02, False)

		@NetgCutOffRefDataUpdReq.deleter
		def NetgCutOffRefDataUpdReq(self):
			del self._NetgCutOffRefDataUpdReq
			self._NetgCutOffRefDataUpdReq = base_types.UninitialisedField(self, 'NetgCutOffRefDataUpdReq', NettingCutOffReferenceDataUpdateRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NetgCutOffRefDataUpdReq', type=NettingCutOffReferenceDataUpdateRequestV02, min=1, max=1, mutex_group=None, array=False),
		))