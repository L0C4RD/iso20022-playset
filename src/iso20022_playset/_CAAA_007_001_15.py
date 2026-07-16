# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCancellationAdviceV15

class CAAA_007_001_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.007.001.15"
		_docname = "caaa.007.001.15"

		__slots__ = ["_AccptrCxlAdvc"]
		@property
		def AccptrCxlAdvc(self):
			return self._AccptrCxlAdvc

		@AccptrCxlAdvc.setter
		def AccptrCxlAdvc(self, value):
			self._AccptrCxlAdvc = value if value is not None else base_types.UninitialisedField(self, 'AccptrCxlAdvc', AcceptorCancellationAdviceV15, False)

		@AccptrCxlAdvc.deleter
		def AccptrCxlAdvc(self):
			del self._AccptrCxlAdvc
			self._AccptrCxlAdvc = base_types.UninitialisedField(self, 'AccptrCxlAdvc', AcceptorCancellationAdviceV15, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlAdvc', type=AcceptorCancellationAdviceV15, min=1, max=1, mutex_group=None, array=False),
		))