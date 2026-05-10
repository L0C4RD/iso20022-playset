from . import base_types
from .MoneyMarketStatisticalReportStatusAdviceV01 import MoneyMarketStatisticalReportStatusAdviceV01

class AUTH_028_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MnyMktSttstclRptStsAdvc"]
		@property
		def MnyMktSttstclRptStsAdvc(self):
			return self._MnyMktSttstclRptStsAdvc

		@MnyMktSttstclRptStsAdvc.setter
		def MnyMktSttstclRptStsAdvc(self, value):
			self._MnyMktSttstclRptStsAdvc = value if type(value) != auto else self.make_default("MnyMktSttstclRptStsAdvc")

		@MnyMktSttstclRptStsAdvc.deleter
		def MnyMktSttstclRptStsAdvc(self):
			del self._MnyMktSttstclRptStsAdvc
			self._MnyMktSttstclRptStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktSttstclRptStsAdvc', type=MoneyMarketStatisticalReportStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

