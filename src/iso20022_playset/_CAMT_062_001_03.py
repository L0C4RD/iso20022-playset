# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PayInScheduleV03 import PayInScheduleV03

class CAMT_062_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03"
		_docname = "camt.062.001.03"

		__slots__ = ["_PayInSchdl"]
		@property
		def PayInSchdl(self):
			return self._PayInSchdl

		@PayInSchdl.setter
		def PayInSchdl(self, value):
			self._PayInSchdl = value if type(value) != base_types.auto else self.make_default("PayInSchdl")

		@PayInSchdl.deleter
		def PayInSchdl(self):
			del self._PayInSchdl
			self._PayInSchdl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PayInSchdl', type=PayInScheduleV03, min=1, max=1, mutex_group=None, array=False),
		))