# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EligibleCounterpartCSDStatusAdviceV01 import EligibleCounterpartCSDStatusAdviceV01

class REDA_044_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.044.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ElgblCntrptCSDStsAdvc"]
		@property
		def ElgblCntrptCSDStsAdvc(self):
			return self._ElgblCntrptCSDStsAdvc

		@ElgblCntrptCSDStsAdvc.setter
		def ElgblCntrptCSDStsAdvc(self, value):
			self._ElgblCntrptCSDStsAdvc = value if type(value) != base_types.auto else self.make_default("ElgblCntrptCSDStsAdvc")

		@ElgblCntrptCSDStsAdvc.deleter
		def ElgblCntrptCSDStsAdvc(self):
			del self._ElgblCntrptCSDStsAdvc
			self._ElgblCntrptCSDStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblCntrptCSDStsAdvc', type=EligibleCounterpartCSDStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))