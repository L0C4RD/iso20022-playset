# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecurityReportV01 import SecurityReportV01

class REDA_012_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01"
		_docname = "reda.012.001.01"

		__slots__ = ["_SctyRpt"]
		@property
		def SctyRpt(self):
			return self._SctyRpt

		@SctyRpt.setter
		def SctyRpt(self, value):
			self._SctyRpt = value if type(value) != base_types.auto else self.make_default("SctyRpt")

		@SctyRpt.deleter
		def SctyRpt(self):
			del self._SctyRpt
			self._SctyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyRpt', type=SecurityReportV01, min=1, max=1, mutex_group=None, array=False),
		))