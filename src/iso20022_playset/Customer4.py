import base_types
import PhoneNumber
import Max35Text
import Max70Text
import TrueFalseIndicator
import CustomerType2Code

class Customer4(base_types._BaseFieldType):

	__slots__ = ["_AuthrsdCtctNm", "_AuthrsdCtctPhneNb", "_VIPInd", "_Tp", "_TaxRegnId", "_RefNb", "_AuthrsdCtctCpny", "_CstmrRltsh"]
	@property
	def AuthrsdCtctNm(self):
		return self._AuthrsdCtctNm

	@AuthrsdCtctNm.setter
	def AuthrsdCtctNm(self, value):
		self._AuthrsdCtctNm = value if type(value) != auto else self.make_default("AuthrsdCtctNm")

	@AuthrsdCtctNm.deleter
	def AuthrsdCtctNm(self):
		del self._AuthrsdCtctNm
		self._AuthrsdCtctNm = None

	@property
	def AuthrsdCtctPhneNb(self):
		return self._AuthrsdCtctPhneNb

	@AuthrsdCtctPhneNb.setter
	def AuthrsdCtctPhneNb(self, value):
		self._AuthrsdCtctPhneNb = value if type(value) != auto else self.make_default("AuthrsdCtctPhneNb")

	@AuthrsdCtctPhneNb.deleter
	def AuthrsdCtctPhneNb(self):
		del self._AuthrsdCtctPhneNb
		self._AuthrsdCtctPhneNb = None

	@property
	def VIPInd(self):
		return self._VIPInd

	@VIPInd.setter
	def VIPInd(self, value):
		self._VIPInd = value if type(value) != auto else self.make_default("VIPInd")

	@VIPInd.deleter
	def VIPInd(self):
		del self._VIPInd
		self._VIPInd = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def TaxRegnId(self):
		return self._TaxRegnId

	@TaxRegnId.setter
	def TaxRegnId(self, value):
		self._TaxRegnId = value if type(value) != auto else self.make_default("TaxRegnId")

	@TaxRegnId.deleter
	def TaxRegnId(self):
		del self._TaxRegnId
		self._TaxRegnId = None

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if type(value) != auto else self.make_default("RefNb")

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = None

	@property
	def AuthrsdCtctCpny(self):
		return self._AuthrsdCtctCpny

	@AuthrsdCtctCpny.setter
	def AuthrsdCtctCpny(self, value):
		self._AuthrsdCtctCpny = value if type(value) != auto else self.make_default("AuthrsdCtctCpny")

	@AuthrsdCtctCpny.deleter
	def AuthrsdCtctCpny(self):
		del self._AuthrsdCtctCpny
		self._AuthrsdCtctCpny = None

	@property
	def CstmrRltsh(self):
		return self._CstmrRltsh

	@CstmrRltsh.setter
	def CstmrRltsh(self, value):
		self._CstmrRltsh = value if type(value) != auto else self.make_default("CstmrRltsh")

	@CstmrRltsh.deleter
	def CstmrRltsh(self):
		del self._CstmrRltsh
		self._CstmrRltsh = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthrsdCtctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdCtctPhneNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VIPInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CustomerType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRegnId', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdCtctCpny', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrRltsh', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

