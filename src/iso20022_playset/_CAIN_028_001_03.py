# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ChargeBackResponseV03 import ChargeBackResponseV03

class CAIN_028_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cain.028.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ChrgBckRspn"]
		@property
		def ChrgBckRspn(self):
			return self._ChrgBckRspn

		@ChrgBckRspn.setter
		def ChrgBckRspn(self, value):
			self._ChrgBckRspn = value if type(value) != base_types.auto else self.make_default("ChrgBckRspn")

		@ChrgBckRspn.deleter
		def ChrgBckRspn(self):
			del self._ChrgBckRspn
			self._ChrgBckRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgBckRspn', type=ChargeBackResponseV03, min=1, max=1, mutex_group=None, array=False),
		))