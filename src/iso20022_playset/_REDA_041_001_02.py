# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyActivityAdviceV02

class REDA_041_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02"
		_docname = "reda.041.001.02"

		__slots__ = ["_PtyActvtyAdvc"]
		@property
		def PtyActvtyAdvc(self):
			return self._PtyActvtyAdvc

		@PtyActvtyAdvc.setter
		def PtyActvtyAdvc(self, value):
			self._PtyActvtyAdvc = value if value is not None else base_types.UninitialisedField(self, 'PtyActvtyAdvc', PartyActivityAdviceV02, False)

		@PtyActvtyAdvc.deleter
		def PtyActvtyAdvc(self):
			del self._PtyActvtyAdvc
			self._PtyActvtyAdvc = base_types.UninitialisedField(self, 'PtyActvtyAdvc', PartyActivityAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyActvtyAdvc', type=PartyActivityAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))