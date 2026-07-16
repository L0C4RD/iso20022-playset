# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCurrencyConversionAdviceV09

class CAAA_018_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.018.001.09"
		_docname = "caaa.018.001.09"

		__slots__ = ["_AccptrCcyConvsAdvc"]
		@property
		def AccptrCcyConvsAdvc(self):
			return self._AccptrCcyConvsAdvc

		@AccptrCcyConvsAdvc.setter
		def AccptrCcyConvsAdvc(self, value):
			self._AccptrCcyConvsAdvc = value if value is not None else base_types.UninitialisedField(self, 'AccptrCcyConvsAdvc', AcceptorCurrencyConversionAdviceV09, False)

		@AccptrCcyConvsAdvc.deleter
		def AccptrCcyConvsAdvc(self):
			del self._AccptrCcyConvsAdvc
			self._AccptrCcyConvsAdvc = base_types.UninitialisedField(self, 'AccptrCcyConvsAdvc', AcceptorCurrencyConversionAdviceV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsAdvc', type=AcceptorCurrencyConversionAdviceV09, min=1, max=1, mutex_group=None, array=False),
		))