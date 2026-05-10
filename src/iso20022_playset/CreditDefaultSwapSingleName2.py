import base_types
import TrueFalseIndicator
import DerivativePartyIdentification1Choice
import ActiveOrHistoricCurrencyCode

class CreditDefaultSwapSingleName2(base_types._BaseFieldType):

	__slots__ = ["_NtnlCcy", "_SvrgnIssr", "_RefPty"]
	@property
	def NtnlCcy(self):
		return self._NtnlCcy

	@NtnlCcy.setter
	def NtnlCcy(self, value):
		self._NtnlCcy = value if type(value) != auto else self.make_default("NtnlCcy")

	@NtnlCcy.deleter
	def NtnlCcy(self):
		del self._NtnlCcy
		self._NtnlCcy = None

	@property
	def SvrgnIssr(self):
		return self._SvrgnIssr

	@SvrgnIssr.setter
	def SvrgnIssr(self, value):
		self._SvrgnIssr = value if type(value) != auto else self.make_default("SvrgnIssr")

	@SvrgnIssr.deleter
	def SvrgnIssr(self):
		del self._SvrgnIssr
		self._SvrgnIssr = None

	@property
	def RefPty(self):
		return self._RefPty

	@RefPty.setter
	def RefPty(self, value):
		self._RefPty = value if type(value) != auto else self.make_default("RefPty")

	@RefPty.deleter
	def RefPty(self):
		del self._RefPty
		self._RefPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtnlCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrgnIssr', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPty', type=DerivativePartyIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
	))

