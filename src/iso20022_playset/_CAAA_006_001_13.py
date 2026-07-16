# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCancellationResponseV13

class CAAA_006_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.006.001.13"
		_docname = "caaa.006.001.13"

		__slots__ = ["_AccptrCxlRspn"]
		@property
		def AccptrCxlRspn(self):
			return self._AccptrCxlRspn

		@AccptrCxlRspn.setter
		def AccptrCxlRspn(self, value):
			self._AccptrCxlRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrCxlRspn', AcceptorCancellationResponseV13, False)

		@AccptrCxlRspn.deleter
		def AccptrCxlRspn(self):
			del self._AccptrCxlRspn
			self._AccptrCxlRspn = base_types.UninitialisedField(self, 'AccptrCxlRspn', AcceptorCancellationResponseV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlRspn', type=AcceptorCancellationResponseV13, min=1, max=1, mutex_group=None, array=False),
		))