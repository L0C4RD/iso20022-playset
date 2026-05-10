from . import base_types
from .GenericIdentification165 import GenericIdentification165
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class IntraDayRequirement1(base_types._BaseFieldType):

	__slots__ = ["_PeakVartnMrgnLblty", "_MrgnAcctId", "_PeakInitlMrgnLblty", "_IntraDayMrgnCall", "_AggtPeakLblty"]
	@property
	def PeakVartnMrgnLblty(self):
		return self._PeakVartnMrgnLblty

	@PeakVartnMrgnLblty.setter
	def PeakVartnMrgnLblty(self, value):
		self._PeakVartnMrgnLblty = value if type(value) != auto else self.make_default("PeakVartnMrgnLblty")

	@PeakVartnMrgnLblty.deleter
	def PeakVartnMrgnLblty(self):
		del self._PeakVartnMrgnLblty
		self._PeakVartnMrgnLblty = None

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

	@property
	def PeakInitlMrgnLblty(self):
		return self._PeakInitlMrgnLblty

	@PeakInitlMrgnLblty.setter
	def PeakInitlMrgnLblty(self, value):
		self._PeakInitlMrgnLblty = value if type(value) != auto else self.make_default("PeakInitlMrgnLblty")

	@PeakInitlMrgnLblty.deleter
	def PeakInitlMrgnLblty(self):
		del self._PeakInitlMrgnLblty
		self._PeakInitlMrgnLblty = None

	@property
	def IntraDayMrgnCall(self):
		return self._IntraDayMrgnCall

	@IntraDayMrgnCall.setter
	def IntraDayMrgnCall(self, value):
		self._IntraDayMrgnCall = value if type(value) != auto else self.make_default("IntraDayMrgnCall")

	@IntraDayMrgnCall.deleter
	def IntraDayMrgnCall(self):
		del self._IntraDayMrgnCall
		self._IntraDayMrgnCall = None

	@property
	def AggtPeakLblty(self):
		return self._AggtPeakLblty

	@AggtPeakLblty.setter
	def AggtPeakLblty(self, value):
		self._AggtPeakLblty = value if type(value) != auto else self.make_default("AggtPeakLblty")

	@AggtPeakLblty.deleter
	def AggtPeakLblty(self):
		del self._AggtPeakLblty
		self._AggtPeakLblty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PeakVartnMrgnLblty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnAcctId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PeakInitlMrgnLblty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraDayMrgnCall', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtPeakLblty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

