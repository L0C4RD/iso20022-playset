# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SettlementInternaliserReportV01 import SettlementInternaliserReportV01

class AUTH_072_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01"
		_docname = "auth.072.001.01"

		__slots__ = ["_SttlmIntlrRpt"]
		@property
		def SttlmIntlrRpt(self):
			return self._SttlmIntlrRpt

		@SttlmIntlrRpt.setter
		def SttlmIntlrRpt(self, value):
			self._SttlmIntlrRpt = value if type(value) != base_types.auto else self.make_default("SttlmIntlrRpt")

		@SttlmIntlrRpt.deleter
		def SttlmIntlrRpt(self):
			del self._SttlmIntlrRpt
			self._SttlmIntlrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmIntlrRpt', type=SettlementInternaliserReportV01, min=1, max=1, mutex_group=None, array=False),
		))