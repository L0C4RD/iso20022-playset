# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionStatusQuery002V06 import SecuritiesTransactionStatusQuery002V06

class SESE_021_002_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.021.002.06"
		_docname = "sese.021.002.06"

		__slots__ = ["_SctiesTxStsQry"]
		@property
		def SctiesTxStsQry(self):
			return self._SctiesTxStsQry

		@SctiesTxStsQry.setter
		def SctiesTxStsQry(self, value):
			self._SctiesTxStsQry = value if type(value) != base_types.auto else self.make_default("SctiesTxStsQry")

		@SctiesTxStsQry.deleter
		def SctiesTxStsQry(self):
			del self._SctiesTxStsQry
			self._SctiesTxStsQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxStsQry', type=SecuritiesTransactionStatusQuery002V06, min=1, max=1, mutex_group=None, array=False),
		))