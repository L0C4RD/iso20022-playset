# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyStatusAdviceV01

class REDA_016_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.016.001.01"
		_docname = "reda.016.001.01"

		__slots__ = ["_PtyStsAdvc"]
		@property
		def PtyStsAdvc(self):
			return self._PtyStsAdvc

		@PtyStsAdvc.setter
		def PtyStsAdvc(self, value):
			self._PtyStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'PtyStsAdvc', PartyStatusAdviceV01, False)

		@PtyStsAdvc.deleter
		def PtyStsAdvc(self):
			del self._PtyStsAdvc
			self._PtyStsAdvc = base_types.UninitialisedField(self, 'PtyStsAdvc', PartyStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyStsAdvc', type=PartyStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))