# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyAuditTrailReportV02 import PartyAuditTrailReportV02

class REDA_043_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.043.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_PtyAudtTrlRpt"]
		@property
		def PtyAudtTrlRpt(self):
			return self._PtyAudtTrlRpt

		@PtyAudtTrlRpt.setter
		def PtyAudtTrlRpt(self, value):
			self._PtyAudtTrlRpt = value if type(value) != base_types.auto else self.make_default("PtyAudtTrlRpt")

		@PtyAudtTrlRpt.deleter
		def PtyAudtTrlRpt(self):
			del self._PtyAudtTrlRpt
			self._PtyAudtTrlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyAudtTrlRpt', type=PartyAuditTrailReportV02, min=1, max=1, mutex_group=None, array=False),
		))