# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MoneyMarketOvernightIndexSwapsStatisticalReportV02 import MoneyMarketOvernightIndexSwapsStatisticalReportV02

class AUTH_015_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MnyMktOvrnghtIndxSwpsSttstclRpt"]
		@property
		def MnyMktOvrnghtIndxSwpsSttstclRpt(self):
			return self._MnyMktOvrnghtIndxSwpsSttstclRpt

		@MnyMktOvrnghtIndxSwpsSttstclRpt.setter
		def MnyMktOvrnghtIndxSwpsSttstclRpt(self, value):
			self._MnyMktOvrnghtIndxSwpsSttstclRpt = value if type(value) != base_types.auto else self.make_default("MnyMktOvrnghtIndxSwpsSttstclRpt")

		@MnyMktOvrnghtIndxSwpsSttstclRpt.deleter
		def MnyMktOvrnghtIndxSwpsSttstclRpt(self):
			del self._MnyMktOvrnghtIndxSwpsSttstclRpt
			self._MnyMktOvrnghtIndxSwpsSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktOvrnghtIndxSwpsSttstclRpt', type=MoneyMarketOvernightIndexSwapsStatisticalReportV02, min=1, max=1, mutex_group=None, array=False),
		))