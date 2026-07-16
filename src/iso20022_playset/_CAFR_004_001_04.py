# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FraudDispositionResponseV04

class CAFR_004_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cafr.004.001.04"
		_docname = "cafr.004.001.04"

		__slots__ = ["_FrdDspstnRspn"]
		@property
		def FrdDspstnRspn(self):
			return self._FrdDspstnRspn

		@FrdDspstnRspn.setter
		def FrdDspstnRspn(self, value):
			self._FrdDspstnRspn = value if value is not None else base_types.UninitialisedField(self, 'FrdDspstnRspn', FraudDispositionResponseV04, False)

		@FrdDspstnRspn.deleter
		def FrdDspstnRspn(self):
			del self._FrdDspstnRspn
			self._FrdDspstnRspn = base_types.UninitialisedField(self, 'FrdDspstnRspn', FraudDispositionResponseV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdDspstnRspn', type=FraudDispositionResponseV04, min=1, max=1, mutex_group=None, array=False),
		))