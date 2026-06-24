# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesAccountAuditTrailReportV01 import SecuritiesAccountAuditTrailReportV01

class REDA_037_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.037.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesAcctAudtTrlRpt"]
		@property
		def SctiesAcctAudtTrlRpt(self):
			return self._SctiesAcctAudtTrlRpt

		@SctiesAcctAudtTrlRpt.setter
		def SctiesAcctAudtTrlRpt(self, value):
			self._SctiesAcctAudtTrlRpt = value if type(value) != base_types.auto else self.make_default("SctiesAcctAudtTrlRpt")

		@SctiesAcctAudtTrlRpt.deleter
		def SctiesAcctAudtTrlRpt(self):
			del self._SctiesAcctAudtTrlRpt
			self._SctiesAcctAudtTrlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctAudtTrlRpt', type=SecuritiesAccountAuditTrailReportV01, min=1, max=1, mutex_group=None, array=False),
		))