# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingReportV01

class CAMT_077_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.077.001.01"
		_docname = "camt.077.001.01"

		__slots__ = ["_BllgRpt"]
		@property
		def BllgRpt(self):
			return self._BllgRpt

		@BllgRpt.setter
		def BllgRpt(self, value):
			self._BllgRpt = value if value is not None else base_types.UninitialisedField(self, 'BllgRpt', BillingReportV01, False)

		@BllgRpt.deleter
		def BllgRpt(self):
			del self._BllgRpt
			self._BllgRpt = base_types.UninitialisedField(self, 'BllgRpt', BillingReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BllgRpt', type=BillingReportV01, min=1, max=1, mutex_group=None, array=False),
		))