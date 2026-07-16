# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO2ALanguageCode
from . import ModelFormIdentification1
from . import Narrative1

class UndertakingWording1(base_types._BaseFieldType):

	__slots__ = ["_MdlForm", "_ReqdWrdgLang", "_UdrtkgTermsAndConds"]
	@property
	def MdlForm(self):
		return self._MdlForm

	@MdlForm.setter
	def MdlForm(self, value):
		self._MdlForm = value if value is not None else base_types.UninitialisedField(self, 'MdlForm', ModelFormIdentification1, False)

	@MdlForm.deleter
	def MdlForm(self):
		del self._MdlForm
		self._MdlForm = base_types.UninitialisedField(self, 'MdlForm', ModelFormIdentification1, False)

	@property
	def ReqdWrdgLang(self):
		return self._ReqdWrdgLang

	@ReqdWrdgLang.setter
	def ReqdWrdgLang(self, value):
		self._ReqdWrdgLang = value if value is not None else base_types.UninitialisedField(self, 'ReqdWrdgLang', ISO2ALanguageCode, False)

	@ReqdWrdgLang.deleter
	def ReqdWrdgLang(self):
		del self._ReqdWrdgLang
		self._ReqdWrdgLang = base_types.UninitialisedField(self, 'ReqdWrdgLang', ISO2ALanguageCode, False)

	@property
	def UdrtkgTermsAndConds(self):
		return self._UdrtkgTermsAndConds

	@UdrtkgTermsAndConds.setter
	def UdrtkgTermsAndConds(self, value):
		self._UdrtkgTermsAndConds = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgTermsAndConds', Narrative1, True)

	@UdrtkgTermsAndConds.deleter
	def UdrtkgTermsAndConds(self):
		del self._UdrtkgTermsAndConds
		self._UdrtkgTermsAndConds = base_types.UninitialisedField(self, 'UdrtkgTermsAndConds', Narrative1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MdlForm', type=ModelFormIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdWrdgLang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgTermsAndConds', type=Narrative1, min=0, max=None, mutex_group=None, array=True),
	))