# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationModificationAdviceV04

class ACMT_022_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.022.001.04"
		_docname = "acmt.022.001.04"

		__slots__ = ["_IdModAdvc"]
		@property
		def IdModAdvc(self):
			return self._IdModAdvc

		@IdModAdvc.setter
		def IdModAdvc(self, value):
			self._IdModAdvc = value if value is not None else base_types.UninitialisedField(self, 'IdModAdvc', IdentificationModificationAdviceV04, False)

		@IdModAdvc.deleter
		def IdModAdvc(self):
			del self._IdModAdvc
			self._IdModAdvc = base_types.UninitialisedField(self, 'IdModAdvc', IdentificationModificationAdviceV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IdModAdvc', type=IdentificationModificationAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))