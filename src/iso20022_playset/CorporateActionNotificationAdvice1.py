from . import base_types
import CorporateAction2
import CorporateActionOption1

class CorporateActionNotificationAdvice1(base_types._BaseFieldType):

	__slots__ = ["_CorpActnDtls", "_CorpActnOptnDtls"]
	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if type(value) != auto else self.make_default("CorpActnDtls")

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = None

	@property
	def CorpActnOptnDtls(self):
		return self._CorpActnOptnDtls

	@CorpActnOptnDtls.setter
	def CorpActnOptnDtls(self, value):
		self._CorpActnOptnDtls = value if type(value) != auto else self.make_default("CorpActnOptnDtls")

	@CorpActnOptnDtls.deleter
	def CorpActnOptnDtls(self):
		del self._CorpActnOptnDtls
		self._CorpActnOptnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnOptnDtls', type=CorporateActionOption1, min=0, max=None, mutex_group=None, array=True),
	))

