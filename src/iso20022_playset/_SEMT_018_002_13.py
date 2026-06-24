# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionPendingReport002V13 import SecuritiesTransactionPendingReport002V13

class SEMT_018_002_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.018.002.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

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
			base_types.FieldEntry(name='SctiesTxPdgRpt', type=SecuritiesTransactionPendingReport002V13, min=1, max=1, mutex_group=None, array=False),
		))