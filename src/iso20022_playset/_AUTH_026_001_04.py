# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CurrencyControlRequestOrLetterV04 import CurrencyControlRequestOrLetterV04

class AUTH_026_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.026.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_CcyCtrlReqOrLttr"]
		@property
		def CcyCtrlReqOrLttr(self):
			return self._CcyCtrlReqOrLttr

		@CcyCtrlReqOrLttr.setter
		def CcyCtrlReqOrLttr(self, value):
			self._CcyCtrlReqOrLttr = value if type(value) != base_types.auto else self.make_default("CcyCtrlReqOrLttr")

		@CcyCtrlReqOrLttr.deleter
		def CcyCtrlReqOrLttr(self):
			del self._CcyCtrlReqOrLttr
			self._CcyCtrlReqOrLttr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CcyCtrlReqOrLttr', type=CurrencyControlRequestOrLetterV04, min=1, max=1, mutex_group=None, array=False),
		))