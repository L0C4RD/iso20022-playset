# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NetReportV04 import NetReportV04

class CAMT_088_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.088.001.04"
		_docname = "camt.088.001.04"

		__slots__ = ["_NetRpt"]
		@property
		def NetRpt(self):
			return self._NetRpt

		@NetRpt.setter
		def NetRpt(self, value):
			self._NetRpt = value if type(value) != base_types.auto else self.make_default("NetRpt")

		@NetRpt.deleter
		def NetRpt(self):
			del self._NetRpt
			self._NetRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NetRpt', type=NetReportV04, min=1, max=1, mutex_group=None, array=False),
		))