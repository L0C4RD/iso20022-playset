# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LiquidityDebitTransferV07 import LiquidityDebitTransferV07

class CAMT_051_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.051.001.07",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_LqdtyDbtTrf"]
		@property
		def LqdtyDbtTrf(self):
			return self._LqdtyDbtTrf

		@LqdtyDbtTrf.setter
		def LqdtyDbtTrf(self, value):
			self._LqdtyDbtTrf = value if type(value) != base_types.auto else self.make_default("LqdtyDbtTrf")

		@LqdtyDbtTrf.deleter
		def LqdtyDbtTrf(self):
			del self._LqdtyDbtTrf
			self._LqdtyDbtTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='LqdtyDbtTrf', type=LiquidityDebitTransferV07, min=1, max=1, mutex_group=None, array=False),
		))