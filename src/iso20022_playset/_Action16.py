from . import base_types
from ._ActionDestination1Code import ActionDestination1Code
from ._ActionType14Code import ActionType14Code
from ._AdditionalData1 import AdditionalData1
from ._ContactPersonal1 import ContactPersonal1
from ._ISOMax3ALanguageCode import ISOMax3ALanguageCode
from ._Max140Binary import Max140Binary
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._OutputFormat4Code import OutputFormat4Code
from ._PartyType34Code import PartyType34Code

class Action16(base_types._BaseFieldType):

	__slots__ = ["_CertId", "_Cntt", "_Ctct", "_Dstn", "_DstnAdr", "_DstnTp", "_Frmt", "_Lang", "_OthrDstn", "_OthrDstnTp", "_OthrFrmt", "_OthrTp", "_Sgntr", "_Tp"]
	@property
	def CertId(self):
		return self._CertId

	@CertId.setter
	def CertId(self, value):
		self._CertId = value if type(value) != base_types.auto else self.make_default("CertId")

	@CertId.deleter
	def CertId(self):
		del self._CertId
		self._CertId = None

	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if type(value) != base_types.auto else self.make_default("Cntt")

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = None

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != base_types.auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if type(value) != base_types.auto else self.make_default("Dstn")

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = None

	@property
	def DstnAdr(self):
		return self._DstnAdr

	@DstnAdr.setter
	def DstnAdr(self, value):
		self._DstnAdr = value if type(value) != base_types.auto else self.make_default("DstnAdr")

	@DstnAdr.deleter
	def DstnAdr(self):
		del self._DstnAdr
		self._DstnAdr = None

	@property
	def DstnTp(self):
		return self._DstnTp

	@DstnTp.setter
	def DstnTp(self, value):
		self._DstnTp = value if type(value) != base_types.auto else self.make_default("DstnTp")

	@DstnTp.deleter
	def DstnTp(self):
		del self._DstnTp
		self._DstnTp = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def OthrDstn(self):
		return self._OthrDstn

	@OthrDstn.setter
	def OthrDstn(self, value):
		self._OthrDstn = value if type(value) != base_types.auto else self.make_default("OthrDstn")

	@OthrDstn.deleter
	def OthrDstn(self):
		del self._OthrDstn
		self._OthrDstn = None

	@property
	def OthrDstnTp(self):
		return self._OthrDstnTp

	@OthrDstnTp.setter
	def OthrDstnTp(self, value):
		self._OthrDstnTp = value if type(value) != base_types.auto else self.make_default("OthrDstnTp")

	@OthrDstnTp.deleter
	def OthrDstnTp(self):
		del self._OthrDstnTp
		self._OthrDstnTp = None

	@property
	def OthrFrmt(self):
		return self._OthrFrmt

	@OthrFrmt.setter
	def OthrFrmt(self, value):
		self._OthrFrmt = value if type(value) != base_types.auto else self.make_default("OthrFrmt")

	@OthrFrmt.deleter
	def OthrFrmt(self):
		del self._OthrFrmt
		self._OthrFrmt = None

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != base_types.auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if type(value) != base_types.auto else self.make_default("Sgntr")

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntt', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctct', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=PartyType34Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnAdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnTp', type=ActionDestination1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDstn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDstnTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ActionType14Code, min=0, max=1, mutex_group=None, array=False),
	))

