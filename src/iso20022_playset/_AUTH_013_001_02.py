# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MoneyMarketUnsecuredMarketStatisticalReportV02 import MoneyMarketUnsecuredMarketStatisticalReportV02

class AUTH_013_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MnyMktUscrdMktSttstclRpt"]
		@property
		def MnyMktUscrdMktSttstclRpt(self):
			return self._MnyMktUscrdMktSttstclRpt

		@MnyMktUscrdMktSttstclRpt.setter
		def MnyMktUscrdMktSttstclRpt(self, value):
			self._MnyMktUscrdMktSttstclRpt = value if type(value) != base_types.auto else self.make_default("MnyMktUscrdMktSttstclRpt")

		@MnyMktUscrdMktSttstclRpt.deleter
		def MnyMktUscrdMktSttstclRpt(self):
			del self._MnyMktUscrdMktSttstclRpt
			self._MnyMktUscrdMktSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktUscrdMktSttstclRpt', type=MoneyMarketUnsecuredMarketStatisticalReportV02, min=1, max=1, mutex_group=None, array=False),
		))