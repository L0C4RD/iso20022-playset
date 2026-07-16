# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesMessageCancellationAdvice002V07

class SEMT_020_002_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.020.002.07"
		_docname = "semt.020.002.07"

		__slots__ = ["_SctiesMsgCxlAdvc"]
		@property
		def SctiesMsgCxlAdvc(self):
			return self._SctiesMsgCxlAdvc

		@SctiesMsgCxlAdvc.setter
		def SctiesMsgCxlAdvc(self, value):
			self._SctiesMsgCxlAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesMsgCxlAdvc', SecuritiesMessageCancellationAdvice002V07, False)

		@SctiesMsgCxlAdvc.deleter
		def SctiesMsgCxlAdvc(self):
			del self._SctiesMsgCxlAdvc
			self._SctiesMsgCxlAdvc = base_types.UninitialisedField(self, 'SctiesMsgCxlAdvc', SecuritiesMessageCancellationAdvice002V07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesMsgCxlAdvc', type=SecuritiesMessageCancellationAdvice002V07, min=1, max=1, mutex_group=None, array=False),
		))