# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialSupervisedPartyIdentityReportV01 import FinancialSupervisedPartyIdentityReportV01

class AUTH_076_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinSprvsdPtyIdntyRpt"]
		@property
		def FinSprvsdPtyIdntyRpt(self):
			return self._FinSprvsdPtyIdntyRpt

		@FinSprvsdPtyIdntyRpt.setter
		def FinSprvsdPtyIdntyRpt(self, value):
			self._FinSprvsdPtyIdntyRpt = value if type(value) != base_types.auto else self.make_default("FinSprvsdPtyIdntyRpt")

		@FinSprvsdPtyIdntyRpt.deleter
		def FinSprvsdPtyIdntyRpt(self):
			del self._FinSprvsdPtyIdntyRpt
			self._FinSprvsdPtyIdntyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinSprvsdPtyIdntyRpt', type=FinancialSupervisedPartyIdentityReportV01, min=1, max=1, mutex_group=None, array=False),
		))