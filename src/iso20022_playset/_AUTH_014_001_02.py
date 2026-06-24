# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MoneyMarketForeignExchangeSwapsStatisticalReportV02 import MoneyMarketForeignExchangeSwapsStatisticalReportV02

class AUTH_014_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_MnyMktFXSwpsSttstclRpt"]
		@property
		def MnyMktFXSwpsSttstclRpt(self):
			return self._MnyMktFXSwpsSttstclRpt

		@MnyMktFXSwpsSttstclRpt.setter
		def MnyMktFXSwpsSttstclRpt(self, value):
			self._MnyMktFXSwpsSttstclRpt = value if type(value) != base_types.auto else self.make_default("MnyMktFXSwpsSttstclRpt")

		@MnyMktFXSwpsSttstclRpt.deleter
		def MnyMktFXSwpsSttstclRpt(self):
			del self._MnyMktFXSwpsSttstclRpt
			self._MnyMktFXSwpsSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktFXSwpsSttstclRpt', type=MoneyMarketForeignExchangeSwapsStatisticalReportV02, min=1, max=1, mutex_group=None, array=False),
		))