# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BillingReportRequestV01 import BillingReportRequestV01

class CAMT_076_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.076.001.01"
		_docname = "camt.076.001.01"

		__slots__ = ["_BllgRptReq"]
		@property
		def BllgRptReq(self):
			return self._BllgRptReq

		@BllgRptReq.setter
		def BllgRptReq(self, value):
			self._BllgRptReq = value if type(value) != base_types.auto else self.make_default("BllgRptReq")

		@BllgRptReq.deleter
		def BllgRptReq(self):
			del self._BllgRptReq
			self._BllgRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BllgRptReq', type=BillingReportRequestV01, min=1, max=1, mutex_group=None, array=False),
		))