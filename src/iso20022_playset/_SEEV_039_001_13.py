# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionCancellationAdviceV13 import CorporateActionCancellationAdviceV13

class SEEV_039_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnCxlAdvc"]
		@property
		def CorpActnCxlAdvc(self):
			return self._CorpActnCxlAdvc

		@CorpActnCxlAdvc.setter
		def CorpActnCxlAdvc(self, value):
			self._CorpActnCxlAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnCxlAdvc")

		@CorpActnCxlAdvc.deleter
		def CorpActnCxlAdvc(self):
			del self._CorpActnCxlAdvc
			self._CorpActnCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnCxlAdvc', type=CorporateActionCancellationAdviceV13, min=1, max=1, mutex_group=None, array=False),
		))