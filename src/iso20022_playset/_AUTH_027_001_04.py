# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CurrencyControlStatusAdviceV04 import CurrencyControlStatusAdviceV04

class AUTH_027_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.027.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_CcyCtrlStsAdvc"]
		@property
		def CcyCtrlStsAdvc(self):
			return self._CcyCtrlStsAdvc

		@CcyCtrlStsAdvc.setter
		def CcyCtrlStsAdvc(self, value):
			self._CcyCtrlStsAdvc = value if type(value) != base_types.auto else self.make_default("CcyCtrlStsAdvc")

		@CcyCtrlStsAdvc.deleter
		def CcyCtrlStsAdvc(self):
			del self._CcyCtrlStsAdvc
			self._CcyCtrlStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CcyCtrlStsAdvc', type=CurrencyControlStatusAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))