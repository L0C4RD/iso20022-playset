import base_types
import ImpliedCurrencyAndAmount
import ActiveCurrencyCode
import Max35Text
import CardDataReading8Code
import StoredValueAccountType1Code
import Max45Text
import CardIdentificationType1Code
import Max10Text

class StoredValueAccount2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_XpryDt", "_IdTp", "_AcctTp", "_OwnrNm", "_NtryMd", "_Brnd", "_Ccy", "_Bal", "_Prvdr"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if type(value) != auto else self.make_default("IdTp")

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = None

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def OwnrNm(self):
		return self._OwnrNm

	@OwnrNm.setter
	def OwnrNm(self, value):
		self._OwnrNm = value if type(value) != auto else self.make_default("OwnrNm")

	@OwnrNm.deleter
	def OwnrNm(self):
		del self._OwnrNm
		self._OwnrNm = None

	@property
	def NtryMd(self):
		return self._NtryMd

	@NtryMd.setter
	def NtryMd(self, value):
		self._NtryMd = value if type(value) != auto else self.make_default("NtryMd")

	@NtryMd.deleter
	def NtryMd(self):
		del self._NtryMd
		self._NtryMd = None

	@property
	def Brnd(self):
		return self._Brnd

	@Brnd.setter
	def Brnd(self, value):
		self._Brnd = value if type(value) != auto else self.make_default("Brnd")

	@Brnd.deleter
	def Brnd(self):
		del self._Brnd
		self._Brnd = None

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
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdTp', type=CardIdentificationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=StoredValueAccountType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrNm', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

