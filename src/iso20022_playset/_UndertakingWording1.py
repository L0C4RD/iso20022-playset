# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISO2ALanguageCode import ISO2ALanguageCode
from ._ModelFormIdentification1 import ModelFormIdentification1
from ._Narrative1 import Narrative1

class UndertakingWording1(base_types._BaseFieldType):

	__slots__ = ["_MdlForm", "_ReqdWrdgLang", "_UdrtkgTermsAndConds"]
	@property
	def MdlForm(self):
		return self._MdlForm

	@MdlForm.setter
	def MdlForm(self, value):
		self._MdlForm = value if type(value) != base_types.auto else self.make_default("MdlForm")

	@MdlForm.deleter
	def MdlForm(self):
		del self._MdlForm
		self._MdlForm = None

	@property
	def ReqdWrdgLang(self):
		return self._ReqdWrdgLang

	@ReqdWrdgLang.setter
	def ReqdWrdgLang(self, value):
		self._ReqdWrdgLang = value if type(value) != base_types.auto else self.make_default("ReqdWrdgLang")

	@ReqdWrdgLang.deleter
	def ReqdWrdgLang(self):
		del self._ReqdWrdgLang
		self._ReqdWrdgLang = None

	@property
	def UdrtkgTermsAndConds(self):
		return self._UdrtkgTermsAndConds

	@UdrtkgTermsAndConds.setter
	def UdrtkgTermsAndConds(self, value):
		self._UdrtkgTermsAndConds = value if type(value) != base_types.auto else self.make_default("UdrtkgTermsAndConds")

	@UdrtkgTermsAndConds.deleter
	def UdrtkgTermsAndConds(self):
		del self._UdrtkgTermsAndConds
		self._UdrtkgTermsAndConds = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MdlForm', type=ModelFormIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdWrdgLang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgTermsAndConds', type=Narrative1, min=0, max=None, mutex_group=None, array=True),
	))