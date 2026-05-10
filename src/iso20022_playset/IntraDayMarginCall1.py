from . import base_types
import ActiveCurrencyAndAmount
import GenericIdentification165
import ISODateTime

class IntraDayMarginCall1(base_types._BaseFieldType):

	__slots__ = ["_TmStmp", "_IntraDayCall", "_MrgnAcctId"]
	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	@property
	def IntraDayCall(self):
		return self._IntraDayCall

	@IntraDayCall.setter
	def IntraDayCall(self, value):
		self._IntraDayCall = value if type(value) != auto else self.make_default("IntraDayCall")

	@IntraDayCall.deleter
	def IntraDayCall(self):
		del self._IntraDayCall
		self._IntraDayCall = None

	@property
	def MrgnAcctId(self):
		return self._MrgnAcctId

	@MrgnAcctId.setter
	def MrgnAcctId(self, value):
		self._MrgnAcctId = value if type(value) != auto else self.make_default("MrgnAcctId")

	@MrgnAcctId.deleter
	def MrgnAcctId(self):
		del self._MrgnAcctId
		self._MrgnAcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraDayCall', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnAcctId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
	))

