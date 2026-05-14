# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionPendingReportV15 import SecuritiesTransactionPendingReportV15

class SEMT_018_001_15():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxPdgRpt"]
		@property
		def SctiesTxPdgRpt(self):
			return self._SctiesTxPdgRpt

		@SctiesTxPdgRpt.setter
		def SctiesTxPdgRpt(self, value):
			self._SctiesTxPdgRpt = value if type(value) != base_types.auto else self.make_default("SctiesTxPdgRpt")

		@SctiesTxPdgRpt.deleter
		def SctiesTxPdgRpt(self):
			del self._SctiesTxPdgRpt
			self._SctiesTxPdgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxPdgRpt', type=SecuritiesTransactionPendingReportV15, min=1, max=1, mutex_group=None, array=False),
		))