# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesBalanceAccountingReport002V11

class SEMT_003_002_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11"
		_docname = "semt.003.002.11"

		__slots__ = ["_SctiesBalAcctgRpt"]
		@property
		def SctiesBalAcctgRpt(self):
			return self._SctiesBalAcctgRpt

		@SctiesBalAcctgRpt.setter
		def SctiesBalAcctgRpt(self, value):
			self._SctiesBalAcctgRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesBalAcctgRpt', SecuritiesBalanceAccountingReport002V11, False)

		@SctiesBalAcctgRpt.deleter
		def SctiesBalAcctgRpt(self):
			del self._SctiesBalAcctgRpt
			self._SctiesBalAcctgRpt = base_types.UninitialisedField(self, 'SctiesBalAcctgRpt', SecuritiesBalanceAccountingReport002V11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalAcctgRpt', type=SecuritiesBalanceAccountingReport002V11, min=1, max=1, mutex_group=None, array=False),
		))