# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesBalanceCustodyReportV12 import SecuritiesBalanceCustodyReportV12

class SEMT_002_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.002.001.12"
		_docname = "semt.002.001.12"

		__slots__ = ["_SctiesBalCtdyRpt"]
		@property
		def SctiesBalCtdyRpt(self):
			return self._SctiesBalCtdyRpt

		@SctiesBalCtdyRpt.setter
		def SctiesBalCtdyRpt(self, value):
			self._SctiesBalCtdyRpt = value if type(value) != base_types.auto else self.make_default("SctiesBalCtdyRpt")

		@SctiesBalCtdyRpt.deleter
		def SctiesBalCtdyRpt(self):
			del self._SctiesBalCtdyRpt
			self._SctiesBalCtdyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalCtdyRpt', type=SecuritiesBalanceCustodyReportV12, min=1, max=1, mutex_group=None, array=False),
		))