import base_types
import Narrative1
import ISO2ALanguageCode
import ModelFormIdentification1

class UndertakingWording1(base_types._BaseFieldType):

	__slots__ = ["_MdlForm", "_UdrtkgTermsAndConds", "_ReqdWrdgLang"]
	@property
	def MdlForm(self):
		return self._MdlForm

	@MdlForm.setter
	def MdlForm(self, value):
		self._MdlForm = value if type(value) != auto else self.make_default("MdlForm")

	@MdlForm.deleter
	def MdlForm(self):
		del self._MdlForm
		self._MdlForm = None

	@property
	def UdrtkgTermsAndConds(self):
		return self._UdrtkgTermsAndConds

	@UdrtkgTermsAndConds.setter
	def UdrtkgTermsAndConds(self, value):
		self._UdrtkgTermsAndConds = value if type(value) != auto else self.make_default("UdrtkgTermsAndConds")

	@UdrtkgTermsAndConds.deleter
	def UdrtkgTermsAndConds(self):
		del self._UdrtkgTermsAndConds
		self._UdrtkgTermsAndConds = None

	@property
	def ReqdWrdgLang(self):
		return self._ReqdWrdgLang

	@ReqdWrdgLang.setter
	def ReqdWrdgLang(self, value):
		self._ReqdWrdgLang = value if type(value) != auto else self.make_default("ReqdWrdgLang")

	@ReqdWrdgLang.deleter
	def ReqdWrdgLang(self):
		del self._ReqdWrdgLang
		self._ReqdWrdgLang = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MdlForm', type=ModelFormIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgTermsAndConds', type=Narrative1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdWrdgLang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
	))

