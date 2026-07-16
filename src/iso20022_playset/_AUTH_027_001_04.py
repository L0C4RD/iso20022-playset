# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyControlStatusAdviceV04

class AUTH_027_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.027.001.04"
		_docname = "auth.027.001.04"

		__slots__ = ["_CcyCtrlStsAdvc"]
		@property
		def CcyCtrlStsAdvc(self):
			return self._CcyCtrlStsAdvc

		@CcyCtrlStsAdvc.setter
		def CcyCtrlStsAdvc(self, value):
			self._CcyCtrlStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'CcyCtrlStsAdvc', CurrencyControlStatusAdviceV04, False)

		@CcyCtrlStsAdvc.deleter
		def CcyCtrlStsAdvc(self):
			del self._CcyCtrlStsAdvc
			self._CcyCtrlStsAdvc = base_types.UninitialisedField(self, 'CcyCtrlStsAdvc', CurrencyControlStatusAdviceV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CcyCtrlStsAdvc', type=CurrencyControlStatusAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))