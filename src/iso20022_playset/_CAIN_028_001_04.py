# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ChargeBackResponseV04

class CAIN_028_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.028.001.04"
		_docname = "cain.028.001.04"

		__slots__ = ["_ChrgBckRspn"]
		@property
		def ChrgBckRspn(self):
			return self._ChrgBckRspn

		@ChrgBckRspn.setter
		def ChrgBckRspn(self, value):
			self._ChrgBckRspn = value if value is not None else base_types.UninitialisedField(self, 'ChrgBckRspn', ChargeBackResponseV04, False)

		@ChrgBckRspn.deleter
		def ChrgBckRspn(self):
			del self._ChrgBckRspn
			self._ChrgBckRspn = base_types.UninitialisedField(self, 'ChrgBckRspn', ChargeBackResponseV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgBckRspn', type=ChargeBackResponseV04, min=1, max=1, mutex_group=None, array=False),
		))