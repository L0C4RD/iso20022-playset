import base_types
import CashAccount204
import PaymentInstrument17

class CashSettlement3(base_types._BaseFieldType):

	__slots__ = ["_OthrCshSttlmDtls", "_CshAcctDtls"]
	@property
	def OthrCshSttlmDtls(self):
		return self._OthrCshSttlmDtls

	@OthrCshSttlmDtls.setter
	def OthrCshSttlmDtls(self, value):
		self._OthrCshSttlmDtls = value if type(value) != auto else self.make_default("OthrCshSttlmDtls")

	@OthrCshSttlmDtls.deleter
	def OthrCshSttlmDtls(self):
		del self._OthrCshSttlmDtls
		self._OthrCshSttlmDtls = None

	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if type(value) != auto else self.make_default("CshAcctDtls")

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrCshSttlmDtls', type=PaymentInstrument17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAcctDtls', type=CashAccount204, min=0, max=None, mutex_group=None, array=True),
	))

