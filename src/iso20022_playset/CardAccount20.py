from . import base_types
import NameAndAddress3
import CardAccountType3Code
import AccountChoiceMethod1Code
import AccountIdentification80Choice
import Max70Text
import PartyIdentification177Choice
import ActiveCurrencyCode

class CardAccount20(base_types._BaseFieldType):

	__slots__ = ["_AcctNm", "_AcctIdr", "_Svcr", "_AcctOwnr", "_SelctnMtd", "_Ccy", "_SelctdAcctTp"]
	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if type(value) != auto else self.make_default("AcctNm")

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = None

	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if type(value) != auto else self.make_default("AcctIdr")

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = None

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if type(value) != auto else self.make_default("Svcr")

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def SelctnMtd(self):
		return self._SelctnMtd

	@SelctnMtd.setter
	def SelctnMtd(self, value):
		self._SelctnMtd = value if type(value) != auto else self.make_default("SelctnMtd")

	@SelctnMtd.deleter
	def SelctnMtd(self):
		del self._SelctnMtd
		self._SelctnMtd = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def SelctdAcctTp(self):
		return self._SelctdAcctTp

	@SelctdAcctTp.setter
	def SelctdAcctTp(self, value):
		self._SelctdAcctTp = value if type(value) != auto else self.make_default("SelctdAcctTp")

	@SelctdAcctTp.deleter
	def SelctdAcctTp(self):
		del self._SelctdAcctTp
		self._SelctdAcctTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=NameAndAddress3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SelctnMtd', type=AccountChoiceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SelctdAcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
	))

