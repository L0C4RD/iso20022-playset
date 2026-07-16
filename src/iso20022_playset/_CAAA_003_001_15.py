# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCompletionAdviceV15

class CAAA_003_001_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.003.001.15"
		_docname = "caaa.003.001.15"

		__slots__ = ["_AccptrCmpltnAdvc"]
		@property
		def AccptrCmpltnAdvc(self):
			return self._AccptrCmpltnAdvc

		@AccptrCmpltnAdvc.setter
		def AccptrCmpltnAdvc(self, value):
			self._AccptrCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'AccptrCmpltnAdvc', AcceptorCompletionAdviceV15, False)

		@AccptrCmpltnAdvc.deleter
		def AccptrCmpltnAdvc(self):
			del self._AccptrCmpltnAdvc
			self._AccptrCmpltnAdvc = base_types.UninitialisedField(self, 'AccptrCmpltnAdvc', AcceptorCompletionAdviceV15, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCmpltnAdvc', type=AcceptorCompletionAdviceV15, min=1, max=1, mutex_group=None, array=False),
		))