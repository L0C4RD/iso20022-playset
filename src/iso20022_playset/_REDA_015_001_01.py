# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyQueryV01

class REDA_015_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01"
		_docname = "reda.015.001.01"

		__slots__ = ["_PtyQry"]
		@property
		def PtyQry(self):
			return self._PtyQry

		@PtyQry.setter
		def PtyQry(self, value):
			self._PtyQry = value if value is not None else base_types.UninitialisedField(self, 'PtyQry', PartyQueryV01, False)

		@PtyQry.deleter
		def PtyQry(self):
			del self._PtyQry
			self._PtyQry = base_types.UninitialisedField(self, 'PtyQry', PartyQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyQry', type=PartyQueryV01, min=1, max=1, mutex_group=None, array=False),
		))