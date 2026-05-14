# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionMovementReversalAdviceV17 import CorporateActionMovementReversalAdviceV17

class SEEV_037_001_17():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnMvmntRvslAdvc"]
		@property
		def CorpActnMvmntRvslAdvc(self):
			return self._CorpActnMvmntRvslAdvc

		@CorpActnMvmntRvslAdvc.setter
		def CorpActnMvmntRvslAdvc(self, value):
			self._CorpActnMvmntRvslAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnMvmntRvslAdvc")

		@CorpActnMvmntRvslAdvc.deleter
		def CorpActnMvmntRvslAdvc(self):
			del self._CorpActnMvmntRvslAdvc
			self._CorpActnMvmntRvslAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntRvslAdvc', type=CorporateActionMovementReversalAdviceV17, min=1, max=1, mutex_group=None, array=False),
		))