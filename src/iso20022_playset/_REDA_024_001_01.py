# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralValueCreationRequestV01

class REDA_024_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01"
		_docname = "reda.024.001.01"

		__slots__ = ["_CollValCreReq"]
		@property
		def CollValCreReq(self):
			return self._CollValCreReq

		@CollValCreReq.setter
		def CollValCreReq(self, value):
			self._CollValCreReq = value if value is not None else base_types.UninitialisedField(self, 'CollValCreReq', CollateralValueCreationRequestV01, False)

		@CollValCreReq.deleter
		def CollValCreReq(self):
			del self._CollValCreReq
			self._CollValCreReq = base_types.UninitialisedField(self, 'CollValCreReq', CollateralValueCreationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollValCreReq', type=CollateralValueCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))