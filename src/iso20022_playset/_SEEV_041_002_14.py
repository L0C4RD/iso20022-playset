# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionInstructionCancellationRequestStatusAdvice002V14 import CorporateActionInstructionCancellationRequestStatusAdvice002V14

class SEEV_041_002_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnInstrCxlReqStsAdvc"]
		@property
		def CorpActnInstrCxlReqStsAdvc(self):
			return self._CorpActnInstrCxlReqStsAdvc

		@CorpActnInstrCxlReqStsAdvc.setter
		def CorpActnInstrCxlReqStsAdvc(self, value):
			self._CorpActnInstrCxlReqStsAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnInstrCxlReqStsAdvc")

		@CorpActnInstrCxlReqStsAdvc.deleter
		def CorpActnInstrCxlReqStsAdvc(self):
			del self._CorpActnInstrCxlReqStsAdvc
			self._CorpActnInstrCxlReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrCxlReqStsAdvc', type=CorporateActionInstructionCancellationRequestStatusAdvice002V14, min=1, max=1, mutex_group=None, array=False),
		))