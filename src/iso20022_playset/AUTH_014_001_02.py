import base_types
import MoneyMarketForeignExchangeSwapsStatisticalReportV02

class AUTH_014_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MnyMktFXSwpsSttstclRpt"]
		@property
		def MnyMktFXSwpsSttstclRpt(self):
			return self._MnyMktFXSwpsSttstclRpt

		@MnyMktFXSwpsSttstclRpt.setter
		def MnyMktFXSwpsSttstclRpt(self, value):
			self._MnyMktFXSwpsSttstclRpt = value if type(value) != auto else self.make_default("MnyMktFXSwpsSttstclRpt")

		@MnyMktFXSwpsSttstclRpt.deleter
		def MnyMktFXSwpsSttstclRpt(self):
			del self._MnyMktFXSwpsSttstclRpt
			self._MnyMktFXSwpsSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktFXSwpsSttstclRpt', type=MoneyMarketForeignExchangeSwapsStatisticalReportV02, min=1, max=1, mutex_group=None, array=False),
		))

