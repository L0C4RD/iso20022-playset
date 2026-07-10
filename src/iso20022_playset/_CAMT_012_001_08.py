# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DeleteLimitV08 import DeleteLimitV08

class CAMT_012_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.012.001.08"
		_docname = "camt.012.001.08"

		__slots__ = ["_DelLmt"]
		@property
		def DelLmt(self):
			return self._DelLmt

		@DelLmt.setter
		def DelLmt(self, value):
			self._DelLmt = value if type(value) != base_types.auto else self.make_default("DelLmt")

		@DelLmt.deleter
		def DelLmt(self):
			del self._DelLmt
			self._DelLmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DelLmt', type=DeleteLimitV08, min=1, max=1, mutex_group=None, array=False),
		))