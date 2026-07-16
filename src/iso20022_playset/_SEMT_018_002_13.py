# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionPendingReport002V13

class SEMT_018_002_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.018.002.13"
		_docname = "semt.018.002.13"

		__slots__ = ["_SctiesTxPdgRpt"]
		@property
		def SctiesTxPdgRpt(self):
			return self._SctiesTxPdgRpt

		@SctiesTxPdgRpt.setter
		def SctiesTxPdgRpt(self, value):
			self._SctiesTxPdgRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxPdgRpt', SecuritiesTransactionPendingReport002V13, False)

		@SctiesTxPdgRpt.deleter
		def SctiesTxPdgRpt(self):
			del self._SctiesTxPdgRpt
			self._SctiesTxPdgRpt = base_types.UninitialisedField(self, 'SctiesTxPdgRpt', SecuritiesTransactionPendingReport002V13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxPdgRpt', type=SecuritiesTransactionPendingReport002V13, min=1, max=1, mutex_group=None, array=False),
		))