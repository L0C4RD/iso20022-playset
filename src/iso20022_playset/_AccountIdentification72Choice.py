from . import base_types
from ._AccountIdentification10 import AccountIdentification10
from ._AccountIdentification71 import AccountIdentification71

class AccountIdentification72Choice(base_types._BaseFieldType):

	__slots__ = ["_ForAllAccts", "_AcctsListAndBalDtls"]
	@property
	def ForAllAccts(self):
		return self._ForAllAccts

	@ForAllAccts.setter
	def ForAllAccts(self, value):
		self._ForAllAccts = value if type(value) != base_types.auto else self.make_default("ForAllAccts")

	@ForAllAccts.deleter
	def ForAllAccts(self):
		del self._ForAllAccts
		self._ForAllAccts = None

	@property
	def AcctsListAndBalDtls(self):
		return self._AcctsListAndBalDtls

	@AcctsListAndBalDtls.setter
	def AcctsListAndBalDtls(self, value):
		self._AcctsListAndBalDtls = value if type(value) != base_types.auto else self.make_default("AcctsListAndBalDtls")

	@AcctsListAndBalDtls.deleter
	def AcctsListAndBalDtls(self):
		del self._AcctsListAndBalDtls
		self._AcctsListAndBalDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ForAllAccts', type=AccountIdentification10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AcctsListAndBalDtls', type=AccountIdentification71, min=1, max=None, mutex_group=1, array=True),
	))

