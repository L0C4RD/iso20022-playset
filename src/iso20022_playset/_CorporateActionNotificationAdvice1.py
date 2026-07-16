# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateAction2
from . import CorporateActionOption1

class CorporateActionNotificationAdvice1(base_types._BaseFieldType):

	__slots__ = ["_CorpActnDtls", "_CorpActnOptnDtls"]
	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction2, False)

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction2, False)

	@property
	def CorpActnOptnDtls(self):
		return self._CorpActnOptnDtls

	@CorpActnOptnDtls.setter
	def CorpActnOptnDtls(self, value):
		self._CorpActnOptnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnOptnDtls', CorporateActionOption1, True)

	@CorpActnOptnDtls.deleter
	def CorpActnOptnDtls(self):
		del self._CorpActnOptnDtls
		self._CorpActnOptnDtls = base_types.UninitialisedField(self, 'CorpActnOptnDtls', CorporateActionOption1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnOptnDtls', type=CorporateActionOption1, min=0, max=None, mutex_group=None, array=True),
	))