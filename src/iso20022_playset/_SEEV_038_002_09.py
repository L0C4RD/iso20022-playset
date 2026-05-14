# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionNarrative002V09 import CorporateActionNarrative002V09

class SEEV_038_002_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnNrrtv"]
		@property
		def CorpActnNrrtv(self):
			return self._CorpActnNrrtv

		@CorpActnNrrtv.setter
		def CorpActnNrrtv(self, value):
			self._CorpActnNrrtv = value if type(value) != base_types.auto else self.make_default("CorpActnNrrtv")

		@CorpActnNrrtv.deleter
		def CorpActnNrrtv(self):
			del self._CorpActnNrrtv
			self._CorpActnNrrtv = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnNrrtv', type=CorporateActionNarrative002V09, min=1, max=1, mutex_group=None, array=False),
		))