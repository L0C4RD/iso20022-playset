# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount204
from . import PaymentInstrument17

class CashSettlement3(base_types._BaseFieldType):

	__slots__ = ["_CshAcctDtls", "_OthrCshSttlmDtls"]
	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'CshAcctDtls', CashAccount204, True)

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = base_types.UninitialisedField(self, 'CshAcctDtls', CashAccount204, True)

	@property
	def OthrCshSttlmDtls(self):
		return self._OthrCshSttlmDtls

	@OthrCshSttlmDtls.setter
	def OthrCshSttlmDtls(self, value):
		self._OthrCshSttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'OthrCshSttlmDtls', PaymentInstrument17, True)

	@OthrCshSttlmDtls.deleter
	def OthrCshSttlmDtls(self):
		del self._OthrCshSttlmDtls
		self._OthrCshSttlmDtls = base_types.UninitialisedField(self, 'OthrCshSttlmDtls', PaymentInstrument17, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcctDtls', type=CashAccount204, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrCshSttlmDtls', type=PaymentInstrument17, min=0, max=None, mutex_group=None, array=True),
	))