# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCurrencyConversionResponseV13

class CAAA_017_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.017.001.13"
		_docname = "caaa.017.001.13"

		__slots__ = ["_AccptrCcyConvsRspn"]
		@property
		def AccptrCcyConvsRspn(self):
			return self._AccptrCcyConvsRspn

		@AccptrCcyConvsRspn.setter
		def AccptrCcyConvsRspn(self, value):
			self._AccptrCcyConvsRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrCcyConvsRspn', AcceptorCurrencyConversionResponseV13, False)

		@AccptrCcyConvsRspn.deleter
		def AccptrCcyConvsRspn(self):
			del self._AccptrCcyConvsRspn
			self._AccptrCcyConvsRspn = base_types.UninitialisedField(self, 'AccptrCcyConvsRspn', AcceptorCurrencyConversionResponseV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsRspn', type=AcceptorCurrencyConversionResponseV13, min=1, max=1, mutex_group=None, array=False),
		))