from . import base_types
from ._MoneyMarketSecuredMarketStatisticalReportV02 import MoneyMarketSecuredMarketStatisticalReportV02

class AUTH_012_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MnyMktScrdMktSttstclRpt"]
		@property
		def MnyMktScrdMktSttstclRpt(self):
			return self._MnyMktScrdMktSttstclRpt

		@MnyMktScrdMktSttstclRpt.setter
		def MnyMktScrdMktSttstclRpt(self, value):
			self._MnyMktScrdMktSttstclRpt = value if type(value) != base_types.auto else self.make_default("MnyMktScrdMktSttstclRpt")

		@MnyMktScrdMktSttstclRpt.deleter
		def MnyMktScrdMktSttstclRpt(self):
			del self._MnyMktScrdMktSttstclRpt
			self._MnyMktScrdMktSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktScrdMktSttstclRpt', type=MoneyMarketSecuredMarketStatisticalReportV02, min=1, max=1, mutex_group=None, array=False),
		))

