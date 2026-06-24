# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesMessageCancellationAdviceV07 import SecuritiesMessageCancellationAdviceV07

class SEMT_020_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesMsgCxlAdvc"]
		@property
		def SctiesMsgCxlAdvc(self):
			return self._SctiesMsgCxlAdvc

		@SctiesMsgCxlAdvc.setter
		def SctiesMsgCxlAdvc(self, value):
			self._SctiesMsgCxlAdvc = value if type(value) != base_types.auto else self.make_default("SctiesMsgCxlAdvc")

		@SctiesMsgCxlAdvc.deleter
		def SctiesMsgCxlAdvc(self):
			del self._SctiesMsgCxlAdvc
			self._SctiesMsgCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesMsgCxlAdvc', type=SecuritiesMessageCancellationAdviceV07, min=1, max=1, mutex_group=None, array=False),
		))