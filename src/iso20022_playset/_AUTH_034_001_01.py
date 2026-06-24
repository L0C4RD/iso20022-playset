# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoiceTaxReportV01 import InvoiceTaxReportV01

class AUTH_034_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.034.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_InvcTaxRpt"]
		@property
		def InvcTaxRpt(self):
			return self._InvcTaxRpt

		@InvcTaxRpt.setter
		def InvcTaxRpt(self, value):
			self._InvcTaxRpt = value if type(value) != base_types.auto else self.make_default("InvcTaxRpt")

		@InvcTaxRpt.deleter
		def InvcTaxRpt(self):
			del self._InvcTaxRpt
			self._InvcTaxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcTaxRpt', type=InvoiceTaxReportV01, min=1, max=1, mutex_group=None, array=False),
		))