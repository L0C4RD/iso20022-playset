# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BillingReportV01 import BillingReportV01

class CAMT_077_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.077.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_BllgRpt"]
		@property
		def BllgRpt(self):
			return self._BllgRpt

		@BllgRpt.setter
		def BllgRpt(self, value):
			self._BllgRpt = value if type(value) != base_types.auto else self.make_default("BllgRpt")

		@BllgRpt.deleter
		def BllgRpt(self):
			del self._BllgRpt
			self._BllgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BllgRpt', type=BillingReportV01, min=1, max=1, mutex_group=None, array=False),
		))