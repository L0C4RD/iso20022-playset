# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransactionReportV03 import TransactionReportV03

class TSMT_041_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03"
		_docname = "tsmt.041.001.03"

		__slots__ = ["_TxRpt"]
		@property
		def TxRpt(self):
			return self._TxRpt

		@TxRpt.setter
		def TxRpt(self, value):
			self._TxRpt = value if type(value) != base_types.auto else self.make_default("TxRpt")

		@TxRpt.deleter
		def TxRpt(self):
			del self._TxRpt
			self._TxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxRpt', type=TransactionReportV03, min=1, max=1, mutex_group=None, array=False),
		))