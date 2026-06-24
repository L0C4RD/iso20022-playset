# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesBalanceAccountingReport002V11 import SecuritiesBalanceAccountingReport002V11

class SEMT_003_002_11():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.003.002.11"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SctiesBalAcctgRpt"]
		@property
		def SctiesBalAcctgRpt(self):
			return self._SctiesBalAcctgRpt

		@SctiesBalAcctgRpt.setter
		def SctiesBalAcctgRpt(self, value):
			self._SctiesBalAcctgRpt = value if type(value) != base_types.auto else self.make_default("SctiesBalAcctgRpt")

		@SctiesBalAcctgRpt.deleter
		def SctiesBalAcctgRpt(self):
			del self._SctiesBalAcctgRpt
			self._SctiesBalAcctgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalAcctgRpt', type=SecuritiesBalanceAccountingReport002V11, min=1, max=1, mutex_group=None, array=False),
		))