# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SettlementFailsMonthlyReportV01 import SettlementFailsMonthlyReportV01

class AUTH_100_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.100.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SttlmFlsMnthlyRpt"]
		@property
		def SttlmFlsMnthlyRpt(self):
			return self._SttlmFlsMnthlyRpt

		@SttlmFlsMnthlyRpt.setter
		def SttlmFlsMnthlyRpt(self, value):
			self._SttlmFlsMnthlyRpt = value if type(value) != base_types.auto else self.make_default("SttlmFlsMnthlyRpt")

		@SttlmFlsMnthlyRpt.deleter
		def SttlmFlsMnthlyRpt(self):
			del self._SttlmFlsMnthlyRpt
			self._SttlmFlsMnthlyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmFlsMnthlyRpt', type=SettlementFailsMonthlyReportV01, min=1, max=1, mutex_group=None, array=False),
		))