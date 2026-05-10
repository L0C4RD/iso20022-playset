import base_types
import UndertakingAmount2
import ExpiryDetails1

class Undertaking10(base_types._BaseFieldType):

	__slots__ = ["_NewXpryDtls", "_NewUdrtkgAmt"]
	@property
	def NewXpryDtls(self):
		return self._NewXpryDtls

	@NewXpryDtls.setter
	def NewXpryDtls(self, value):
		self._NewXpryDtls = value if type(value) != auto else self.make_default("NewXpryDtls")

	@NewXpryDtls.deleter
	def NewXpryDtls(self):
		del self._NewXpryDtls
		self._NewXpryDtls = None

	@property
	def NewUdrtkgAmt(self):
		return self._NewUdrtkgAmt

	@NewUdrtkgAmt.setter
	def NewUdrtkgAmt(self, value):
		self._NewUdrtkgAmt = value if type(value) != auto else self.make_default("NewUdrtkgAmt")

	@NewUdrtkgAmt.deleter
	def NewUdrtkgAmt(self):
		del self._NewUdrtkgAmt
		self._NewUdrtkgAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewXpryDtls', type=ExpiryDetails1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewUdrtkgAmt', type=UndertakingAmount2, min=0, max=1, mutex_group=None, array=False),
	))

