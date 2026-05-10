import base_types
import AccountAndBalance60
import AccountIdentification10

class AccountIdentification71Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctsListAndBalDtls", "_ForAllAccts"]
	@property
	def AcctsListAndBalDtls(self):
		return self._AcctsListAndBalDtls

	@AcctsListAndBalDtls.setter
	def AcctsListAndBalDtls(self, value):
		self._AcctsListAndBalDtls = value if type(value) != auto else self.make_default("AcctsListAndBalDtls")

	@AcctsListAndBalDtls.deleter
	def AcctsListAndBalDtls(self):
		del self._AcctsListAndBalDtls
		self._AcctsListAndBalDtls = None

	@property
	def ForAllAccts(self):
		return self._ForAllAccts

	@ForAllAccts.setter
	def ForAllAccts(self, value):
		self._ForAllAccts = value if type(value) != auto else self.make_default("ForAllAccts")

	@ForAllAccts.deleter
	def ForAllAccts(self):
		del self._ForAllAccts
		self._ForAllAccts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctsListAndBalDtls', type=AccountAndBalance60, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='ForAllAccts', type=AccountIdentification10, min=0, max=1, mutex_group=1, array=False),
	))

