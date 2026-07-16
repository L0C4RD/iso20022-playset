# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExpiryDetails1
from . import UndertakingAmount2

class Undertaking10(base_types._BaseFieldType):

	__slots__ = ["_NewUdrtkgAmt", "_NewXpryDtls"]
	@property
	def NewUdrtkgAmt(self):
		return self._NewUdrtkgAmt

	@NewUdrtkgAmt.setter
	def NewUdrtkgAmt(self, value):
		self._NewUdrtkgAmt = value if value is not None else base_types.UninitialisedField(self, 'NewUdrtkgAmt', UndertakingAmount2, False)

	@NewUdrtkgAmt.deleter
	def NewUdrtkgAmt(self):
		del self._NewUdrtkgAmt
		self._NewUdrtkgAmt = base_types.UninitialisedField(self, 'NewUdrtkgAmt', UndertakingAmount2, False)

	@property
	def NewXpryDtls(self):
		return self._NewXpryDtls

	@NewXpryDtls.setter
	def NewXpryDtls(self, value):
		self._NewXpryDtls = value if value is not None else base_types.UninitialisedField(self, 'NewXpryDtls', ExpiryDetails1, False)

	@NewXpryDtls.deleter
	def NewXpryDtls(self):
		del self._NewXpryDtls
		self._NewXpryDtls = base_types.UninitialisedField(self, 'NewXpryDtls', ExpiryDetails1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewUdrtkgAmt', type=UndertakingAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewXpryDtls', type=ExpiryDetails1, min=0, max=1, mutex_group=None, array=False),
	))