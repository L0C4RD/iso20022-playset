# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyEventAdviceV01

class TSMT_055_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.055.001.01"
		_docname = "tsmt.055.001.01"

		__slots__ = ["_PtyEvtAdvc"]
		@property
		def PtyEvtAdvc(self):
			return self._PtyEvtAdvc

		@PtyEvtAdvc.setter
		def PtyEvtAdvc(self, value):
			self._PtyEvtAdvc = value if value is not None else base_types.UninitialisedField(self, 'PtyEvtAdvc', PartyEventAdviceV01, False)

		@PtyEvtAdvc.deleter
		def PtyEvtAdvc(self):
			del self._PtyEvtAdvc
			self._PtyEvtAdvc = base_types.UninitialisedField(self, 'PtyEvtAdvc', PartyEventAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyEvtAdvc', type=PartyEventAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))