# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SettlementFailsAnnualReportV01 import SettlementFailsAnnualReportV01

class AUTH_101_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01"
		_docname = "auth.101.001.01"

		__slots__ = ["_SttlmFlsAnlRpt"]
		@property
		def SttlmFlsAnlRpt(self):
			return self._SttlmFlsAnlRpt

		@SttlmFlsAnlRpt.setter
		def SttlmFlsAnlRpt(self, value):
			self._SttlmFlsAnlRpt = value if type(value) != base_types.auto else self.make_default("SttlmFlsAnlRpt")

		@SttlmFlsAnlRpt.deleter
		def SttlmFlsAnlRpt(self):
			del self._SttlmFlsAnlRpt
			self._SttlmFlsAnlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmFlsAnlRpt', type=SettlementFailsAnnualReportV01, min=1, max=1, mutex_group=None, array=False),
		))