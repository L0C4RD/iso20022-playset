# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CalendarQueryV02

class REDA_064_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.064.001.02"
		_docname = "reda.064.001.02"

		__slots__ = ["_CalQry"]
		@property
		def CalQry(self):
			return self._CalQry

		@CalQry.setter
		def CalQry(self, value):
			self._CalQry = value if value is not None else base_types.UninitialisedField(self, 'CalQry', CalendarQueryV02, False)

		@CalQry.deleter
		def CalQry(self):
			del self._CalQry
			self._CalQry = base_types.UninitialisedField(self, 'CalQry', CalendarQueryV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CalQry', type=CalendarQueryV02, min=1, max=1, mutex_group=None, array=False),
		))