# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligibleCounterpartCSDStatusAdviceV01

class REDA_044_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01"
		_docname = "reda.044.001.01"

		__slots__ = ["_ElgblCntrptCSDStsAdvc"]
		@property
		def ElgblCntrptCSDStsAdvc(self):
			return self._ElgblCntrptCSDStsAdvc

		@ElgblCntrptCSDStsAdvc.setter
		def ElgblCntrptCSDStsAdvc(self, value):
			self._ElgblCntrptCSDStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'ElgblCntrptCSDStsAdvc', EligibleCounterpartCSDStatusAdviceV01, False)

		@ElgblCntrptCSDStsAdvc.deleter
		def ElgblCntrptCSDStsAdvc(self):
			del self._ElgblCntrptCSDStsAdvc
			self._ElgblCntrptCSDStsAdvc = base_types.UninitialisedField(self, 'ElgblCntrptCSDStsAdvc', EligibleCounterpartCSDStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblCntrptCSDStsAdvc', type=EligibleCounterpartCSDStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))