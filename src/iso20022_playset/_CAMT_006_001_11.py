# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReturnTransactionV11 import ReturnTransactionV11

class CAMT_006_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.006.001.11"
		_docname = "camt.006.001.11"

		__slots__ = ["_RtrTx"]
		@property
		def RtrTx(self):
			return self._RtrTx

		@RtrTx.setter
		def RtrTx(self, value):
			self._RtrTx = value if type(value) != base_types.auto else self.make_default("RtrTx")

		@RtrTx.deleter
		def RtrTx(self):
			del self._RtrTx
			self._RtrTx = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrTx', type=ReturnTransactionV11, min=1, max=1, mutex_group=None, array=False),
		))